from arduino_io import ArduinoIO
import time
from colors import get_led_colors
import random


# Function to generate a random hex color
def generate_random_hex_color():
    return "{:06x}".format(random.randint(0, 0xFFFFFF))


def generate_random_color():
    return random.choice(["R", "G", "B"])


ard = ArduinoIO("COM3", 115200)

last_send = {}

try:
    while True:
        # Generate 86 random hex colors
        COLORS = get_led_colors()

        start = time.time()

        sent = False

        for i, color in enumerate(COLORS):
            if i in last_send and last_send.get(i) == color:
                continue

            sent = True
            last_send[i] = color

            print(f"SENDING <{i}:{color}>")

            ard.write(f"<{i}:{color}>")

            # d = ard.read()

            # print("RECEIVED: " + d)

        if sent:
            print("SENDING <END>")
            ard.write("<END>")

        # d = ard.read()

        # print("RECEIVED: " + d)

except KeyboardInterrupt:
    print("Stopped...")
finally:
    ard.close()
