# Python Group Chat Application

A simple Python-based group chat application using socket programming. This application allows multiple clients to connect to a server and chat together in real-time with usernames displayed.

## Features

- **Real-time Messaging**: Clients can send and receive messages in real-time.
- **Username Support**: Each client has a unique username displayed with each message.
- **Broadcasting**: Messages from one client are broadcast to all other connected clients.
- **Multiple Client Connections**: Supports multiple clients chatting simultaneously.

## Requirements

- **Python 3.x**: This application requires Python 3 or higher.

No additional libraries are needed beyond Python's standard library.

## Files

1. **server.py** - The server script that handles connections and broadcasts messages.
2. **client.py** - The client script that allows each user to connect to the server and chat with others.

## Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/group-chat-app.git
cd group-chat-app
