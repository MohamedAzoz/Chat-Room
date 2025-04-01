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

def Handle(conn,nick):
    while True:
        try:
            msg=conn.recv(1024).decode()
            if msg:
                Broadcast(msg) 
        except:
            Clients.remove(conn)
            nick_names.remove(nick)
            print(f"Error: {nick} disconnected")
            Broadcast(F'{nick} : Left the chat room')
            conn.close()
            break

def Broadcast(msg):
    for client in Clients:
        try:
            client.send(msg.encode())
        except:
            Clients.remove(client)


def Receive():
    while True:
        conn,add=sock.accept()
        print(f"New connection from {add}")

        conn.send('NICK'.encode())
        nick_name=conn.recv(1024).decode()

        Clients.append(conn)
        nick_names.append(nick_name)

        print(f"Nickname of client is {nick_name}")
        Broadcast(F"{nick_name} : join in chat room")

        thread=threading.Thread(target=Handle,args=(conn,nick_name))
        thread.start()


print("Server is running...")
Receive()
