'''
Author: Taylor Cochran
Poject: NATS
Version: 1.0

Algorythm:
  1) select host and port
  2) create socket object
  3) connect to host
  4) send data
  5) recieve data
'''
import socket


'''
##########################
####     CLIENT       ####
##########################
'''
def setup(host=socket.gethostbyname(socket.gethostname()),
          port=10135):
  '''Creates the client/socket object'''
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))
  return client


def send(client, message="This is a test message"):
  '''Sends the passed message to the client'''
  client.send(to_bytes(message))


def recieve(client):
  '''Receives the data from the server'''
  response = client.recv(4096)
  return response


'''
##########################
#### HELPER FUNCTIONS ####
##########################
'''
def to_str(bytes_or_str):
  '''
  Accepts a 8-bit or string and returns a string
  '''
  if isinstance(bytes_or_str, bytes):
    value = bytes_or_str.decode('utf-8')
  else:
    value = bytes_or_str
  return value


def to_bytes(bytes_or_str):
  '''
  Accepts a 8-bit or string and returns an 8-bit
  '''
  if isinstance(bytes_or_str, str):
    value = bytes_or_str.encode('utf-8')
  else:
    value = bytes_or_str
  return value

'''
##########################
####      MAIN        ####
##########################
'''
if __name__ == '__main__':
  client = setup()
  send(client, to_bytes("get people"))
  response = to_str(recieve(client))
  print(response)

