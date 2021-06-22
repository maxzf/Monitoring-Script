# Monitoring-Script
 Scripts for monitoring availability of network devices

## First gen communicates via socket connection.
    - *socket-client* pings devices by list and transmots to server a result
    - *socket-server* lisents on the port and writes to csv file all recieved data
    - *socket-sender* reads csv file and sends a message via telegram bot in case any devise is unavailable
    
## Second gen works via MongoDB database.
	- *mongo-monitor* in loop pings network devices and writes to DB a result of test
	- *mongo sender* in loop checks several latest records and notifys via telegram bot if any device is unavailable