from Module_Client import *

nickname = input("Enter Your Nickname: ")

connection()



thread_Receive(Receive,nickname)
thread_Write(Write)


# import threading
# import socket

# nickname = input("Enter Your Nickname: ")

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 13579
# server_add = (host, port)

# try:
#     sock.connect(server_add)
# except:
#     print("Unable to connect to the server.")
#     exit()

# def Receive():
#     while True:
#         try:
#             msg = sock.recv(1024).decode()
#             if msg == 'NICK':
#                 sock.send(nickname.encode())
#             else:
#                 print(msg)
#         except:
#             print("Connection lost. Exiting...")
#             sock.close()
#             break

# def Write():
#     while True:
#         try:
#             msg = input("")
#             if msg.lower() == "exit":  
#                 sock.close()
#                 print("Disconnected from chat.")
#                 break
#             msg = nickname+" : "+msg
#             sock.send(msg.encode())
#         except:
#             print("Error in sending message.")
#             sock.close()
#             break

# thread_Receive = threading.Thread(target=Receive, daemon=True)  
# thread_Receive.start()

# thread_Write = threading.Thread(target=Write, daemon=True)
# thread_Write.start()

# thread_Write.join()

