UDP Client-Server Socket Programming

Files:
- server.py : Run this first.
- client.py : Run this in a second terminal.

How to run:
1. Open Terminal 1:
   python server.py

2. Open Terminal 2:
   python client.py

3. Enter a message in the client.

Expected:
Client:
Enter message to send: Hello UDP Server
Server: Message received by UDP Server!

Server:
UDP Server started...
Waiting for client message...
Client [('127.0.0.1', <port>)]: Hello UDP Server
