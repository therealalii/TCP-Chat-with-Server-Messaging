import socket
import threading

HOST = "0.0.0.0"  # Listen on all network interfaces
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the chat.\n".encode("utf-8"))
            nicknames.remove(nickname)
            break

def receive():
    print(f"Server is running on {HOST}:{PORT} ...")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!\n".encode("utf-8"))
        client.send("Connected to the server!\n".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
