# Weather alerting system
This is a weather alerting system. Every hour the api makes a call to a server that stores weather related values from sensors located in three farms in Thrace, Greece. 
Based on the received values, a trained LSTM model makes a prediction. If the difference between the predicted value and the current value exceeds a predefined threshold
then the api sends an alert which is registered to a database.
