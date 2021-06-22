import socket
import time
import csv

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8888))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client += data.decode('utf-8')
        testtime = time.time_ns()
        with open('log.csv', 'a', newline='') as log_file:
            writer = csv.writer(log_file)
            writer.writerow([testtime, from_client[0:7], from_client[7]])
    conn.close()
    