import subprocess
import socket

dest_ip = '10.10.10.3'
dest_port = 33333
locations_list = [
    ['mondev1', '10.10.10.4'],
    ['mondev2', '10.10.10.5'],
    ['mondev3', '10.10.10.6'],
    ['mondev4', '10.10.10.7']
]


def ping(host):
    command = ['ping', '-c', '1', host]
    return subprocess.call(command) == 0


def transmitter(status):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((dest_ip, dest_port))
    client.sendall(status.encode('utf-8'))
    client.close()


for dest, ip in locations_list:
    test = ping(ip)
    if test == 1:
        status = dest + '1'
        transmitter(status)
    else:
        status = dest + '0'
        transmitter(status)