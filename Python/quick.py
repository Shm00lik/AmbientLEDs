from arduino_io import ArduinoIO

ard = ArduinoIO("COM3", 115200)
MAX = 86

try:
    while True:
        num = int(input("NUM OF LEDS: "))

        for i in range(MAX):
            if i >= num:
                ard.write(f"<{i}:000000>")
            else:
                ard.write(f"<{i}:FF0000>")

        ard.write(f"<END>")

except KeyboardInterrupt:
    print("Stopped...")
finally:
    ard.close()
