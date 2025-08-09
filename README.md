# TCP-Chat-with-Server-Messaging
This project is a simple TCP chat application in Python where both the server and the client can send and receive messages in real-time.
## Features
- Two-way communication between server and client
- Works over localhost or LAN
- Easy to extend to multiple users

## How to Run

1. **Run the server:**

   - Open a terminal or command prompt.
   - Navigate to the folder containing `server.py`.
   - Run the command:
     ```bash
     python server.py
     ```
   - The server will start listening on port `5555`.
   - Once a client connects, you can type messages directly into the terminal and send them.

2. **Run the client:**

   - Open another terminal or command prompt.
   - Navigate to the folder containing `client.py`.
   - Run the command:
     ```bash
     python client.py
     ```
   - When prompted, enter the server's IP address:
     - Use `127.0.0.1` if running on the same computer.
     - Use the server machine's local IP if running on different computers in the same network.
   - After connecting, type messages and press Enter to send.

3. **Chat and Exit:**

   - Messages from the other side will appear prefixed with `Server:` or `Client:` accordingly.
   - To quit, type `exit` in either the server or client terminal.

---

**Note:**  
Make sure firewall settings allow communication on port `5555`.  
Both server and client must be on the same network or have network access to each other.

