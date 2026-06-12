import serial
import socket
import threading
import queue
import pygame

#class representing the current state of the thumb
#curl represents the amount of curl in the finger(last two joints)
#left and right represent the servo angles in the palm

    
HOST = "127.0.0.1"
PORT = 8765

cmd_queue = queue.Queue()

def socket_thread() :
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server listening...")

    conn, addr = server.accept()
    print("Connected:", addr)

    while True:
        cmd = cmd_queue.get()
        if cmd == "EXIT":
            break
        message = cmd.encode("utf-8")
        conn.send(message)
    conn.close()

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
            elif event.key == pygame.K_s:
                cmd_queue.put("backward")
            elif event.key == pygame.K_ESCAPE:
                cmd_queue.put("EXIT")
                running = False

pygame.quit()
 
server_thread.join()











