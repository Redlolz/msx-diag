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

gray = img.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')

for y in range(0, img_height):
    current_byte = 0x00
    for x in range(0, img_width):
        current_byte = (current_byte << 1) | (1 if bw.getpixel((x,y)) > 128 else 0)
    current_byte = current_byte << 2
    data.append(current_byte)

with open(output_filename, "wb") as output_file:
    output_file.write(data)
