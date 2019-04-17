import socket
def main():
    # 1. 创建tcp监听套接字(socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server_socket:

        # 2. 绑定一个ip和端口(bind)
        tcp_server_socket.bind(("", 7888))

        # 3. 设置个客户端分配一个服务套接字(listen)
        tcp_server_socket.listen(128)
        
        print("==========1===========")
        # 4. 等待客户端的响应(accept)
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("==========2===========")

        print("客户端ip:",client_addr)

        # 接受到客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print(recv_data)
        
        #响应客户端给客户端发送数据包
        new_client_socket.send("心有猛虎,细嗅蔷薇.".encode("gbk"))
    new_client_socket.close()
if __name__ == "__main__":
    main()
