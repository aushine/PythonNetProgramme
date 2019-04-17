import socket
print('当前主机名称为 : ' + socket.gethostname())
print("当前主机的Ip地址",socket.gethostbyname(socket.gethostname()))
def socket_recvfrom():
    #创建套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        localaddr=('', 7878)  # 必须绑定一个本地的ip和端口
        s.bind(localaddr)
        while True:
            recv_data = s.recvfrom(1024)
            if recv_data[0].decode("gbk") == "exit":
                break
            print(f"接收的消息:{recv_data[0].decode('gbk')} 来自地址:{recv_data[1]}")
def socket_sendto():
    # 创建套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        localaddr = ('', 7788)  # 必须绑定一个本地的ip和端口
        s.bind(localaddr)
        while True:
            # 接收一个输入数据
            send_data = input("输入需要发送的数据键入exit退出:")
            if send_data == "exit":
                break
            # s.sendto(b"Hello World!!!", ("192.168.81.1", 8080))
            # 给指定ip的指定端口发送数据
            s.sendto(send_data.encode("GBK"), ("192.168.56.1", 8080))
if __name__ == "__main__":
    # socket_recvfrom()
    socket_sendto()