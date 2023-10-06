import socket

host = '0.0.0.0'
port = 4000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1024).decode('utf-8')

    if 'GET /sum' in request:
        a = int(request.split('a=')[1].split('&')[0])
        b = int(request.split('b=')[1].split(' ')[0])
        result = a + b
        response = f'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{a} + {b} = {result}'
        client_socket.sendall(response.encode('utf-8'))
    if 'GET /sub' in request:
        a = int(request.split('a=')[1].split('&')[0])
        b = int(request.split('b=')[1].split(' ')[0])
        result = a - b
        response = f'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{a} - {b} = {result}'
        client_socket.sendall(response.encode('utf-8'))
    if 'GET /div' in request:
        a = int(request.split('a=')[1].split('&')[0])
        b = int(request.split('b=')[1].split(' ')[0])
        result = a / b
        response = f'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{a} / {b} = {result}'
        client_socket.sendall(response.encode('utf-8'))
    if 'GET /mult' in request:
        a = int(request.split('a=')[1].split('&')[0])
        b = int(request.split('b=')[1].split(' ')[0])
        result = a * b
        response = f'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n{a} * {b} = {result}'
        client_socket.sendall(response.encode('utf-8'))
client_socket.close()
