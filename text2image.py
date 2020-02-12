#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFont
import os, sys, getopt

def main(argv):
    output_filename = "output.png" #default output filename
    code = ""
    try:
        opts, args = getopt.getopt(argv,"i:o:",[])
    except getopt.GetoptError:
        print("Usage: text2image -i input.txt -o output_name.png")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            fo = open(arg, "r")
            lines = fo.readlines()
            for line in lines:
                tab_to_space_line = line.replace('\t', '    ')
                code += tab_to_space_line
            fo.close()
            os.remove(arg)
        elif opt == '-o':
            output_filename = arg
    im = Image.new('RGBA', (1200, 600), (48, 10, 36, 255)) #background like Ubuntu
    draw = ImageDraw.Draw(im)
    try:
        fontsFolder = '/usr/share/fonts/truetype'
        monoFont = ImageFont.truetype(os.path.join(fontsFolder, 'UbuntuMono-R.ttf'), 32)
        draw.text((50, 10), code, fill='white', font=monoFont)
    except Exception as ex:
        draw.text((10, 10), code, fill='white')
    im.save(output_filename)

if __name__ == "__main__":
    main(sys.argv[1:])
