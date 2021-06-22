import csv
import time
import requests


def sender(message):
    url = f'https://api.telegram.org/bot1234567890:AAAXXXXWWWPPPCCC_QQQZZZ1EeKM-rbDxc8d/sendMessage?chat_id=12345678&text={message}'
    return requests.post(url)


def renamer(name):
    if name == 'mondev1':
        newname = 'Monitored Device #1'
        name = newname
        return name
    if name == 'mondev2':
        newname = 'Camera'
        name = newname
        return name
    if name == 'mondev3':
        newname = 'Server'
        name = newname
        return name
    if name == 'mondev4':
        newname = 'PC'
        name = newname
        return name
    else:
        return name


while True:
    with open('log.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    i = 1
    while i < 7:
        n = i * -1
        timenow = time.time_ns()
        diff = int((timenow - int(data[n][0])) / 1e9 / 60)
        if diff > 5:
            break
        else:
            if int(data[n][2]) == 0:
                name = str(data[n][1])
                right_name = renamer(name)
                message = right_name + ' is DOWN'
                sender(message)
            else:
                pass
        i = i + 1
    time.sleep(600)
