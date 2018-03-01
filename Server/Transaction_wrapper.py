'''
Author: Taylor Cochran
Poject: NATS
Version: 0.1

Algorythm:
1) Get called by the server
2) Log the time of the transaction
3) Process the transaction
4) Log the process
5) Return the processed results
'''

import datetime
import sys
import subprocess

'''
##########################
####   TRANSACTION  ######
##########################
'''
def run(request):
  '''
  Runs the transaction request.
  '''
  time_stamp = datetime.datetime.now()
  log(time_stamp)
  transaction_message = transaction(request)
  # log(transaction_message, 1)
  return transaction_message


def log(message, stage=0):
  '''
  Logs the passed message in the 'transaction_log'.
  If this is the first log of the session then it simply logs the datetime.
  If this is the second log then the transaction is considered finished 
  and all transaction data is logged.
  If stage '2' is passed then the message is logged as an error
  '''
  location = "/Users/taylorcochran/Desktop/Server Data/Logs/"
  if stage == 0:
    location += "Transaction_Log.txt"
    with open(location, "ab+") as file:
      message = to_bytes(message)
      file.write(to_bytes("\n============================\n"))
      file.write(to_bytes(("Date time %s\n" % message)))
  elif stage == 1:
    location += "Transaction_Log.txt"
    with open(location, "ab+") as file:
      file.write(to_bytes("TRANSACTION: %s" % message))
      file.write(to_bytes("\n============================\n"))
  elif stage == 2:
    location += "Transaction_Crashlog.txt"
    with open(location, "ab+") as file:
      file.write(to_bytes("\n============================\n"))
      file.write(to_bytes(str(type(message)) + "\n"))
      file.write(to_bytes(str(message.args) + "\n"))
      file.write(to_bytes(str(message) + "\n"))
      file.write(to_bytes("\n============================\n"))
  else:
    print("You should never see this message!")
    sys.exit()


def transaction(request):
  '''
  Attempts to process the passed request.
  In the event that the request is not recognized, then the system returns a Nonetype
  object.
  Logs any crashes that occur
  '''
  print("[*][*] Processing request: %s [*][*]" % request)
  command = ["perl"]
  file = "/Users/taylorcochran/Desktop/Server Data/DATA/"
  data = ""
  try:
    if request == "get people":
      log(request, 1)
      file += "simpleDB.pl"
      command.append(file)
      command.append("l")
      print("[*][*] Running command: %s %s %s" % (command[0], command[1], command[2]))
      subprocess.run(command)
      # add to the perl script flags for grabbing stored data
    else:
      data = "Request not matched"
  except Exception as e:
    log(e, 2) # log error
    data = ("Exception thrown %s" % e)
  return to_str(data)



'''
##########################
####HELPER FUNCTIONS######
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



