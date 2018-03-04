#!/usr/local/bin/python3
''' A simple TCP server'''

import Log
import socket
import threading

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class TCP_server:
  def __init__(self, ip, port):
    self.ip, self.port = ip, port
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.setsockopt(socket.SOL_SOCKET, 
                           socket.SO_REUSEADDR, 
                           1)
    self.client_address = None

    self.exception_log = "/Users/taylorcochran/Documents" 
    self.exception_log += "/ServerLogs/Server/Exceptions.txt"
    self.transaction_log = "/Users/taylorcochran/Documents" 
    self.transaction_log += "/ServerLogs/Server/Transactions.txt"

    self.log = Log.Log()
    self.log.exception_file = self.exception_log
    self.log.data_file = self.transaction_log

  def run_server(self):
    '''
    Spins up the client thread to hangle incoming data.
    In the event that a client connects calls handle_client
    '''
    self.server.bind((ip, port))
    self.server.listen(5)
    while True:
      client, self.client_address = self.server.accept()
      
      print("ཽ", end="")
      print("\tཽ"*4)
      print("༾༽༽༼༼༿     Connection      ༾༽༽༼༼༿")
      print("༺༺༺༺༺  %s:%d ༻༻༻༻༻\n" % (self.client_address[0],
                                                    self.client_address[1]))
      try:
        client_handle = threading.Thread(target=self.handle_client,
                                         args=(client,)) 
        client_handle.start()
      except RuntimeError as e:
        self.log.log_exception(e)
         
        
  def handle_client(self, client_socket):
    '''
    Decids what to do with the connected client.
    1) Recieve the message
    2) log it
    3) Attempt to parse it
    4) Get the response
    5) Log the response
    6) Send the Response
    7) Close the connection
    '''
    request = client_socket.recv(1024)
    request = self.to_str(request)
    self.log.log_request(request, 
                         self.client_address[0],
                         self.client_address[1]
                         )
    response = self.handle_request(request)
    response = self.to_str(response)
    self.log.log_response(response, 
                         self.client_address[0], 
                         self.client_address[1]
                         )
    print("ཽ", end="")
    print("\tཽ"*4)

    response = self.to_bytes(response)
    client_socket.send(response)
    client_socket.close()

  def handle_request(self, request):
    ''' 
    Attempts to parse the recieved request.
    Right now this is simply a place holder
    '''
    response = "ؿӬ٣ՄӬ٣: %s:%d\n" % (self.ip,self.port)
    response += "Has recieved your request\n"
    return response

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
  ip = socket.gethostbyname(socket.gethostname())
  port = 10135
  print( "༾༽༽༼༼༿       ؿӬ٣ՄӬ٣        ༾༽༽༼༼༿")
  print("༺༺༺༺༺  %s:%d ༻༻༻༻༻" % (ip, port))
  server = TCP_server(ip, port)
  server.run_server()



