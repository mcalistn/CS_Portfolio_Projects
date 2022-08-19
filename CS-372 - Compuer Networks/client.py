import socket

# Create socket and connect to 'server'
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("localhost", 52928))

# Ensure connection with server
res = clientSocket.recv(3)
clientSocket.send(res)

# Start conversation with server
print("\nType '/q' to quit")
print("Enter message to send...")
done = False
while True:
    # Send information to server
    message = input(">")
    if message == "/q":
        break
    message_length = str(len(message))
    clientSocket.send(message_length.encode())
    clientSocket.send(message.encode())

    # Wait on reply from server
    message_length = clientSocket.recv(4096).decode()
    if message_length == "":
        break
    message_length = int(message_length)
    client_message = clientSocket.recv(message_length).decode()
    print(client_message)

# Close connection
clientSocket.close()

# Citations -
# Laboratories, M. (n.d.). Making HTTP requests with sockets in Python. Internal Pointers.
#     Retrieved April 15, 2022, from https://www.internalpointers.com/post/making-http-
#     requests-sockets-python
# Bodnar, J. (n.d.). Python socket. Python Socket - Python network programming with sockets.
#     Retrieved April 15, 2022, from https://zetcode.com/python/socket/
# Real Python. (2022, February 21). Socket programming in python (guide). Real Python.
#     Retrieved April 15, 2022, from https://realpython.com/python-sockets/
