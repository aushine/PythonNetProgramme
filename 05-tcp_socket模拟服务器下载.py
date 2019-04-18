import socket
def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("go to hell")   
    tcp_socket.connect(("192.168.56.1", 7980))

    file_name = input("请输入想从服务端中下载的文件名:")
   
    tcp_socket.send(file_name.encode("gbk"))
    file_content = tcp_socket.recv(1024*1024)
    with open("[新]"+file_name,"wb") as f:
        f.write(file_content)

    tcp_socket.close()

if __name__ == "__main__":
    main()
