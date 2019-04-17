import  socket
def main():
    # 1.创建tcp的套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        server_ip = input("请输入要连接的服务器的Ip:")
        server_port = int(input("请输入要连接服务器的端口:"))
        server_addr = (server_ip, server_port)
        tcp_socket.connect(server_addr)
        send_data = input("请输入要发送的信息:")
        # 2. 连接服务器

        # 3. 发送/接收数据

        # 4. 关闭套接字(with打开自动关闭)
if __name__ == "__main__":
    main()