
import socket
import os
import sys
import requests

connection= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host= '192.168.43.44'
port= 8000

print('waiting for connection')
try:
  connection.connect((host,port))
except socket.error as etaksambung:
 print(str(etaksambung))

Response= connection.recv(1024)
print(Response)

while True:
 links= requests.get('https://www.w3schools.com/')
 print(links.content)
 print(links.url)

connection.close()
