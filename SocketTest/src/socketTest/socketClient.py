import json
import os
import socket
import struct
import sys

download_dir = r'd:\download'  # 文件存放地址


def get(pc):
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
    with open('%s/%s' % (download_dir, file_name), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            res = pc.recv(1024)
            f.write(res)
            recv_size += len(res)
            print('总大小：%s  已经下载大小：%s' % (total_size, recv_size))


def put(cmds, conn):
    filename = cmds[1]
    # 3.以读的方式打开,读取文件
    # 1制作报头
    header_dic = {
        'filename': filename,
        'md5': 'xxdxx',
        'file_size': os.path.getsize(r'%s/%s' % (download_dir, filename))
    }
    header_json = json.dumps(header_dic)
    header_bytes = header_json.encode('utf-8')

    # 2 发送报头长度
    conn.send(struct.pack('i', len(header_bytes)))  # 固定长度4

    # 3 发报头
    conn.send(header_bytes)
    # 4发真实数据
    send_size = 0
    with open('%s/%s' % (download_dir, filename), 'rb') as f:
        # conn.send(f.read())
        for a in f:
            conn.send(a)
            send_size += len(a)
            print(send_size)


def run():
    pc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pc.connect(('127.0.0.1', 10000))
    print(pc)
    while True:
        # 1.发命令
        inp = input('>>>:').strip()  # get a.text
        if not inp:
            continue
        pc.send(inp.encode('utf-8'))
        cmds = inp.split()
        if cmds[0] == 'get':
            get(pc)
        elif cmds[0] == 'put':
            put(cmds, pc)
        elif cmds[0] == 'stop':
            sys.exit(0)
    pc.close()


if __name__ == '__main__':
    run()
