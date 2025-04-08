from Module_Client import *

nickname = input("Enter Your Nickname: ")


connection()


thread_Receive(Receive,nickname)
thread_Write(Write)





