# server.py
import socket
import threading

clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        username = usernames[index]
        broadcast(f"{username} has left the chat.".encode(), client)
        usernames.remove(username)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            remove_client(client)
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen()

    print("Server started, waiting for connections...")

    while True:
        client, address = server_socket.accept()
        print(f"New connection from {address}")

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)

        print(f"Username of the new client: {username}")
        broadcast(f"{username} has joined the chat.".encode(), client)
        client.send("Connected to the chat!".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
