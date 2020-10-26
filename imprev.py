import numpy as np
import cv2
import coloring
from tqdm import tqdm

bad_color_definitions = {
    'Black':        (0, 0, 0),
    'Red':          (151, 4, 12),
    'Green':        (23, 164, 26),
    'Yellow':       (153, 152, 29),
    'Blue':         (5, 22, 175),
    'Magenta':      (175, 25, 175),
    'Cyan':         (25, 165, 175),
    'LightGray':    (191, 191, 191),
    'DarkGray':     (105, 105, 105),
    'LightRed':     (227, 10, 23),
    'LightGreen':   (33, 215, 38),
    'LightYellow':  (229, 228, 49),
    'LightBlue':    (11, 36, 251),
    'LightMagenta': (227, 35, 227),
    'LightCyan':    (39, 229, 228),
    'White':        (230, 229, 230)
}

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

    # cv2.imshow("sample", im)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows()

    out_im = im.copy()
    out_str = ""

    for y in tqdm(range(len(im))):
        for x in range(len(im[y])):
            pixel = list(im[y][x])
            # print(pixel)
            min_dist = float('inf')
            min_value = None
            min_name = None
            for name in color_definitions:
                value = color_definitions[name]
                d = dist(pixel, value)
                # print(d, pixel, value)
                if d < min_dist:
                    min_dist = d
                    min_value = value
                    min_name = name

            # Add to color
            out_im[y,x] = min_value
            out_str += coloring.color("█", color_chars[min_name])

            # Print checks
            # print(pixel, min_value)
            # print(f"setting {(y, x)} to {min_value}")
            # print(f"{out_im[y,x] = }")


    # Print finishing checks
    # print(list(out_im)[:1])
    # print(im.shape)
    # print(out_im.shape)
    # print(out_str)
    # cv2.imshow("out_im", out_im)
    # cv2.imshow("original", im)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return out_str


def rect(size):
    r = "█"
    w, h = size
    arr = [r*w for _ in range(h)]
    out = '\n'.join(arr)
    return out


if __name__ == "__main__":
    # Get size of the terminal
    import os
    try:
        w, h = os.get_terminal_size()
    except OSError:
        w, h = 20, 20

    pref_size = (w, h-2)
    print(prev("sample.png", pref_size))
