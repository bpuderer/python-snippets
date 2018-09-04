import time


# time.time() - seconds since epoch as float
start = time.time()
print('snoozing for 300 ms')
time.sleep(0.3)
print(f'{time.time() - start} elapsed')
