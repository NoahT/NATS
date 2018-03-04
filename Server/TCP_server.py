#!/usr/local/bin/python3
''' A simple TCP server'''

import Helper
import Log
import socket
import threading
import Transaction

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class TCP_server(object):
  def __init__(self, ip, port):
    self.ip, self.port = ip, port
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.setsockopt(socket.SOL_SOCKET, 
                           socket.SO_REUSEADDR, 
                           1)
    self.helper = Helper.Helper()
    self.wrapper = Transaction.Wrapper(self.ip, self.port)
    self.client_address = None

  def run_server(self):
    '''Spins up the client thread to hangle incoming data.'''
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
    '''Calls the transaction wrapper
    Args:
        client_socket: the client connection
    '''
    request = client_socket.recv(1024)
    response = self.wrapper.process_request(request, self.client_address)
    response = self.helper.to_bytes(response)
    client_socket.send(response)
    client_socket.close()


if __name__ == '__main__':
  ip = socket.gethostbyname(socket.gethostname())
  port = 10135
  print( "༾༽༽༼༼༿       ؿӬ٣ՄӬ٣        ༾༽༽༼༼༿")
  print("༺༺༺༺༺  %s:%d ༻༻༻༻༻" % (ip, port))
  server = TCP_server(ip, port)
  server.run_server()



