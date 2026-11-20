import socket

HOST = "127.0.0.1"
PORT = 5000

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print(f"Connected to TCP Server at {HOST}:{PORT}")
            print("Type a message and press Enter. Type 'exit' to quit.")

            while True:
                message = input("You: ")
                client.sendall(message.encode("utf-8"))

                if message.strip().lower() == "exit":
                    break

                response = client.recv(1024)
                if not response:
                    print("Server closed the connection.")
                    break

                print(response.decode("utf-8"))

        except ConnectionRefusedError:
            print("Could not connect. Start server.py first, then run client.py.")
        except OSError as error:
            print(f"Network error: {error}")

if __name__ == "__main__":
    start_client()
