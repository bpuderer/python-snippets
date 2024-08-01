"""
pip install python-barcode
pip install cairosvg
pip install pillow
pip install pyzbar
sudo apt-get install libzbar0
"""

import barcode
from barcode.writer import ImageWriter, SVGWriter
from PIL import Image
from pyzbar.pyzbar import decode


def create_svg_barcode(data, filename, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open(filename, "wb") as f:
        FMT(str(data), writer=SVGWriter()).write(f)

def create_jpeg_barcode(data, filename, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open(filename, "wb") as f:
        FMT(str(data), writer=ImageWriter()).write(f)

def read_barcode_from_image(filename):
    with Image.open(filename) as image:
        barcodes = decode(image)
        #return [(barcode.type, barcode.data.decode('utf-8')) for barcode in barcodes]
        return barcodes[0].data.decode('utf-8')



# https://en.wikipedia.org/wiki/International_Article_Number#Calculation_of_checksum_digit
# checksum digit = 8
data = 100000011111
filename = 'test_barcode.svg'
create_svg_barcode(data, filename)

filename = 'test_barcode.jpeg'
create_jpeg_barcode(data, filename)
print(read_barcode_from_image(filename))


# Code 39
create_jpeg_barcode(data, filename, fmt='code39')
print(read_barcode_from_image(filename))
