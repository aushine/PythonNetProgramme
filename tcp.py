import socket
from sys import stdout
from time import sleep
print("本机ip地址:",socket.gethostbyname(socket.gethostname()))
def out(Any):
    return stdout.write(Any)

def tcp_sendtest():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.connect(("192.168.56.1", 7980))
        send_data = input("\033[31m 请输入须要发送的数据:")
        tcp_socket.send(send_data.encode("gbk"))

def sockettcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
        tcp_socket.bind(("", 7895))
        tcp_socket.listen(128)
        client_socket, client_addr = tcp_socket.accept()
        print(client_addr)
        recv_data = client_socket.recv(1024)
        print(f"\033[31m{recv_data.decode('gbk')}")
        client_socket.send("雷猴啊".encode("gbk"))
    client_socket.close()
if __name__ == "__main__":
    sockettcp()