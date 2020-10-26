import numpy as np
import cv2
import coloring
from tqdm import tqdm

color_definitions = {
    'Black':        (0, 0, 0),
    'Red':          (12, 4, 151),
    'Green':        (26, 164, 23),
    'Yellow':       (29, 152, 153),
    'Blue':         (175, 22, 5),
    'Magenta':      (175, 25, 175),
    'Cyan':         (175, 165, 25),
    'LightGray':    (191, 191, 191),
    'DarkGray':     (105, 105, 105),
    'LightRed':     (23, 10, 227),
    'LightGreen':   (38, 215, 33),
    'LightYellow':  (49, 228, 229),
    'LightBlue':    (251, 36, 11),
    'LightMagenta': (227, 35, 227),
    'LightCyan':    (228, 229, 39),
    'White':        (230, 229, 230)
}

color_chars = {
    'Black':        "\033[30m",
    'Red':          "\033[31m",
    'Green':        "\033[32m",
    'Yellow':       "\033[33m",
    'Blue':         "\033[34m",
    'Magenta':      "\033[35m",
    'Cyan':         "\033[36m",
    'LightGray':    "\033[37m",
    'DarkGray':     "\033[90m",
    'LightRed':     "\033[91m",
    'LightGreen':   "\033[92m",
    'LightYellow':  "\033[93m",
    'LightBlue':    "\033[94m",
    'LightMagenta': "\033[95m",
    'LightCyan':    "\033[96m",
    'White':        "\033[97m",
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
    im = cv2.resize(cv2.imread(im_file), size)
    out_im = im.copy()
    out_str = ""

    for y in tqdm(range(len(im))):
        for x in range(len(im[y])):
            pixel = list(im[y][x])
            min_dist = float('inf')
            min_value = None
            min_name = None

            for name in color_definitions:
                value = color_definitions[name]
                d = dist(pixel, value)
                if d < min_dist:
                    min_dist = d
                    min_value = value
                    min_name = name

            # Add to color
            out_im[y,x] = min_value
            out_str += coloring.color("█", color_chars[min_name])

    return out_str


if __name__ == "__main__":
    # Get size of the terminal
    import os
    try:
        w, h = os.get_terminal_size()
    except OSError:
        w, h = 20, 20

    pref_size = (w, h-2)
    print(prev("sample.png", pref_size))
