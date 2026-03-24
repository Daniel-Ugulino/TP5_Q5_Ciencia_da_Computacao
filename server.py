import ssl
import socket

HOST = 'localhost'
PORT = 8443

contexto = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
contexto.load_cert_chain('cert.pem', 'chave.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    print(f"Conexao aberta: {HOST}:{PORT}...")

    with contexto.wrap_socket(sock, server_side=True) as tls:
        conn, addr = tls.accept()
        print(f" {addr} Conectado")

        with conn:
            dados = conn.recv(1024)
            print(f"{addr} Dados: {dados.decode()}")
            conn.sendall(b"Dados recebidos com seguranca")