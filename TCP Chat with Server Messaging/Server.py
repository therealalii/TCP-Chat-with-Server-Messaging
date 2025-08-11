import socket
import threading

HOST = ''
PORT = 5555

nickname = input("Enter your server nickname: ")

def receive_messages(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print("\n" + msg)  # Already contains client's nickname
            else:
                break
        except:
            break

def send_messages(conn):
    while True:
        msg = input()
        if msg.lower() == 'exit':
            print("Shutting down server...")
            conn.close()
            break
        try:
            conn.send(f"{nickname}: {msg}".encode())
        except:
            break

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server listening on port {PORT}...")
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # دو thread برای ارسال و دریافت پیام‌ها
    receive_thread = threading.Thread(target=receive_messages, args=(conn,))
    send_thread = threading.Thread(target=send_messages, args=(conn,))

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()
    server.close()

if __name__ == "__main__":
    main()
