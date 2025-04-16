import threading
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=13579
server_add=(host,port)
sock.bind(server_add)
sock.listen()
Clients=[]
nick_names=[]

def Handle():
    while True:
        try:
            conn,add=sock.accept()
            print(f"New connection from {add}")

            conn.send('NICK'.encode())
            nick_name=conn.recv(1024).decode()

            Clients.append(conn)
            nick_names.append(nick_name)

            print(f"Nickname of client is {nick_name}")
            Broadcast(F"{nick_name} : join in chat room")

            thread=threading.Thread(target=Receive,args=(conn,nick_name))
            thread.start()
        except:
            print("Error in Receive data")


def Receive(client,nick_name):
    while True:
        try:
            message=client.recv(1024).decode()
            if message:
                print(f"{nick_name}: {message}")
                Broadcast(f"{nick_name}: {message}") 
        except:
            Clients.remove(client)
            nick_names.remove(nick_name)
            print(f"Error: {nick_names} disconnected ")
            Broadcast(F'{nick_names} : Left the chat room')
            client.close()
            break

def Broadcast(msg):
    for client in Clients:
        try:
            client.send(msg.encode())
        except:
            Clients.remove(client)



print("Server is running...")
Handle()
