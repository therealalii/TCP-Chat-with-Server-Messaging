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
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        try:
            msg_text = input("")
            message = f"{nickname}: {msg_text}"
            client.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Send error: {e}")
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
