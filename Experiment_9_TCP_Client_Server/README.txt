EXPERIMENT 9
Connection-Oriented Client-Server Socket Programming Using TCP/IP

OBJECTIVE
To implement communication between a TCP client and TCP server using socket
programming.

REQUIREMENTS
- Python 3
- VS Code (or any code editor)
- Two terminal windows

FILES
- server.py : Creates a TCP server, listens for a client, receives messages,
              and sends an acknowledgement.
- client.py : Connects to the server, sends messages, and displays replies.

HOW TO RUN IN VS CODE (WINDOWS)

1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Check Python installation:
       python --version
   If that command is not recognized, try:
       py --version

5. TERMINAL 1 - Start the server:
       python server.py
   Or:
       py server.py

   Keep this terminal running. It should show that the server is listening
   on 127.0.0.1:5000.

6. TERMINAL 2 - Start the client:
   Open a second terminal in the same folder and run:
       python client.py
   Or:
       py client.py

7. Type a message in the client terminal and press Enter. The server will
   display the message and send an acknowledgement back to the client.

8. To end the session, type:
       exit

IMPORTANT
- Start server.py before client.py.
- Both programs use 127.0.0.1 (localhost), so they run on the same computer.
- The server and client communicate using TCP (SOCK_STREAM), which is
  connection-oriented and provides reliable, ordered data delivery.
- The port used is 5000. If it is already occupied, change PORT in BOTH
  server.py and client.py to the same unused port.

EXPECTED OUTPUT (EXAMPLE)

Server terminal:
    TCP Server listening on 127.0.0.1:5000
    Waiting for a client to connect...
    Connected by ('127.0.0.1', <client-port>)
    Client: Hello
    Connection closed.

Client terminal:
    Connected to TCP Server at 127.0.0.1:5000
    Type a message and press Enter. Type 'exit' to quit.
    You: Hello
    Server received: Hello

CONCEPTS USED
- AF_INET : IPv4 address family
- SOCK_STREAM : TCP socket type
- bind() : Assigns an IP address and port to the server socket
- listen() : Waits for incoming client connections
- accept() : Accepts a client connection
- connect() : Connects the client to the server
- sendall() : Sends data through the socket
- recv() : Receives data from the socket

NOTE
This is a basic single-client demonstration for the Network Lab experiment.
