# uses OpenCV instead of pillow as in the others
# has problems decoding data matrix barcode produced by pylibdmtx

import cv2
from pyzbar.pyzbar import decode
import zxingcpp


def decode_barcode(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    if not decoded_objects:
        return None
    return decoded_objects[0].data.decode('utf-8')

def decode_barcode_zxing(image_path):
    img = cv2.imread(image_path)
    decoded_objects = zxingcpp.read_barcodes(img)
    if not decoded_objects:
        return None
    return decoded_objects[0].text
