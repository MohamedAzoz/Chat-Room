import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 13579
server_add = (host, port)

def connection():
    try:
        sock.connect(server_add)
    except:
        print("Unable to connect to the server.")
        exit()

def Receive(nickname):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg == 'NICK':
                sock.send(nickname.encode())
            else:
                print(msg)
        except Exception as e:
            print(f"Error in Receiving the message : {e}" )
            sock.close()
            break


def Write():
    while True:
        try:
            msg = input("==> ")
            if msg.lower() == "exit" or msg.lower() == "end":  
                sock.close()
                print("Disconnected from chat.")
                break
            sock.send(msg.encode())
        except Exception as e:
            print(f"Error in sending message : {e}")
            sock.close()
            break


def thread_Receive(Function_Name,Args):
    thread = threading.Thread(target=Function_Name, daemon=True,args=(Args,))  
    thread.start()


def thread_Write(Function_Name):
    thread = threading.Thread(target=Function_Name, daemon=True)  
    thread.start()
    thread.join()

