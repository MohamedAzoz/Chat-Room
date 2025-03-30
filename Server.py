# import threading
# import socket

# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host=socket.gethostname()
# port=13579
# server_add=(host,port)
# sock.bind(server_add)
# sock.listen()
# Clients=[]
# nick_names=[]

# def Receive(client,nick):
#     while True:
#         try:
#             msg=client.recv(1024).decode()
#             SharingMessages(msg.encode())
#         except:
#             Clients.remove(client)
#             nick_names.remove(nick)
#             print("error in Receive Message")
#             SharingMessages(F'{nick} : Left the chat room')
#             break

# def SharingMessages(msg=''):
#     for conne in Clients:
#         try:
#             conne.send(msg.encode())
#         except:
#             Clients.remove(conne)

# def Messaging():
#     while True:
#         conn,add=sock.accept()
#         conn.send('NICK'.encode())
#         nick_name=conn.recv(1024).decode()
#         Clients.append(conn)
#         nick_names.append(nick_name)
#         SharingMessages(F"{nick_name} : join in chat room")
#         thread=threading.Thread(target=Receive,args=(conn,nick_name))
#         thread.start()
        

# Messaging()



import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  
port = 13579
server_add = (host, port)
sock.bind(server_add)
sock.listen()

Clients = []
nick_names = []

def handle_client(conn, nick_name):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                SharingMessages(msg)
        except:
            Clients.remove(conn)
            nick_names.remove(nick_name)
            print(f"Error: {nick_name} disconnected")
            SharingMessages(f"{nick_name} left the chat room")
            conn.close()
            break

def SharingMessages(msg):
    for client in Clients:
        try:
            client.send(msg.encode())
        except:
            Clients.remove(client)

def accept_clients():
    while True:
        conn, addr = sock.accept()
        print(f"New connection from {addr}")

        conn.send('NICK'.encode())
        nick_name = conn.recv(1024).decode()
        
        nick_names.append(nick_name)
        Clients.append(conn)
        
        print(f"Nickname of client is {nick_name}")
        SharingMessages(f"{nick_name} joined the chat room")

        thread = threading.Thread(target=handle_client, args=(conn, nick_name))
        thread.start()

print("Server is running...")
accept_clients()
