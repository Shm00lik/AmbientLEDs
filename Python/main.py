from arduino_io import ArduinoIO
import time

import random


# Function to generate a random hex color
def generate_random_hex_color():
    return "{:06x}".format(random.randint(0, 0xFFFFFF))


ard = ArduinoIO("COM3", 115200)


while True:
    # Generate 86 random hex colors
    COLORS = [generate_random_hex_color() for _ in range(86)]

    start = time.time()

    for _, color in enumerate(COLORS):
        ard.write(f"{_}:{color}\n")
        time.sleep(0.004)

    print("FINISHED AT " + str(time.time() - start))
