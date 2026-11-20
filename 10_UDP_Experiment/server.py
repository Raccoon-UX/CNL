import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to localhost and port
server_address = ("127.0.0.1", 5000)
server_socket.bind(server_address)

print("UDP Server started...")
print("Waiting for client message...")

while True:
    # Receive message from client
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()

    print(f"Client [{client_address}]: {message}")

    # Send response to client
    response = "Message received by UDP Server!"
    server_socket.sendto(response.encode(), client_address)
