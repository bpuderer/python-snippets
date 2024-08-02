"""
pip install python-barcode
pip install cairosvg
"""
from common import decode_barcode

import barcode
from barcode.writer import ImageWriter, SVGWriter


def create_svg_barcode(data, filename, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open(filename, "wb") as f:
        FMT(str(data), writer=SVGWriter()).write(f)

def create_jpeg_barcode(data, filename, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open(filename, "wb") as f:
        FMT(str(data), writer=ImageWriter()).write(f)


# https://en.wikipedia.org/wiki/International_Article_Number#Calculation_of_checksum_digit
# checksum digit = 8
data = 100000011111
filename = 'test_barcode.svg'
create_svg_barcode(data, filename)

filename = 'test_barcode.jpeg'
create_jpeg_barcode(data, filename)
print(decode_barcode(filename))


# Code 39
create_jpeg_barcode(data, filename, fmt='code39')
print(decode_barcode(filename))
