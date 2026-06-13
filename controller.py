##CAN ONLY BE RUN IN A BLENDER INTERFACE
## All lines of code containing one # need to be uncommented
## keep all lines that have two ##
## comment out any lines that say comment out next to them
## All comments are here to ensure that code for sockets and threading compiles inside of an external editor

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
    #cube = bpy.data.objects["Cube"]
    try:
        while True:
            message = message_queue.get_nowait()

            if message == "forward":
               #cube.location.x += 1
               pass
            elif message == "backward":
                #cube.location.x -=1
                pass
            print(message)
    except queue.Empty:
        pass

    return 0.1

##set daemon = True and remove .join() when running in a blender file

#bpy.app.timers.register(blender_processes)
client_thread = threading.Thread(target=client_process, daemon=True)
client_thread.start()


blender_processes() #comment out
client_thread.join() #comment out

