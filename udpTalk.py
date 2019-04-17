import socket


def main():
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind(("", 8988))
        # 获取对方的ip与端口
        dest_ip = input("输入对方的ip:")
        dest_port = int(input("输入对方的端口:"))

        # 键入须要发送的数据
        while True:
            send_data = input("输入需要发送的数据:")
            if send_data == "exit":
                break
            udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

            #接收回送的数据
            recv_data = udp_socket.recvfrom(1024)
            print(recv_data[0].decode("gbk"), "来自地址:", recv_data[1])
            '''
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        dest_ip = "127.0.0.1"
        dest_port = 7980
        udp_socket.bind(("", 6799))
        while True:
            send_data = input("\33[31m 输入想要发送的信息:")
            udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))
            recv_data = udp_socket.recvfrom(1024)
            print(f"\33[0m 来自地址:{recv_data[1]} 内容:{recv_data[0].decode('gbk')}")

def sendto():
    pass


if __name__ == "__main__":
    main()