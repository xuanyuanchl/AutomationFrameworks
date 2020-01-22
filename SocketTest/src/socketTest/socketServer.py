import json
import os
import socket
import struct


share_dir = r'd:\shared'  # 文件地址


def get(cmds, conn):
    filename = cmds[1]
    # 3.以读的方式打开,读取文件
    # 1制作报头
    header_dic = {
        'filename': filename,
        'md5': 'xxdxx',
        # E:\study\第3模块，面向对象\网络编程\文件传输\server\share\jiaoyue.mp4
        'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))
    }
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 2 发送报头长度
    conn.send(struct.pack('i', len(header_bytes)))  # 固定长度4

    # 3 发报头
    conn.send(header_bytes)
    # 4发真实数据
    with open('%s/%s' % (share_dir, filename), 'rb') as f:
        # conn.send(f.read())
        for a in f:
            conn.send(a)


def put(pc):
    # 2.接受文件内容，以写的方式打开一个新文件，写入客户端新文件中
    # 1收报头长度
    obj = pc.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 2接收报头
    header_bytes = pc.recv(header_size)

    # 3解析报头,对于数据的描述
    header_json = header_bytes.decode('utf-8')
    header_dic = json.loads(header_json)
    print(header_dic)
    total_size = header_dic['file_size']
    file_name = header_dic['filename']

    # 4 接受真实的数据
    with open('%s/%s' % (share_dir, file_name), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            res = pc.recv(1024)
            f.write(res)
            recv_size += len(res)
            print('总大小：%s  已经下载大小：%s' % (total_size, recv_size))


def run():
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 回收重用端口10000
    phone.bind(('127.0.0.1', 10000))  # 0-65535  0-1024给操作系统，
    phone.listen(5)
    while True:  # 建链接循环
        conn, client_addr = phone.accept()
        print(client_addr)
        while True:  # 通信循环
            try:
                # 1.收命令
                res = conn.recv(1024)  # get jiaoyue.mp4
                # 2.解析命令，提取相应命令参数
                cmds = res.decode('utf-8').split()  # ['get', 'jiaoyue.mp4']
                if cmds[0] == 'get':
                    get(cmds, conn)
                elif cmds[0] == 'put':
                    put(conn)
                elif cmds[0] == 'stop':
                    print('成功关闭连接')
                    break
            except ConnectionResetError:
                break
        conn.close()
    phone.close()


if __name__ == '__main__':
    run()
