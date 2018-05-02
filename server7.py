import socket
import datetime, time
# import thread module
from _thread import *
import threading
from decimal import Decimal
 
print_lock = threading.Lock()
 
# thread fuction
def threaded(c):
    cont =0
    while (cont < 100):
        
        data = data_to_sent()
 
        # send back reversed string to client
        c.send(data.encode())
        cont = cont +1 
    # connection closed
    c.close()
 
def data_to_sent():
    
    return ("Hi\n")
def Main():
    host = ""
 
   
    port = 4444
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        
        c, addr = s.accept()
 
      
        print('Connected to :', addr[0], ':', addr[1])
 
        
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()
