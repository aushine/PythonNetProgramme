import socket
print("本机IP地址：",socket.gethostbyname(socket.gethostname()))
def main():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as tcp_socket:
      tcp_socket.bind(("", 7902))
      while True:
         tcp_socket.listen(128)
         print("正在等待客户端的链接.....")
         
         client_socket, client_addr = tcp_socket.accept()
         print(f"新客户端ip:{client_addr[0]} port:{client_addr[1]}已连接")
         while True:
            recv_data = client_socket.recv(1024)
            if recv_data:
               print("客户端信息:", recv_data.decode("gbk"))
               client_socket.send("go back fuck yourself".encode("utf-8"))
            else:
               client_socket.close()
               break
         
if __name__ == "__main__":
   main()
