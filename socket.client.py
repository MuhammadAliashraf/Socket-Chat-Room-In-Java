import socket
import threading


def receive_messages(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            print("Server disconnected.")
            break
        print(f"Server: {data.decode()}")


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


def start_client(host='192.168.0.246', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))

    recv_thread.start()
    send_thread.start()

    recv_thread.join()
    send_thread.join()

    client_socket.close()


if __name__ == "__main__":
    start_client()
