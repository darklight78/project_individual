import socket
import os
import sys
import http.server
import socketserver
from _thread import *
import threading

sambung= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= ''
port= 8000
threadCount=0

try:
   sambung.bind((host, port))
   print('socket bind dengan port', port)
except socket.error as takboleh:
  print(str(takboleh))
#sambung.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sambung.listen(5)
print('socket sedang mendengar network', port)


def threaded_client(sambung):
  #data diterima oleh client
  sambung.send(str.encode('welcome to the server\n'))
  while True:
   data=sambung.recv(2048)
   reply= 'server says:' +data.decode('utf-8')
   if not data:
    break
   sambung.sendall(str.encode(reply))
  sambung.close()

while True:
   client, address= sambung.accept()
   print('connected to:' +address[0] +':' +str(address[1]))
   start_new_thread(threaded_client, (client, ))
   threadCount+= 1
   print('Thread Number:' +str(threadCount))

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  print('http server is starting...')
  server_address= ('192.168.43.44', 80)
  httpd= server_class(server_address, handler_class)
  while keep_running():
    httpd.handle_request()
    print('http server is running..')

if _name_ == '_main_':
  run()
