import socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_add="192.168.137.10"
port=2020
complete=(ip_add,port)
message=input("msg.....")
encode_msg=message.encode('ascii')
s.sendto(encode_msg,complete)