"""
pip install pylibdmtx
pip install pillow
sudo apt-get install libdmtx0b
"""

from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image


data = "HELLO123"
filename = 'datamatrix.png'

encoded = encode(data.encode('utf-8'))
image = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
image.save(filename)


image = Image.open(filename)
decoded_data = decode(image)
print(decoded_data[0].data.decode('utf-8'))
