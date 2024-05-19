import serial
import time


class ArduinoIO:
    def __init__(self, port: str, baudrate: int = 9600):
        self.ser = serial.Serial(port, baudrate)
        time.sleep(2)

    def read(self):
        return self.ser.readline().decode().strip()

    def write(self, data: str):
        self.ser.write(data.encode())

    def close(self):
        self.ser.close()
