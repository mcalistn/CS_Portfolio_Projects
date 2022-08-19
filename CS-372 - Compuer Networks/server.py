import socket

# Host name and port number
localHost = "localhost"
port = 52928

# Set-up socket to listen for client application on 'localhost:port'
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((localHost, port))
serverSocket.listen()
print("\r\nServer is listening at '" + localHost + "' on port number '" + str(port) + "'...")

# Accept and create a new socket for conversation with client application
acceptedSocket, clientAddress = serverSocket.accept()
print("\r\nConnected to client at '" + clientAddress[0] + "' on port number '" + str(clientAddress[1]) + "'...")

print("\nType '/q' to quit")
# Establish connection with client application
acceptedSocket.send(str.encode("SYN"))
if acceptedSocket.recv(3).decode() != "SYN":
    acceptedSocket.close()

# Start conversation with server
print("Waiting for message from client")
print("After the client's message is received, enter a message to respond!")
print("Type /q to quit")
while True:
    # Wait for client response
    message_length = acceptedSocket.recv(4096).decode()
    if message_length == "":
        break
    message_length = int(message_length)
    client_message = acceptedSocket.recv(message_length).decode()
    print(client_message)

    # Send information to client application
    message = input(">")
    if message == "/q":
        break
    message_length = str(len(message))
    acceptedSocket.send(message_length.encode())
    acceptedSocket.send(message.encode())

# Close connections
acceptedSocket.close()
serverSocket.close()

# Citations -
# Laboratories, M. (n.d.). Making HTTP requests with sockets in Python. Internal Pointers.
#     Retrieved April 15, 2022, from https://www.internalpointers.com/post/making-http-
#     requests-sockets-python
# Bodnar, J. (n.d.). Python socket. Python Socket - Python network programming with sockets.
#     Retrieved April 15, 2022, from https://zetcode.com/python/socket/
# Real Python. (2022, February 21). Socket programming in python (guide). Real Python.
#     Retrieved April 15, 2022, from https://realpython.com/python-sockets/
