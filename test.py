import socket
import threading
from sys import *
print(socket.gethostbyname(socket.gethostname()))

nm = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nm.bind(("", 7666))

def send_():
    while True:
        send_data = input("请输入想需要发送的信息:")
        if send_data == "exit()":
            break
        nm.sendto(send_data.encode("gbk"), ("192.168.137.1", 7655))

def recv_():
    while True:
        recv_data = nm.recvfrom(1024)
        print("\n收到来自地址:", recv_data[1][0], "端口号:", recv_data[1][1], "的信息:", recv_data[0].decode("gbk"))

def main():
    t1 = threading.Thread(target=send_)
    t2 = threading.Thread(target=recv_)
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()
    while True:
        if len(threading.enumerate()) == 1:
            nm.close()
            break