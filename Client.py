import socket
import threading

HOST = input("Enter server IP address: ")
PORT = 5555
nickname = input("Enter your nickname: ")

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print("\n" + msg)  # Already contains nickname
            else:
                break
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    print("Connected to chat. Type messages and press Enter to send. Type 'exit' to quit.")

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        try:
            client.send(f"{nickname}: {message}".encode())
        except:
            break

    client.close()

if __name__ == "__main__":
    main()
