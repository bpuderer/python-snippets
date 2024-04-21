# bytes - streaming files or transmitting text w/o knowing the encoding. IMMUTABLE
laughBytes = bytes('😂', 'utf-8')
print(laughBytes)
print(laughBytes.decode('utf-8'))

# bytearray - MUTABLE
laughByteArray = bytearray('😂', 'utf-8')
print(laughByteArray)
laughByteArray[-1] = int('83', 16)
print(laughByteArray.decode('utf-8'))
