from threading import Thread
from vidstream import StreamingServer
from vidstream import ScreenShareClient
from vidstream import CameraClient
from tkinter import *
import socket
import threading

root = Tk()
root.geometry("1680x680")



label = Label(root, text="Ip to connect: ")
label.pack()

e2 = Entry()
e2.pack()

# connect
def connect():
    ip_to_listen = socket.gethostname()
    server = StreamingServer(ip_to_listen, 9999)
    server.start_server()


button = Button(text="connect",command=connect)
button.pack()


# Share Screen
def screen():
    ip_to_connect = e2.get()
    client1 = ScreenShareClient(ip_to_connect, 9999)
    client1.start_stream()

# Camera Chat
def camera():
    ip_to_connect = e2.get()
    client1 = CameraClient(ip_to_connect, 9999)
    client1.start_stream()


label = Label(root, text="\n")
label.pack()

button = Button(text="Start share screen",command=screen)
button.pack()

label = Label(root, text="\n")
label.pack()

button = Button(text="Start camera",command=camera)
button.pack()


label = Label(root, text="\n")
label.pack()

# Chat
def chat():

    nicknames = []
    nicknames_recv = []

    nickname = input("Enter your nickname: ")
    nicknames.append(nickname)


    ip_to_conn = e2.get()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_to_conn, 1111))

    nickname_recv = s.recv(1024).decode()
    nicknames_recv.append(nickname_recv)

    s.send(nickname.encode())

    print(f"Chatting with {nickname_recv}")

    while True:
        msg_recv = s.recv(1024).decode()
        print(f"Received from {nickname_recv}, Message: {msg_recv}")
        msg = input("Enter your message: ")
        s.send(msg.encode())

def handle_conn():
    t = threading.Thread(target=chat)
    t.start()
    

button = Button(text="Chat", command=handle_conn)
button.pack()



root.mainloop()