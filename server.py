import socket
HOST = ''                 
PORT = 50007              
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(2048)
            str = bytes.decode(data)
            print("分割前：" +str)
            serviceData =str.split('|')
            print("分割后：")
            print(serviceData)
            print(len(serviceData))
            i = 0;
            while i < len(str)-1:
                j = i+1;
                servicedir = open('F://serviceData//'+serviceData[i],'w',encoding='utf-8')
                i = i+2;
                servicedir.write(serviceData[j])
            if not data: break
            conn.sendall(data)
