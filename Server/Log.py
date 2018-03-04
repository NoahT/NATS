#!/usr/local/bin/python3
''' A simple Data/Crash Logger'''

import datetime

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class Log:
  def __init__(self):
    self.date = str(datetime.datetime.now())
    self.exception_file = None
    self.data_file = None

  def log_exception(self, data):
    '''
    Composes an exception message and writes it to a file
    '''
    self.get_date()
    start = "\n==========\n"
    start += str(type(data)) + self.date
    start += "\n==========\n"
    message = start + str(data.args) + "\n" + str(data) + "\n"
    message = self.to_bytes(message)

    try:
      with open(self.exception_file, 'ab+') as file:
        file.write(message)
    except IOError as e:
      raise e
    else:
      print("٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤")
      print("༺༺༺༺༺    LOGGED ERROR      ༻༻༻༻༻")
      print("٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤٤")

  def log_request(self, data, ip="0.0.0.0", port=80):
    '''
    Composes a request message and writes it to a file
    '''
    print("༺༺༺༺༺    Logged Request    ༻༻༻༻༻") 
    print(data)

    self.get_date()
    start = "\n==========\n"
    start += "Request Received @ " + self.date
    start += "\n==========\n"
    message = start + "IP: " + ip + "\nPort: " 
    message += str(port) + "\nRequest" + data
    message = self.to_bytes(message)

    with open(self.data_file, 'ab+') as file:
      file.write(message)

  def log_response(self, data, ip="0.0.0.0", port=80):
    '''
    Composes a return message and writes it to a file
    '''
    print("༺༺༺༺༺    Logged Response   ༻༻༻༻༻") 
    print(data)

    self.get_date()
    start = "\n==========\n"
    start += "Response Sent @ " + self.date
    start += "\n==========\n"
    message = start + "IP: " + ip + "\nPort: " 
    message += str(port) + "\nReturn " + data
    message = self.to_bytes(message)

    with open(self.data_file, 'ab+') as file:
      file.write(message)

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

  def get_date(self):
    ''' Grabs the current date/time stamp'''
    self.date = str(datetime.datetime.now())

if __name__ == '__main__':
  log = Log()
  # test the exception logger
  try:
    1/0
  except Exception as e:
    log.exception_file = "/Users/taylorcochran/Desktop/Server Data/"
    log.exception_file += "Logs/ExceptionTestLog.txt"
    log.log_exception(e)
  # test the data logger
  data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
  log.data_file = "/Users/taylorcochran/Desktop/Server Data/"
  log.data_file += "Logs/DataTestLog.txt"
  log.log_request(data)




