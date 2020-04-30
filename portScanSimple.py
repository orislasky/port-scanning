import socket
s = socket.socket()
 
result = s.connect_ex(('google.com', 8080))
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')