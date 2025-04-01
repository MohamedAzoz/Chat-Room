import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 13579
server_add = (host, port)

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

