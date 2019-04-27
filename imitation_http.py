#coding=utf-8
import re
import socket
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
"""模拟一个浏览器访问服务器获取服务器上的html内容,本机作为服务端
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
header
GET / HTTP/1.1
Host: 127.0.0.1:7988
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: hibext_instdsigdipv2=1
Upgrade-Insecure-Requests: 1
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""


def server_client(client_socket):

    # response_header定义
    global file_name
    response = b"HTTP/1.1 200 OK\r\n"

    response += b"\r\n"

    # 把浏览器请求的文件取出
    request = client_socket.recv(1024)
    file_request = re.search(r"[^/]+(/[^?* ]*)", str(request))
    file_name = "/"
    if file_request:
        file_name = file_request.group(1)

    if file_name == "/":
        file_name = "/index.html"

    print("客户端机请求文件:", file_name)
    try:
        html_f = open("html"+file_name, "rb")

    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "<h1>------------File NotFound------------</h1>"
    else:
        html_content = html_f.read()
        html_f.close()

        response += html_content

        client_socket.send(response)

    client_socket.close()


def main():
    # 创建套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as http_imititim:
        # 绑定本地的端口
        http_imititim.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        http_imititim.bind(("", 6790))

        # 设置套接字为监听
        http_imititim.listen(128)

        # 接收客服端发送的数据
        while True:
            client_socket, client_addr = http_imititim.accept()
            print(f"用户{client_addr}已连接......")

            server_client(client_socket)


if __name__ == "__main__":
    main()
