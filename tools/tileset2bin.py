#!/usr/bin/env python
from PIL import Image
from pathlib import Path
import sys

def usage():
    print("usage: {} [input file] [output file]".format(sys.argv[0]))

if len(sys.argv) < 2:
    print("No input file supplied")
    usage()
    sys.exit()

if len(sys.argv) < 3:
    print("No output file supplied")
    usage()
    sys.exit()

input_filename = sys.argv[1]
output_filename = sys.argv[2]

if not Path(input_filename).is_file():
    print("{} does not exist".format(input_filename))
    sys.exit()


data = bytearray()

img = Image.open(input_filename)
img_width = img.size[0]
img_height = img.size[1]

if img_width % 8 != 0 or img_height % 8 != 0:
    print("image width or height not divisable by eight")
    sys.exit()

bw = img.convert('1')

for sprite_y in range(0, int(img_height / 8)):
    for sprite_x in range(0, int(img_width / 8)):
        for y in range(0, 8):
            current_byte = 0x00
            for x in range(0, 8):
                current_byte <<= 1
                current_byte |= 1 if bw.getpixel((sprite_x * 8 + x, sprite_y * 8 + y)) > 128 else 0
            data.append(current_byte)

with open(output_filename, "wb") as output_file:
    output_file.write(data)
