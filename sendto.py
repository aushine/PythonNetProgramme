import socket
print(socket.gethostbyname(socket.gethostname()))
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.bind(("", 7895))

        tcp_socket.listen(128)

        client_socket, client_addr = tcp_socket.accept()

        recv_data = client_socket.recv(1024)
        print(recv_data.decode("gbk"))
        client_socket.close()
if __name__ == "__main__":
    main()