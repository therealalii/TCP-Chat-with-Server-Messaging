import socket
import threading

SERVER_IP = input("Enter server IPv4 address: ").strip()
PORT = 5555
nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("You have been disconnected from the server.")
            client.close()
            break

def write():
    while True:
        try:
            message = f"{nickname}: {input('')}"
            client.send(message.encode('utf-8'))
        except:
            break

threading.Thread(target=receive).start()
threading.Thread(target=write).start()
