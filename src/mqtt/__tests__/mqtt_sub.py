import random
import mysql.connector
from paho.mqtt import client as mqtt_client


broker = 'dev.tec.fev.com.mx'
port = 1884
top_temp = "srv/info"
client_id = f'python-mqtt-{random.randint(0, 1000)}'

username = 'bridge1'
password = 'bridge123456789'

def mysqlcon():
  mydb = mysql.connector.connect(
  host="dev.tec.fev.com.mx",
  user="demo",
  password="Iot123456789%",
  database="events")
  return mydb


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client,conexion):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        sqlmessend(conexion,msg.payload.decode())
    client.subscribe(top_temp)
    client.on_message = on_message

def sqlmessend(mydb, msg):
    msgl = msg.split(':')
    print(msgl[1], msgl[2],msgl[3]);
    mycursor = mydb.cursor()
    sql = "INSERT INTO events (lat, lon, color) VALUES (%s,%s,%s)"
    val = (msgl[3], msgl[4],msgl[2])
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")



def run():
    client = connect_mqtt()
    con = mysqlcon()
    subscribe(client,con)
    client.loop_forever()

run()