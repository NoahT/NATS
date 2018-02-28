'''
Author: Taylor Cochran
Poject: NATS
Version: 0.1

Algorythm:
  1) select host and port
  2) create socket object
  3) connect to host
  4) send data
  5) recieve data
'''
import socket

def setup(host=socket.gethostbyname(socket.gethostname()),
          port=10135):
  '''Creates the client/socket object'''
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  return client

def send(client, message="This is a test message"):
  '''Sends the passed message to the client'''
  client.send(message)

def recieve(client):
  '''Receives the data from the server'''
  response = client.recv(4096)
  return response


if __name__ == '__main__':
  client = setup()
  send(client, "Hello Server!")
  response = recieve(client)
  print response

