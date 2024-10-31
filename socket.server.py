import socket
import threading


def receive_messages(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            print("Client disconnected.")
            break
        print(f"Client: {data.decode()}")


def send_messages(client_socket):
    while True:
        # Get user input and send it to the client
        message_to_client = input("You: ")
        if message_to_client.lower() == "quit":  # Exit condition
            client_socket.sendall("Server has disconnected.".encode())
            print("Closing connection.")
            client_socket.close()
            break
        client_socket.sendall(message_to_client.encode())


def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()
    print(f"Server listening on {host}:{port}")

    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    # Start threads for receiving and sending messages
    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    recv_thread.start()
    send_thread.start()

    # Wait for both threads to finish
    recv_thread.join()
    send_thread.join()

    # Close the server socket after threads complete
    server_socket.close()


if __name__ == "__main__":
    start_server()
