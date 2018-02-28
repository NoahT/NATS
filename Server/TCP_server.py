'''
Author: Taylor Cochran
Poject: NATS
Version: 0.1

Algorythm:
  1) Grab the bind_ip & desired port
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
import socket
import threading 


def setup():
  '''Sets up the server on the localhost with the port 3000'''
  bind_ip = socket.gethostbyname(socket.gethostname())
  bind_port = 3000
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((bind_ip, bind_port))
  print "[*] Listening on %s:%d" % (bind_ip, bind_port)
  return server


def handle_client(client_socket):
  '''Recives the client request, processes the past data, and replies.
  Finally it closed the client_socket
  '''
  request = client_socket.recv(1024)
  print"[*] Received: %s" % request
  client_socket.send("Message!")
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

      print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

      #spin up our client threat to handle incoming data
      client_handler = threading.Thread(target=handle_client,args=(client,))
      client_handler.start()

    except Exception as e:
      print type(e)
      print e.args
      print e


if __name__ == '__main__':
  server = setup()
  server.listen(5)
  run(server)


