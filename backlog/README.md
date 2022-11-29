<p align="center">
  <a href="" rel="noopener">
 <img src="../fig/iot-icon.png" alt="GSL Final Course - ITA & Tecnológico de Monterrey" width="100"></a>
</p>
<h2 align="center">GSL Final Course - ITA & Tecnológico de Monterrey</h2>
<h3 align="center">Command and Control Support System</h3>
<h1 align="center">User stories </h1>


### 1.US 01
AS a potential disaster victim,  I´d like to ask for help, by sending my position and my health condition, personal information (name, cell phone number …), and receive the feedback that they were given.   So I can be sure that my helpers can find me.

| SR No | Statements                                                                                                                                           | Description                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1     | Scenario                                   | Sending a position to a Central Agency.                 |
| 2     | Given                                          | The victim navigates to the initial page.                 |
| 3     | When                                                  | victim select *report position* button.                     |
| 4     | Then                                                             | The system sends cell phone position and personal information to the central.                     |
| 5     | Given                                                | The victim is waiting for confirmation his data was given.                     |
| 6     | When                                                   | The confirmation was received.                    |
| 7     | Then                    | The system confirms to the victim that his data was given.                      |

### 2.US 02
As an Agency Operator, I´d like to know, in real time, the people's position,  personal information (name, cell phone number …)  and condition and forward it to the rescue team and track the situation of each of them. So we can control each rescue mission and try to elaborate a list of potential victims.

| SR No | Statements                                                                                                                                           | Description                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
|1     |Scenario                                                                  |Receiving a position from a victim.                                     |
|2     |Given                                                                     |The operation center is receiving victims’ data.                         |
|3     |When                                                                      |New victim data comes from the network.                                  |
|4     |Then                                                                      |System calculates Severity (SEV), based on received data.      |
|5     |Then                                                                      |System shows a  *new position icon*, blinking on the operation map. The icon is green, if  SEV is low; yellow, if SEV is middle; and red, if SEV is high.    |
|6     |Given                                                                     |The Agency Operator is focused on the operation map.                     |
|7     |When                                                                      |The Agency Operator double clicks the blinking icon.                     |
|8     |Then                                                                      |The system shows *forward position window*.                              |
|9     |Given                                                                     |The Agency Operator is focused on the  *forward position window*.      |
|10     |When                                                                      |The Agency Operator selects a rescue team.                               | 
|11    |And                                                                       |The Agency Operator selects the *send position* button.                  |
|12    |Then                                                                      |The system sends the position data to the selected team.                 |


### 3.US 03
As State official, I want to receive the position and the victims data, so we can get right to the rescue point faster.
| SR No | Statements                                                                                                                                           | Description                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
|1     |Scenario                                                                      |Receiving a position from a Victim.                                  |
|2     |Given                                                                         |The State official is receiving victims' data.                       |
|3     |When                                                                          |The System received a victim position, from central.                 |
|4     |Then                                                                          |System shows a  *new position icon*, blinking on the map.          |
|5     |Given                                                                         |The State official is focused on the map of operation.               |
|6     |When                                                                          |The State official double clicks the blinking icon.                  |
|7     |Then                                                                          |The system shows a *report window* with the position.                |
|8     |Given                                                                         |The State official is focused on the  *report window*.             |
|9     |When                                                                          |The State official push *position received* button.                  |
|10    |Then                                                                          |The system records the position data was received.                   |


<h1 align="center">Dashboard requirements </h1>

<ol>
<li>The dashboard eceives all the MQTT messages from the users in the central broker.</li>
<li>The central broker will persist the messages in a SQL database.</li>
<li>The dashboard will make queries in the database and fill the dashboard.</li>
</ol> 
  
<p>The dashboard supports the rescue team in identifying and prioritizing which actions are required to keep the disaster victims. In addition, the dashboard will make queries to the database (data source) and process the answer to present the information in a more helpful format.</p>

<p>As we told you before, the users will publish messages where the content is the id, severity, and geo-location. The severity (SEV) is used to calculate the risk, where the risk has three levels: low, middle, or high.</p>


<ul>
<li>A dynamic map where you identify the risk situation colors the node positions.</li>
<li>A dynamic map where you identify the node positions, and they are colored by the severity situation.</li>
<li>A bar chart shows the number of nodes classified by risk.</li>
<li>A bar chart shows the number of nodes classified by risk.</li>
<li>A bar chart shows the number of nodes classified by severity.</li>
</ul>

