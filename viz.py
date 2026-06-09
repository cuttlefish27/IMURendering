import serial

#replace these values with the actual Serial port name and baud rate
PORT = 'PLACEHOLDER'
BAUD = 0000



with serial.Serial(port=PORT, baudrate=BAUD, timeout = 1) as ser :
    print(f"Connected to {ser.name}")

    while True:
        raw_data = ser.readLine()
        if raw_data:
            clean_text = raw_data.decode('utf-8').strip()
            print(f"Received: {clean_text}")




