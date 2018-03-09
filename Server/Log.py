#!/usr/local/bin/python3
''' A simple Data/Crash Logger'''

import Helper

__author__ = "Taylor Cochran"
__version__ = "1.0"
__maintainer__ = "Taylor Cochran"
__email__ = "taylorjcochran@hotmail.com"
__status__ = "Prototype"


class Log(object):
  def __init__(self):
    self.exception_file = None
    self.data_file = None
    self.helper = Helper.Helper()

  def log_exception(self, data):
    '''
    Composes an exception message and writes it to a file
    '''
    date = self.Helper.get_date()
    start = "\n==========\n"
    start += str(type(data)) + date
    start += "\n==========\n"
    message = start + str(data.args) + "\n" + str(data) + "\n"
    message = self.helper.to_bytes(message)

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

    date = self.helper.get_date()
    start = "\n==========\n"
    start += "Request Received @ " + date
    start += "\n==========\n"
    message = start + "IP: " + ip + "\nPort: " 
    message += str(port) + "\nRequest" + data
    message = self.helper.to_bytes(message)

    with open(self.data_file, 'ab+') as file:
      file.write(message)

  def log_response(self, data, ip="0.0.0.0", port=80):
    '''
    Composes a return message and writes it to a file
    '''
    print("༺༺༺༺༺    Logged Response   ༻༻༻༻༻") 
    print(data)

    date = self.helper.get_date()
    start = "\n==========\n"
    start += "Response Sent @ " + date
    start += "\n==========\n"
    message = start + "IP: " + ip + "\nPort: " 
    message += str(port) + "\nReturn " + data
    message = self.helper.to_bytes(message)

    with open(self.data_file, 'ab+') as file:
      file.write(message)


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




