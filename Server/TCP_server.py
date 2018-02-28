'''
Author: Taylor Cochran
Poject: NATS
Version: 0.1

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


def setup(ip=socket.gethostbyname(socket.gethostname()),
          port=10135):
  '''
  Sets up the server on the localhost with the port.
  Sets up the socket for a restart if the server crashes
  '''
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((ip, port))
  print( "[*] Listening on %s:%d" % (ip, port))
  return server


def handle_client(client_socket):
  '''
  Recives the client request, processes the passed data, and replies.
  Finally it closes the client_socket
  '''
  request = to_str(client_socket.recv(1024))
  message = None
  command = ["python2",]

  # @@@@@@@ REPLACE WITH ACTUAL COMMANDS
  if (request == "I hope this works!"):
    client_socket.send(to_bytes("It does!"))
  elif (request == "Hello Server!"):
    command.append("HelloWorld.py")
    print( "[*] Executing the following command: %s %s" % (command[0], command[1]))
    # message = to_bytes(database(command))
    message = to_bytes("Lol wut")
    client_socket.send(message)
  else:
    client_socket.send(to_bytes("Idk what you're talking about!"))

  print("[*] Received: %s" % request)
  client_socket.close()


def run(server):
  '''
  Opens the server. Accepts the server connection. 
  Threads the client handler
  Runs the thread.
  '''
  while True:
    try:
      client, addr = server.accept()
      print( "[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
      #spin up our client thread to handle incoming data
      client_handler = threading.Thread(target=handle_client,args=(client,))
      client_handler.start()
      # print( 1/0)
    except Exception as e:
      with open("/Users/taylorcochran/Documents/crash_log.txt", "a") as file:
        file.write("\n============================\n")
        file.write(str(type(e)) + "\n")
        file.write(str(e.args) + "\n")
        file.write(str(e) + "\n")
        file.write("============================")
      print( "[*] Exception %s logged." % str(type(e)))
      print( "[*] Attemping to recover...")
      break
  run(server)


def database(command):
  '''
  Calls the database and passes the desired command
  '''
  result = subprocess.check_output(command)
  return result


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


if __name__ == '__main__':
  server = setup()
  server.listen(5)
  run(server)
  




