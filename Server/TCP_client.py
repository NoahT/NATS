#!/usr/bin/env python
''' A simple TCP client'''

import socket

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"



class TCP_client:
  def __init__(self, host, port):
    self.host, self.port = host, port
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def setup(self):
    '''Initializes the client connection'''
    self.client.connect((host, port))

  def send(self, message):
    '''Sends a byte message to the client'''
    message = self.to_bytes(message)
    self.client.send(message)

  def recieve(self):
    ''' Recives and parses the recieved message '''
    message = self.client.recv(4096)
    return self.to_str(message)

  def to_bytes(self, str_or_byte):
    '''Encodes the passed str or bytes into utf-8'''
    if isinstance(str_or_byte, str):
      str_or_byte = str_or_byte.encode('utf-8')
    return str_or_byte

  def to_str(self, str_or_byte):
    '''Decodes the passed str or bytes from utf-8'''
    if isinstance(str_or_byte, bytes):
      str_or_byte = str_or_byte.decode('utf-8')
    return str_or_byte

if __name__ == '__main__':
  # host = "www.google.com"
  host = socket.gethostbyname(socket.gethostname())
  # port = 80
  port = 10135
  
  client = TCP_client(host, port)
  client.setup()
  client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
  message = client.recieve()
  print("Message recived: %s" % message)











