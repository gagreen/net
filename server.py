import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
data = client_socket.recv(65535)

__, a, b = data.decode().split('/')

if a == 'nayeon' and b == 'height':
    data = "163cm 중간 정도"
elif a == 'nayeon' and b == 'weight':
    data = '48kg 평균' 
elif a == 'junghyun' and b == 'height' :
    data = '168cm 큰 정도' 
elif a == 'junghyun' and b == 'weight':
    data = '48kg 평균' 
elif a == 'momo' and b == 'height' :
    data = '170cm 큰 정도'
elif a == 'momo' and b == 'weight':
    data = '52kg 평균 이상'
elif a == 'sana' and b == 'height' :
    data = '164cm 중간 정도'
elif a == 'sana' and b == 'weight':
    data = '48kg 평균'
elif a == 'jihyo' and b == 'height' :
    data = '160cm 작은 정도'
elif a == 'jihyo' and b == 'weight':
    data = '48kg 평균'
elif a == 'mina' and b == 'height' :
    data = '163cm 중간 정도'
elif a == 'mina' and b == 'weight':
    data = '46kg 평균 이하' 
elif a == 'dahyun' and b == 'height' :
    data = '158cm 작은 정도'
elif a == 'dahyun' and b == 'weight':
    data = '48kg 평균'
elif a == 'chaeyoung' and b == 'height' :
    data = '159cm 작은 정도'
elif a == 'chaeyoung' and b == 'weight':
    data = '49kg 평균'
elif a == 'tsuwi' and b == 'height' :
    data = '170cm 큰 정도'
elif a == 'tsuwi' and b == 'weight':
    data = '52kg 평균 이상'
else :
    data = "Not supported" 


client_socket.send(data.encode())
