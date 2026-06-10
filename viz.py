import serial
import socket
import threading
from pynput import keyboard

#class representing the current state of the thumb
#curl represents the amount of curl in the finger(last two joints)
#left and right represent the servo angles in the palm


class Finger():
    def __init__(self, curl, left, right):
        self.curl = curl
        self.left = left
        self.right = right
        

def convertData(rawdata: bytes):
    chars = rawdata.decode('utf-8')
    curl, left, right = chars.split(',')
    f1 = Finger(curl, left, right)
    return f1

HOST = "127.0.0.1"
PORT = 8765

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))
message = "1;2;3"
client.send(message.encode())

client.close()





# with serial.Serial(port=PORT, baudrate=BAUD, timeout = 1) as ser :
#     print(f"Connected to {ser.name}")

#     while True:
#         raw_data = ser.readLine()
#         if raw_data:
#             finger1 = convertData(raw_data)




