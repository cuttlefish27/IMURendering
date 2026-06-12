#CAN ONLY BE RUN IN A BLENDER INTERFACE
#import bpy
import socket
import threading
import queue


HOST = "127.0.0.1"
PORT = 8765

message_queue = queue.Queue()


def socket_thread() :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server listening...")

    conn, addr = server.accept()
    print("Connected:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break

        message = data.decode("utf-8")
        message_queue.put(message)

    conn.close()

def processes():
    try:
        while True:
            message = message_queue.get_nowait()
            #replace with code that executes the blender object updates
    except queue.Empty:
        pass

#set daemon = True and remove .join() when running in a blender file
server_thread = threading.Thread(target=socket_thread, daemon=False)
server_thread.start()

server_thread.join()




#loading blender data into variables for each digit of a finger
# dBone = bpy.data.objects["distal"]
# iBone = bpy.data.objects["intermediate"]
# pBone = bpy.data.objects["phalanx"]
