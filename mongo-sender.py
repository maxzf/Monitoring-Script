import pymongo
import time
import urllib.parse
import requests
username = urllib.parse.quote_plus('username')
password = urllib.parse.quote_plus('password')

ß
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

myclient = pymongo.MongoClient('mongodb://%s:%s@10.10.10.3:33333' % (username, password))
mydb = myclient['status']
mycol1 = mydb['status1']
mycol2 = mydb['status2']

while True:

  myres1 = mycol1.find().sort("_id", -1).limit(4)
  myres2 = mycol2.find().sort("_id", -1).limit(3)

  for x in myres1:
    name = x['name']
    stat = x['status']
    if stat == '1':
      pass
      # print('test', name, 'OK')
    else:
      # print('oops!', name, 'is down')
      right_name = renamer(name)
      message = right_name + ' is DOWN'
      sender(message)
  for x in myres2:
    name = x['name']
    stat = x['status']
    if stat == '1':
      pass
      # print('test', name, 'OK')
    else:
      # print('oops!', name, 'is down')
      right_name = renamer(name)
      message = right_name + ' is DOWN'
      sender(message)
  time.sleep(300)

