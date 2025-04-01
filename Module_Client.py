import threading
import socket

# nickname=''

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 13579
server_add = (host, port)

# try:
#     sock.connect(server_add)
# except:
#     print("Unable to connect to the server.")
#     exit()

def Receive(nickname):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg == 'NICK':
                sock.send(nickname.encode())
            else:
                print(msg)
        except:
            print("Connection lost. Exiting...")
            sock.close()
            break

def Write(nickname):
    while True:
        try:
            msg = input("")
            if msg.lower() == "exit":  
                sock.close()
                print("Disconnected from chat.")
                break
            msg =  nickname+" : "+msg
            sock.send(msg.encode())
        except:
            print("Error in sending message.")
            sock.close()
            break

def thread_Receive(Function_Name,Args):
    thread = threading.Thread(target=Function_Name, daemon=True,args=(Args,))  
    thread.start()
    
def thread_Write(Function_Name,Args):
    thread = threading.Thread(target=Function_Name, daemon=True,args=(Args,))  
    thread.start()
    thread.join()




# thread_Write = threading.Thread(target=Write, daemon=True)
# thread_Write.start()

# thread_Write.join()
