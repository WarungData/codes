#!/usr/bin/env python

#(c) Noprianto, GPL.
#Read first n lines of text files, draw text
#to PNG file.
#simple thunar thumbnailer for text file
#
#Note:
#n = image size / h
#h = font size (20) + extra space (4)
#
#accepts 3 argumens: <input textfile> <output PNG file> [size]
#
#todo: better [margin] calculation

import sys
import os
from PIL import Image, ImageDraw, ImageFont

FONT_SIZE=20
SPACE=4

def main(input, output, size):
    img = Image.new('RGBA', (size, size), '#FFFFFF')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSerif.ttf', 
            FONT_SIZE)
    #
    lines = (size / (FONT_SIZE+SPACE)) 
    chars = size / (FONT_SIZE+SPACE)
    contents = open(input).readlines()[:lines]
    #
    posx = 10
    posy = 0
    diffy = FONT_SIZE + SPACE
    for i in range(lines):
        try:
            text = contents[i][:chars].strip()
        except: 
            text = ''
        draw.text((posx, posy), text, font=font, fill='#000000')
        posy += diffy
    #
    img.save(output, 'PNG')
    #

if __name__ == '__main__':
    if not len(sys.argv) > 2:
        sys.exit(1)
    else:
        input = sys.argv[1]
        output = sys.argv[2]
        try:
            size = int(sys.argv[3])
        except:
            size = 128
        #
        if not os.path.exists(input):
            sys.exit(2)
        #
        main(input, output, size)


