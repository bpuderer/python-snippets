"""
    https://github.com/lincolnloop/python-qrcode
    pip install qrcode
    pip install pyzbar
    pip install pillow
"""

from pyzbar.pyzbar import decode
from PIL import Image
import qrcode


def decode_qrcode(filename):
    image = Image.open(filename)
    decoded_data = decode(image)
    return decoded_data[0].data.decode('utf-8')


filename = 'qrcode_ex1.png'
data = 'Some data here'
img = qrcode.make(data)
img.save(filename)
print(decode_qrcode(filename))


filename = 'qrcode_ex2.png'
data = "HELLO123"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save(filename)
print(decode_qrcode(filename))
