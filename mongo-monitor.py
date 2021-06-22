import subprocess
import pymongo
import time
import urllib.parse
username = urllib.parse.quote_plus('username')
password = urllib.parse.quote_plus('password')
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


def transmitter(dest, status):
    myclient = pymongo.MongoClient('mongodb://%s:%s@10.10.10.3:33333' % (username, password))
    mydb = myclient['status']
    mycol = mydb['status1']
    tnow = str(time.time_ns())[:-6]
    mydict = {'date': tnow, 'name': dest, 'status': status}
    x = mycol.insert_one(mydict)


while True:
    for dest, ip in locations_list:
        test = ping(ip)
        if test == 1:
            status = '1'
            transmitter(dest, status)
        else:
            status = '0'
            transmitter(dest, status)
    tm1 = time.time()
    tm = time.ctime(tm1)
    print('Check completed. Data loaded.', tm)
    time.sleep(300)
