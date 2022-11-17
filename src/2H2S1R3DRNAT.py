#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Host, Node, OVSKernelSwitch
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.log import setLogLevel, info
from subprocess import call
from mininet.link import Intf
from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, adhoc
from mn_wifi.net import Mininet_wifi
from mn_wifi.telemetry import telemetry
from mn_wifi.wmediumdConnector import interference



def myNetwork():
    
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)
    info( '*** Adding controller\n' )
    info( '*** Add switches/APs\n')
    s1  = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2  = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    #r2 = net.addHost('r2', cls=Node, ip='0.0.0.0')
    r2 = net.addHost('r2', cls=Node)
    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1', port=6633 )
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')# Hostonly para o gest
    info( '*** Add hosts/stations\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.11/24', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.12/24', defaultRoute=None)
    info("*** Creating nodes\n")
    dr1 = net.addStation('dr1', mac='00:00:00:00:00:01', ip='11.0.0.11/24',
                         position='30,60,0')
    dr2 = net.addStation('dr2', mac='00:00:00:00:00:02', ip='11.0.0.12/24',
                         position='70,30,0')
    dr3 = net.addStation('dr3', mac='00:00:00:00:00:03', ip='11.0.0.13/24',
                         position='10,20,0')

    info( '*** Add links\n')
    net.addLink(r2, s2)
    net.addLink(h2, s2)
    net.addLink(h1, s2)
    net.addLink(dr1, s2)#Saindo para o guest host-only
    #r2_node = net.getNodeByName('r2')
    #r2.attach("ens35")
    
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    net.addLink(dr1, cls=adhoc, intf='dr1-wlan0',
                ssid='adhocNet', proto='batman_adv', mode='g', channel=5, ht_cap='HT40+')

    net.addLink(dr2, cls=adhoc, intf='dr2-wlan0',
                ssid='adhocNet', proto='batman_adv', mode='g', channel=5, ht_cap='HT40+')

    net.addLink(dr3, cls=adhoc, intf='dr3-wlan0',
                ssid='adhocNet', proto='batman_adv', mode='g', channel=5, ht_cap='HT40+')

    
    info( '*** Starting network\n')
    net.build()
    c0.start()
    s1.start( [c0] )
    s2.start( [c0] )
    r2.cmd("ifconfig r2-eth0 0")
    r2.cmd("ip addr add 10.0.1.1/24 brd + dev r2-eth0")
    r2.cmd("ip addr add 10.0.2.1/24 brd + dev r2-eth0")
    r2.cmd("ip addr add 12.0.0.1/24 brd + dev r2-eth0")
    r2.cmd("ip addr add 192.168.199.131/24 brd + dev r2-eth0")
    Intf("ens33",node=s1)#NAT
    #Intf("ens33",node=r1)#NAT
    Intf("ens35",node=s2)#Host-only
    #info( "*** type r2 --->",type(r2), "\n")    
    r2.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    r2.cmd("ip route add 11.0.0.0/24 via 12.0.0.11")
    r2.cmd("route add default gw 192.168.0.1")    
    h1.cmd("ip route add 10.0.2.0/24 via 10.0.1.1")
    h1.cmd("ip route add 11.0.0.0/24 via 10.0.1.1")
    #h1.cmd("route add default gw 10.0.1.1")
    h1.cmd("ip route add 192.168.199.0/24 via 10.0.1.1") # para responder o guest
    dr1.cmd("ifconfig dr1-eth0 12.0.0.11/24")
    #dr1.cmd("ifconfig dr1-eth1 192.168.226.11/24") #tentando pegar do DHCP
    dr1.cmd("ifconfig dr1-eth1 0.0.0.0")
    net.addLink(dr1, s1)#Saindo para o NAT internet
    dr1.cmd("ip route add 192.168.199.0/24 via 12.0.0.1") # para responder o guest
    dr1.cmd("ip route add 10.0.2.0/24 via 12.0.0.1") # para responder h2
    #dr1.cmd("route add default gw 12.0.0.1")
    #dr1.cmd("route add default gw 192.168.226.144")
    dr1.cmd("sysctl -w net.ipv4.ip_forward=1")
    dr1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    dr2.cmd("route add default gw 11.0.0.11")
    dr2.cmd("sysctl -w net.ipv4.ip_forward=1")
    dr2.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    dr3.cmd("route add default gw 11.0.0.11")
    dr3.cmd("sysctl -w net.ipv4.ip_forward=1")
    dr3.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
    h2.cmd("ip route add 10.0.1.0/24 via 10.0.2.1")    
    h2.cmd("ip route add 11.0.0.0/24 via 10.0.2.1")
    #h2.cmd("route add default gw 10.0.2.1")
    
    s1.cmd("ovs-ofctl add-flow s1 priority=1,arp,actions=flood")
    s1.cmd("ovs-ofctl add-flow s1 priority=65535,ip,dl_dst=00:00:00:00:01:00,actions=output:1")
    s1.cmd("ovs-ofctl add-flow s1 priority=10,ip,nw_dst=192.168.226.0/24,actions=output:2")
    s1.cmd("ovs-ofctl add-flow s1 priority=101,ip,nw_dst=11.0.0.0/24,actions=output:3")
    
    
    s2.cmd("ovs-ofctl add-flow s2 priority=1,arp,actions=flood")
    s2.cmd("ovs-ofctl add-flow s2 priority=65535,ip,dl_dst=00:00:00:00:01:00,actions=output:1")
    s2.cmd("ovs-ofctl add-flow s2 priority=10,ip,nw_dst=10.0.1.0/24,actions=output:2")
    s2.cmd("ovs-ofctl add-flow s2 priority=1000,ip,nw_dst=10.0.2.0/24,actions=output:3")
    s2.cmd("ovs-ofctl add-flow s2 priority=10,ip,nw_dst=12.0.0.0/24,actions=output:4")
    s2.cmd("ovs-ofctl add-flow s2 priority=1500,ip,nw_dst=11.0.0.0/24,actions=output:5")
    
    #s1.cmd("ovs-ofctl add-flow s1 priority=10,ip,nw_dst=10.0.3.0/24,actions=output:4")

    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('s1').start([])
    net.get('s2').start([])

    info( '*** Post configure nodes\n')
    dr1.cmd("dhclient dr1-eth1")
    dr1.cmd("iptables -t  nat -A POSTROUTING -o dr1-eth1 -j MASQUERADE")
    #info( '*** DHCP Add ',r1.IP()," \n")
    #info("route add default gw"+r1.IP())
    #dr1.cmd("route add default gw"+r1.IP())
    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

