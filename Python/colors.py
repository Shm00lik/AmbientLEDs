from PIL import ImageGrab
import numpy as np

SCREEN_WIDTH = 1920  # Replace with your screen's width
SCREEN_HEIGHT = 1200

HEIGHT_LIMIT = 100  # Use only the first 50 pixels from the height

BOTTOM_LEDS = 33
RIGHT_LEDS = 22
TOP_LEDS = 32


def get_average_color(image):
    """Returns the average color of the given image as a tuple (R, G, B)."""
    np_image = np.array(image)
    avg_color = np.mean(np_image, axis=(0, 1))
    return tuple(avg_color.astype(int))


def rgb_to_hex(rgb):
    """Converts an RGB tuple to a HEX string."""
    return "{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])


def capture_screen_and_get_led_colors(
    num_leds_bottom=BOTTOM_LEDS,
    num_leds_right=RIGHT_LEDS,
    num_leds_top=TOP_LEDS,
    screen_width=SCREEN_WIDTH,
    screen_height=SCREEN_HEIGHT,
):
    """Captures the screen and returns a list of HEX colors for each LED on all four sides."""
    # Capture the screenshot
    screenshot = ImageGrab.grab()
    screenshot = screenshot.resize((screen_width, screen_height))

    # Initialize an array to hold the HEX colors for each LED
    led_colors = []

    # Define the width of the strips to average (50 pixels)
    strip_width = HEIGHT_LIMIT

    # Bottom strip (left to right)
    segment_width = screen_width // num_leds_bottom
    for i in range(num_leds_bottom):
        segment = screenshot.crop(
            (
                i * segment_width,
                screen_height - strip_width,
                (i + 1) * segment_width,
                screen_height,
            )
        )
        avg_color = get_average_color(segment)
        led_colors.append(rgb_to_hex(avg_color))

    # Right strip (bottom to top)
    segment_height = screen_height // num_leds_right
    for i in range(num_leds_right):
        segment = screenshot.crop(
            (
                screen_width - strip_width,
                (num_leds_right - 1 - i) * segment_height,
                screen_width,
                (num_leds_right - i) * segment_height,
            )
        )
        avg_color = get_average_color(segment)
        led_colors.append(rgb_to_hex(avg_color))

    # Top strip (right to left)
    segment_width = screen_width // num_leds_top
    for i in range(num_leds_top):
        segment = screenshot.crop(
            (
                screen_width - (i + 1) * segment_width,
                0,
                screen_width - i * segment_width,
                strip_width,
            )
        )
        avg_color = get_average_color(segment)
        led_colors.append(rgb_to_hex(avg_color))

    return led_colors


# led_colors = capture_screen_and_get_led_colors(
#     BOTTOM_LEDS,
#     RIGHT_LEDS,
#     TOP_LEDS,
#     SCREEN_WIDTH,
#     SCREEN_HEIGHT,
# )
# print(led_colors)
