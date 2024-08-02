"""
    https://github.com/lincolnloop/python-qrcode
    pip install qrcode
"""

from common import decode_barcode, decode_barcode_zxing
import qrcode


filename = 'qrcode_ex1.png'
data = 'Some data here'
img = qrcode.make(data)
img.save(filename)
print(decode_barcode(filename))


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
print(decode_barcode_zxing(filename))
