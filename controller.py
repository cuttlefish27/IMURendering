#CAN ONLY BE RUN IN A BLENDER INTERFACE
#import bpy
import socket
import threading


HOST = "127.0.0.1"
PORT = 8765

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("Server listening...")


#def socket_thread() :
conn, addr = server.accept()
print("Connected:", addr)
while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode("utf-8")
    dRot, iRot, pRot = message.split(";")
    print(dRot)
    print(iRot)
    print(pRot)

conn.close()

#threading.Thread(target=socket_thread, daemon=True).start()



#loading blender data into variables for each digit of a finger
# dBone = bpy.data.objects["distal"]
# iBone = bpy.data.objects["intermediate"]
# pBone = bpy.data.objects["phalanx"]
