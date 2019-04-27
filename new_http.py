import socket
import time

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as tcp_http:
        tcp_http.bind(("", 6788))
        tcp_http.listen(128)

        while True:
            print("服务端处于闲置状态,正在等待新用户的链接")
            client_socket, client_addr = tcp_http.accept()
            print(f"\r新客服端:ip{client_addr[0]} port:{client_addr[1]}已连接...", end="")
            client_socket.send("HTTP/1.1 200 OK\r\n\r\n<h1>HelloWorld</h1>".encode("gbk"))
            # client_socket.close()
if __name__ == "__main__":
    main()