from vidstream import StreamingServer
from vidstream import ScreenShareClient
from vidstream import CameraClient
from tkinter import *
import socket
import threading

root = Tk()
root.geometry("1680x680")



label = Label(root, text="Ip to listen: ")
label.pack()

e2 = Entry()
e2.pack()

# Listen
def listen():

    ip_to_listen = socket.gethostname()
    server = StreamingServer(ip_to_listen, 5555)
    server.start_server()


button = Button(text="listen",command=listen)
button.pack()


# Share Screen
def screen():
    ip_to_connect = e2.get()
    client1 = ScreenShareClient(ip_to_connect, 5555)
    client1.start_stream()

# Camera 
def camera():
    ip_to_connect = e2.get()
    client1 = CameraClient(ip_to_connect, 5555)
    client1.start_stream()

# Chat
def chat():

    clients = []
    nicknames = []
    nicknames_recv = []

    nickname = input("Enter your nickname: ")
    nicknames.append(nickname)


    ip_to_conn = e2.get()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip_to_conn, 1111))
    s.listen()
    print("Waiting for the other client to connect to the chat")
    conn, addr = s.accept()

    clients.append(addr)

    conn.send(nickname.encode())

    nickname_recv = conn.recv(1024).decode()
    nicknames_recv.append(nickname_recv)

    print(f"Connected with {addr}, his/her nickname {nickname_recv}")

    while True:
        msg = input("Your message: ")
        conn.send(msg.encode())
        msg_recv = conn.recv(1024).decode()

        print(f"Received from {nickname_recv}, Message: {msg_recv}")

def handle_conn():
    t = threading.Thread(target=chat)
    t.start()

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

button = Button(text="Chat",command=handle_conn)
button.pack()




root.mainloop()