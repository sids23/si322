from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    
    filename = sentence.split()[1][1:]  # Remove leading /
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        content_type = "image/jpeg"
        binary = True
    elif filename.endswith(".png"):
        content_type = "image/png"
        binary = True
    elif filename.endswith(".gif"):
        content_type = "image/gif"
        binary = True
    elif filename.endswith(".html"):
        content_type = "text/html"
        binary = False
    else:
        content_type = "text/plain"
        binary = False

    try:
        if binary:
            # Images must be opened in binary mode
            with open(filename, "rb") as f:
                body = f.read()
        else:
            # Text/HTML files can be opened normally
            with open(filename, "r") as f:
                body = f.read().encode()

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Connection: close\r\n"
            f"Content-Type: {content_type}\r\n"
            "\r\n"
        )

        connectionSocket.send(response.encode() + body)

    except FileNotFoundError:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Connection: close\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><body><h1>404 Not Found</h1></body></html>"
        )

        connectionSocket.send(response.encode())

    connectionSocket.close()

#     response = "HTTP/1.1 200 OK\r\nConnection:close\r\nContent-Type: text/html\r\n\r\n"
#     # connectionSocket.send(response.encode())
#     # connectionSocket.close()
#     print("connected")


#     filename = sentence.split()[1]
#     f = open(filename[1:])
#     body = f.read()
#     connectionSocket.send(response.encode() + body.encode())
#     connectionSocket.close()


# # Parse the filename from the HTTP request.
# # Use Python to read the file and convert it to a string.
# # Create a response string like you did in the previous step. Except, instead of using hardcoded HTML use the file contents.




