import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)

message = input("Enter message to send: ")

# Send message to server
client_socket.sendto(message.encode(), server_address)

# Receive response from server
data, server_address = client_socket.recvfrom(1024)

print("Server:", data.decode())

client_socket.close()
