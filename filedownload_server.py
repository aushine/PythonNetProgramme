import socket
def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.bind(("192.168.56.1", 7980))

    tcp_socket.listen(128)
    print("服务器开启,当前处于闲置....")
    client_socket, client_addr = tcp_socket.accept()
    print("新客户端地址:", client_addr[0], "端口:", client_addr[1], "已链接")
    file_name = client_socket.recv(1024)

    try:
        f = open(file_name, "rb")
        client_socket.send(f. read())
        print(str(file_name)+"文件已发送....")
        f. close()
    except Exception:
        print("没有找到请求的文件"+str(file_name)+"....")

    tcp_socket.close()
    client_socket.close()
if __name__ == "__main__":
    main()