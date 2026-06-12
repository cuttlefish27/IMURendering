#CAN ONLY BE RUN IN A BLENDER INTERFACE
#import bpy
import socket
import threading
import queue

message_queue = queue.Queue()
send_queue = queue.Queue()

HOST = "127.0.0.1"
PORT = 8765

def client_process():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    while True:
        data = client.recv(1024)
        if not data:
            break

        message = data.decode("utf-8")
        message_queue.put(message)
        print(message)
    client.close()

def blender_processes():
    try:
        while True:
            message = message_queue.get_nowait()
            #replace with code that executes the blender object updates
            print(message)
    except queue.Empty:
        pass

    return 0.1

#set daemon = True and remove .join() when running in a blender file

#bpy.app.timer.register(processes)
client_thread = threading.Thread(target=client_process, daemon=False)
client_thread.start()


blender_processes()
client_thread.join()

#loading blender data into variables for each digit of a finger
# dBone = bpy.data.objects["distal"]
# iBone = bpy.data.objects["intermediate"]
# pBone = bpy.data.objects["phalanx"]
