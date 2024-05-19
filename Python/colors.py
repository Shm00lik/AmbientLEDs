from PIL import ImageGrab
import numpy as np

SCREEN_WIDTH = 1920  # Replace with your screen's width
ACTIVE_LEDS = 32
NUM_LEDS = 86
FROM_END = True
HEIGHT_LIMIT = 100  # Use only the first 50 pixels from the height


def get_average_color(pixels):
    # Compute the average color of the given pixels
    avg_color = np.mean(pixels, axis=(0, 1))
    return tuple(avg_color.astype(int))


def get_led_colors(
    screen_width=SCREEN_WIDTH,
    num_leds=NUM_LEDS,
    active_leds=ACTIVE_LEDS,
    height_limit=HEIGHT_LIMIT,
    from_end=FROM_END,
):
    # Capture the screen
    screen = ImageGrab.grab()
    screen_np = np.array(screen)

    # Limit the height to the first 50 pixels
    screen_np = screen_np[:height_limit, :, :]

    # Determine the width of each segment
    segment_width = screen_width // active_leds

    led_colors = ["000000"] * num_leds

    for i in range(active_leds):
        # Calculate the pixel range for this LED
        start_x = i * segment_width
        end_x = (i + 1) * segment_width if i < active_leds - 1 else screen_width

        # Get the segment of pixels
        segment_pixels = screen_np[:, start_x:end_x, :]

        # Calculate the average color of this segment
        avg_color = get_average_color(segment_pixels)

        if from_end:
            led_colors[-(i + 1)] = "{:02x}{:02x}{:02x}".format(*avg_color)
        else:
            led_colors.append("{:02x}{:02x}{:02x}".format(*avg_color))

    return led_colors
