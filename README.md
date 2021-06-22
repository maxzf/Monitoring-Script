# Monitoring-Script
 Scripts for monitoring availability of network devices

## First gen communicates via socket connection.
- *socket-client.py* pings devices by list and transmits to server a result
- *socket-server.py* lisents on the port and writes to csv file all received data
- *socket-sender.py* reads csv file and sends a message via telegram bot in case any device is unavailable
    
## Second gen works via MongoDB database.
- *mongo-monitor.py* pings network devices and writes to DB a result of test
- *mongo-sender.py* checks several latest records and notify via telegram bot if any device is unavailable
