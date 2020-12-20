import socket
import os
import sys
import requests as req2

#http_server= sys.argv[1]
#con=httplib.HTTPConnection(http_server)
clientSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.43.44'
port=8000

print('waiting for connection')
try:
  clientSocket.connect((host,port))
except socket.error as etakboleh:
  print(str(etakboleh))

Respond= clientSocket.recv(1024)
print(Respond)

while True:
  linky=req2.get('http://www.amazon.com/')
  print(linky.url)
  print(linky.text)

clientSocket.close()

