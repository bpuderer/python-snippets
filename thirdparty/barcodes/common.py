# uses OpenCV instead of pillow as in the others
# has problems decoding data matrix barcode produced by pylibdmtx

import cv2
from pyzbar.pyzbar import decode


def decode_barcode(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    return decoded_objects[0].data.decode('utf-8')
