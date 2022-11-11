<p align="center">
  <a href="" rel="noopener">
 <img src="fig/iot-icon.png" alt="GSL Final Course - ITA & Tecnológico de Monterrey" width="100"></a>
</p>


# GSL Final Course - ITA & Tecnológico de Monterrey
## Command and Control to support the operations.
## User stories 

### 1.US 01
AS a potential disaster victim,  I´d like to ask for help, by sending my position and my health condition, personal information (name, cell phone number …), and receive the feedback that they were given.   So I can be sure that my helpers can find me.

| SR No | Statements                                                                                                                                           | Description                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1     | Scenario                                   | Sending a position to a Central Agency.                 |
| 2     | Given                                          | The victim navigates to the initial page.                 |
| 3     | When                                                  | victim select <report position> button.                     |
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
|4     |Then                                                                      |System shows a  <new position icon>, blinking on the operation map.      |
|5     |Given                                                                     |The Agency Operator is focused on the operation map.                     |
|6     |When                                                                      |The Agency Operator double clicks the blinking icon.                     |
|7     |Then                                                                      |The system shows *<forward position window>*.                            |
|8     |Given                                                                     |The Agency Operator is focused on the  *<forward position window>*.      |
|9     |When                                                                      |The Agency Operator selects a rescue team.                               | 
|10    |And                                                                       |The User selects the <send position> button.                             |
|11    |Then                                                                      |The system sends the position data to the selected team.                 |


### 3.US 03
As State official, I want to receive the position and the victims data, so we can get right to the rescue point faster.
| SR No | Statements                                                                                                                                           | Description                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
|1     |Scenario                                                                      |Receiving a position from a Victim.                                  |
|2     |Given                                                                         |The State official is receiving victims' data.                       |
|3     |When                                                                          |The System received a victim position, from central.                 |
|4     |Then                                                                          |System shows a  *<new position icon>*, blinking on the map.          |
|5     |Given                                                                         |The State official is focused on the map of operation.               |
|6     |When                                                                          |The State official double clicks the blinking icon.                  |
|7     |Then                                                                          |The system shows a <report window> with the position.                |
|8     |Given                                                                         |The State official is focused on the  *<report window>*.             |
|9     |When                                                                          |The State official push <position received> button.                  |
|10    |Then                                                                          |The system records the position data was received.                   |


