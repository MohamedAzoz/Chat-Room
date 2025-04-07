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

# def Receive(nickname):
#     while True:
#         try:
#             msg = sock.recv(1024).decode()
#             if msg == 'NICK':
#                 sock.send(nickname.encode())
#             else:
#                 print(msg)
#         except Exception as e:
#             print(f"Error in Receiving the message : {e}" )
#             sock.close()
#             break


# def Write():
#     while True:
#         try:
#             msg = input("==> ")
#             if msg.lower() == "exit" or msg.lower() == "end":  
#                 sock.close()
#                 print("Disconnected from chat.")
#                 break
#             sock.send(msg.encode())
#         except Exception as e:
#             print(f"Error in sending message : {e}")
#             sock.close()
#             break

# thread_Receive = threading.Thread(target=Receive, daemon=True)  
# thread_Receive.start()

# thread_Write = threading.Thread(target=Write, daemon=True)
# thread_Write.start()

# thread_Write.join()

