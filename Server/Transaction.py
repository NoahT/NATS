#!/usr/local/bin/python3
''' A simple transaction wrapper'''

import Helper
import Log

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class Wrapper(object):
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port
    self.helper = Helper.Helper()
    self.log = Log.Log()
    exception_log = "/Users/taylorcochran/Documents" 
    exception_log += "/ServerLogs/Server/Exceptions.txt"
    transaction_log = "/Users/taylorcochran/Documents" 
    transaction_log += "/ServerLogs/Server/Transactions.txt"
    self.log.exception_file = exception_log
    self.log.data_file = transaction_log

  def process_request(self, request, client_address):
    '''Attempts to process the request sent by the client'''
    reply = "HTTP/1.1 400 Bad Request"
    request = self.helper.to_str(request)
    if self.check_request(request):
      self.log.log_request(request, 
                           client_address[0],
                           client_address[1]
                           )
      reply = self.process_response(request, client_address)
    print("ཽ", end="")
    print("\tཽ"*4)
    return reply

  def process_response(self, request, client_address):
    ''' Determines the specific reponse '''
    response = "ؿӬ٣ՄӬ٣: %s:%d\n" % (self.ip, self.port)
    response += "Has recieved your request\n"
    response = self.helper.to_str(response)
    self.log.log_response(response, 
                         client_address[0], 
                         client_address[1]
                         )
    print("ཽ", end="")
    print("\tཽ"*4)
    response = self.helper.to_bytes(response)
    return response 

  def check_request(self, request):
    '''Determines the validity of the client's request'''
    return True




