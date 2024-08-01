"""
pip install python-barcode
pip install cairosvg
pip install pillow
pip install pyzbar
sudo apt-get install libzbar0
"""

import barcode
from barcode.writer import SVGWriter
from barcode.writer import ImageWriter
from PIL import Image
from pyzbar.pyzbar import decode


def create_svg_barcode(data, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open("test_barcode.svg", "wb") as f:
        FMT(str(data), writer=SVGWriter()).write(f)

def create_jpeg_barcode(data, fmt='ean13'):
    FMT = barcode.get_barcode_class(fmt)
    with open("test_barcode.jpeg", "wb") as f:
        FMT(str(data), writer=ImageWriter()).write(f)

def read_barcode_from_image(image_path):
    image = Image.open(image_path)
    barcodes = decode(image)
    return [(barcode.type, barcode.data.decode('utf-8')) for barcode in barcodes]


# https://en.wikipedia.org/wiki/International_Article_Number#Calculation_of_checksum_digit
# checksum digit = 8
data = 100000011111
create_svg_barcode(data)
create_jpeg_barcode(data)
print(read_barcode_from_image('./test_barcode.jpeg'))
