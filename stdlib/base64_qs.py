import base64


orig_str = 'data to be encoded'
byte_str = orig_str.encode()
encoded  = base64.b64encode(byte_str)
decoded  = base64.b64decode(encoded)
new_orig = decoded.decode()

print('Orig str:    ', orig_str)
print('Byte str:    ', byte_str)
print('b64 Encoded: ', encoded)
print('b64 Decoded: ', decoded)
print('Back again:  ', new_orig)


def b64_encode(filename):
    with open(filename, 'rb') as f:
        b = f.read()
    print(type(b))
    return base64.b64encode(b).decode()

print(b64_encode('./test.xml'))
