import time


start = time.perf_counter()
time.sleep(0.3)
end = time.perf_counter()
print(f'{end - start:.7f}s elapsed')
