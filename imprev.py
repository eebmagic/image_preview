import numpy as np
import cv2
import coloring
import time

color_definitions = {
    'Black':        ((0, 0, 0), "\033[30m"),
    'Red':          ((12, 4, 151), "\033[31m"),
    'Green':        ((26, 164, 23), "\033[32m"),
    'Yellow':       ((29, 152, 153), "\033[33m"),
    'Blue':         ((175, 22, 5), "\033[34m"),
    'Magenta':      ((175, 25, 175), "\033[35m"),
    'Cyan':         ((175, 165, 25), "\033[36m"),
    'LightGray':    ((191, 191, 191), "\033[37m"),
    'DarkGray':     ((105, 105, 105), "\033[90m"),
    'LightRed':     ((23, 10, 227), "\033[91m"),
    'LightGreen':   ((38, 215, 33), "\033[92m"),
    'LightYellow':  ((49, 228, 229), "\033[93m"),
    'LightBlue':    ((251, 36, 11), "\033[94m"),
    'LightMagenta': ((227, 35, 227), "\033[95m"),
    'LightCyan':    ((228, 229, 39), "\033[96m"),
    'White':        ((230, 229, 230), "\033[97m"),
}


def dist(a, b):
    diffs = [abs(x - y) / 255 for x, y in zip(a, b)]
    return sum(diffs) / (3 * 1)


def prev(im_file, size):
    w, h = size
    assert type(im_file), str
    assert type(w), int
    assert type(h), int

    # Read and reshape image
    load_start = time.time()
    im = cv2.resize(cv2.imread(im_file), size)
    out_im = im.copy()
    out_str = ""
    load_durr = time.time() - load_start
    print(f"{load_durr = }")

    iter_start = time.time()
    for y in range(len(im)):
        for x in range(len(im[y])):
            pixel = list(im[y][x])
            min_dist = float('inf')
            min_value = None
            min_name = None

            for name in color_definitions:
                value = color_definitions[name][0]
                d = dist(pixel, value)
                if d < min_dist:
                    min_dist = d
                    min_value = value
                    min_name = name

            # Add to color
            out_im[y,x] = min_value
            out_str += coloring.color("█", color_definitions[min_name][1])
    iter_durr = time.time() - iter_start
    print(f"{iter_durr = }")

    return out_str


if __name__ == "__main__":
    start = time.time()
    # Get size of the terminal
    import os
    try:
        w, h = os.get_terminal_size()
    except OSError:
        w, h = 20, 20

    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[-1]
    else:
        filename = "./images/sample.png"

    pref_size = (w, h-2)
    print(prev(filename, pref_size))
    prev(filename, pref_size)
    duration = (time.time() - start) * 100
    print(f"{duration = }")
