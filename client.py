# client.py
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "USERNAME":
                client_socket.send(username.encode())
            else:
                print(message)
        except:
            print("An error occurred! Disconnected from the server.")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(f"{username}: {message}".encode())
        if message.lower() == "bye":
            client_socket.close()
            break

server_ip = '127.0.0.1'
server_port = 5555
username = input("Enter your username: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client_socket,))
send_thread.start()
