import socket
def main():
    # 1. 创建tcp的套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:

        #2. 链接服务器
        tcp_socket.connect(("192.168.56.1", 8080))
        '''
        server_ip = input("请输入要链接的服务器ip:")
        server_port = input("请输入要链接的服务器端口：")
        server_addr = (server_ip, server_port)
        tcp_socket.connect(server_addr)
       '''

       #3. 发送或者接收数据
        send_data = input("\033 [0:31m 请输入要发送的信息:")
        tcp_socket.send(send_data.encode("gbk"))

if __name__ == "__main__":
    main()
