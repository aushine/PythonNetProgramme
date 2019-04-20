import socket
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        server_addr = ("192.168.229.128", 7903)
        tcp_socket.connect(server_addr)
        send_data = input("请输入需要发送的信息:")
        tcp_socket.send(send_data.encode("gbk"))


if __name__ == "__main__":
    main()
