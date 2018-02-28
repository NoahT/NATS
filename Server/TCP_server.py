'''
Author: Taylor Cochran
Poject: NATS
Version: 0.4

Algorythm:
  1) Grab the ip & desired port
  2) Create socket object
  3) Bind ip/port
  4) run the server
  5) thread the server
    1) recive the message from the client
    2) do things with the recieved data
    3) send a reply
    4) Close the client socket
  6) start the client_handler
'''
import os
import socket
import subprocess
import sys
import threading 
import Transaction_wrapper



'''
##########################
####     SERVER       ####
##########################
'''
def setup(ip=socket.gethostbyname(socket.gethostname()),
          port=10135):
  '''
  Sets up the server on the localhost with the port.
  Sets up the socket for a restart if the server crashes
  '''
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((ip, port))
  print( "[*][*] Listening on %s:%d [*][*]" % (ip, port))
  return server


def run(server, restarts=0):
  '''
  Opens the server. Accepts the server connection. 
  Threads the client handler
  Runs the thread.
  '''
  while True:
    try:
      print("[*] Waiting for connection....", flush=True)
      client, addr = server.accept()
      print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
      #spin up our client thread to handle incoming data
      client_handler = threading.Thread(target=handle_client,
                                        args=(client, server_restarts))
      client_handler.start()
    except Exception as e:
      log(e)
      restarts = server_restarts(restarts)
      run(server, restarts)


def log(exception, 
  location="ServerMain_CrashLog.txt"):
  '''
  Logs the passed exception to a file
  '''
  location = "/Users/taylorcochran/Desktop/Server Data/Logs/" + location
  with open(location,
            "ab+") as file:
    file.write(to_bytes("\n============================\n"))
    file.write(to_bytes(str(type(exception)) + "\n"))
    file.write(to_bytes(str(exception.args) + "\n"))
    file.write(to_bytes(str(exception) + "\n"))
    file.write(to_bytes("============================"))
  print("[*] Exception %s logged." % str(type(exception)))



'''
##########################
####     CLIENT       ####
##########################
'''
def handle_client(client_socket, restarts):
  '''
  Recives the client request, processes the passed data, and replies.
  Finally it closes the client_socket
  '''
  try:
    request = to_str(client_socket.recv(1024))
    message = None
    command = ["python2",]
    # @@@@@@@ REPLACE WITH ACTUAL COMMANDS
    if (request == "I hope this works!"):
      client_socket.send(to_bytes("It does!"))
    elif (is_valid_request(request)):
      message = to_bytes(transaction(request))
      client_socket.send(message)
    else:
      client_socket.send(to_bytes("Idk what you're talking about!"))
    print("[*] Received: %s" % request)
    client_socket.close()
  except Exception as e:
    log(e)
    restarts = server_restarts(restarts)
  run(server, server_restarts)



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


def transaction(request):
  '''
  Calls the database and passes the desired command
  '''
  result = Transaction_wrapper.run(request)
  return result


def server_restarts(restarts=0):
  '''
  Attempts to reboot the server.
  Will do so 10 times before shutting down
  '''
  print(restarts)
  restarts += 1
  print("[*] Server has restarted %d times" % restarts) 
  if restarts >= 10:
    print("[*][*] Server has reached restart limit! [*][*]")
    print("[*][*] Exiting....[*][*]")
    sys.exit()
  return restarts

def is_valid_request(request):
  boo = False
  request = to_str(request)
  if (request == "get people"):
    boo = True
  return boo


'''
##########################
####      MAIN        ####
##########################
'''
if __name__ == '__main__':
  server = setup()
  server.listen(5)
  run(server)
  




