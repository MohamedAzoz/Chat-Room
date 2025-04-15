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
        except:
            print(f"Error in Receiving the message " )
            sock.close()
            break


def Write():
    while True:
        try:
            msg = input("")
            if msg.lower() == "exit" or msg.lower() == "end":  
                sock.close()
                print("Disconnected from chat.")
                break

            sock.send(msg.encode())
        except:
            print(f"Error in sending message ")
            sock.close()
            break


def thread_Receive(Arg):
    thread = threading.Thread(target=Receive,args=(Arg,))  
    thread.start()


def thread_Write():
    thread = threading.Thread(target=Write)  
    thread.start()

