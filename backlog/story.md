GSL Final Course - ITA & Tecnológico de Monterrey
Command and Control to support the operations.
User stories 

# 1.US 01
AS a potential disaster victim,  I´d like to ask for help, by sending my position and my health condition, personal information (name, cell phone number …), and receive the feedback that they were given.   So I can be sure that my helpers can find me.



User story
AS a potential disaster victim,  I´d like to ask for help, by sending my position and my health condition, personal information (name, cell phone number …), and receive the feedback that they were given.   So I can be sure that my helpers will find me.
Scenario
Sending a position to a Central Agency.
Given
The victim navigates to the initial page.
When 
victim select <report position> button.
Then
The system sends cell phone position and personal information to the central. 
Given
The victim is waiting for confirmation his data was given.
When
The confirmation was received.
Then
The system confirms to the victim that his data was given.






#2. US 02
As an Agency Operator, I´d like to know, in real time, the people's position,  personal information (name, cell phone number …)  and condition and forward it to the rescue team and track the situation of each of them. So we can control each rescue mission and try to elaborate a list of potential victims.



User story
As an Agency Operator, I´d like to know, in real time, the people's position,  personal information (name, cell phone number …)  and condition and forward it to the rescue team and track the situation of each of them. So we can control each rescue mission and try to elaborate a list of victims.
Scenario
Receiving a position from a victim.
Given
The operation center is receiving victims’ data.
When
New victim data comes from the network.
Then
System shows a  <new position icon>, blinking on the operation map.
Given
The Agency Operator is focused on the operation map.
When 
The Agency Operator double clicks the blinking icon. 
Then
The system shows <forward position window>.
Given
The Agency Operator is focused on the  <forward position window>.
When 
The Agency Operator selects a rescue team. 
And
The User selects the <send position> button.
Then
The system sends the position data to the selected team.










# 3.US 03
As State official, I want to receive the position and the victims data, so we can get right to the rescue point faster.

User story
As State official, I want to receive the position and the victims data, so we can get right to the rescue point faster.
Scenario
Receiving a position from a Victim.
Given
The State official is receiving victims' data.
When
The System received a victim position, from central.
Then
System shows a  <new position icon>, blinking on the map.
Given
The State official is focused on the map of operation.
When 
The State official double clicks the blinking icon. 
Then
The system shows a <report window> with the position.
Given
The State official is focused on the  <report window>.
When
The State official push <position received> button.
Then
The system records the position data was received.


