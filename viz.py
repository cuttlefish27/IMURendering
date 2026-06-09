import serial
import socket
import threading
from tkinter import *
from tkinter import tkk




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











#replace these values with the actual Serial port name and baud rate
PORT = 'PLACEHOLDER'
BAUD = 0000


# with serial.Serial(port=PORT, baudrate=BAUD, timeout = 1) as ser :
#     print(f"Connected to {ser.name}")

#     while True:
#         raw_data = ser.readLine()
#         if raw_data:
#             finger1 = convertData(raw_data)




