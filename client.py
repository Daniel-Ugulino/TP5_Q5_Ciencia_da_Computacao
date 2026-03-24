import ssl
import socket

HOST = 'localhost'
PORT = 8443

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
contexto.load_verify_locations('cert.pem')

with socket.create_connection((HOST, PORT)) as sock:
    with contexto.wrap_socket(sock, server_hostname=HOST) as tls:
        print(f"Conectado {tls.cipher()}")
        tls.sendall(b"Teste dados sensiveis")
        resposta = tls.recv(1024)
        print(f"Resposta: {resposta.decode()}")