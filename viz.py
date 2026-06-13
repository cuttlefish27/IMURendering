import serial
import socket
import threading
import queue
import pygame
from serial.tools import list_ports


def find_ports():
    for p in list_ports.comports():
        if "CP2102" in p.description:
            return p.device
    return None

##Host and port info for sockets connection
HOST = "127.0.0.1"
PORT = 8765


## Port and Baud rate info for Serial connection

SERIAL_PORT = None 
if SERIAL_PORT == None:
    SERIAL_PORT = find_ports()

if SERIAL_PORT == None:
    raise Exception("Serial Device not found")

BAUD = 115200


cmd_queue = queue.Queue()
serial_queue = queue.Queue()

def serial_process():
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=0)
    while True:
        cmd = serial_queue.get()
        if cmd == "EXIT":
            break
        ser.write((cmd + "\n").encode("utf-8"))
    ser.close()

def socket_thread() :
    conn = None
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)


    server.settimeout(60)


    print("Server listening...")
    try:
        conn, addr = server.accept()
        print("Connected:", addr)

    except socket.timeout:
        print("No client connected in time")
    if conn:
        while True:
            cmd = cmd_queue.get()
            #print(cmd)
            if cmd == "EXIT":
                break
            message = cmd.encode("utf-8")
            conn.send(message)
        conn.close()




if SERIAL_PORT:
    print("starting serial process")
    serial_thread = threading.Thread(target=serial_process, daemon=False)
    serial_thread.start()

server_thread = threading.Thread(target=socket_thread, daemon=False)
server_thread.start()



pygame.init()
pygame.display.set_mode((100, 100))  # hidden-ish input window


running = True
while running:
    
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                cmd_queue.put("forward")
                serial_queue.put("forward")
            elif event.key == pygame.K_s:
                cmd_queue.put("backward")
                serial_queue.put("backward")
            elif event.key == pygame.K_ESCAPE:
                cmd_queue.put("EXIT")
                serial_queue.put("EXIT")
                running = False

pygame.quit()

serial_thread.join()
server_thread.join()

