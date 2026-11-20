import socket

HOST = "127.0.0.1"
PORT = 5000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"TCP Server listening on {HOST}:{PORT}")
        print("Waiting for a client to connect...")

        conn, address = server.accept()
        with conn:
            print(f"Connected by {address}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                message = data.decode("utf-8")
                print(f"Client: {message}")

                if message.strip().lower() == "exit":
                    print("Client requested to close the connection.")
                    break

                reply = f"Server received: {message}"
                conn.sendall(reply.encode("utf-8"))

        print("Connection closed.")

if __name__ == "__main__":
    start_server()
