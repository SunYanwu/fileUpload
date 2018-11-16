import socket
import os


def file_name(file_dir):
    for files in os.walk(file_dir):
         # 当前路径下所有非目录子文件
        return files
HOST = '127.0.0.1'    
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    list =file_name("F://data")
    filenaemList = list[2]   #获取当前文件夹下的所有非目录文件
    path = list[0]
    data = ''
    for filename in filenaemList:
        data =data + filename + '|' #将文件名加入到data,并以一个特殊字符作为分隔
        dataup = open(path+"//"+filename)
        for line in dataup:
            data = data + line  #将文件内容加入到data
        data = data + '|'
    bytes = data.encode()    #将data转化为字节
    s.send(bytes)
    data = s.recv(1024)
print('Received', repr(data))
