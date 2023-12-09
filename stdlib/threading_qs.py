import threading
import time


def slow_doubler(n, results):
    time.sleep(1)
    results[n] = n * 2

results = {}
threads = [threading.Thread(target=slow_doubler, args=(n, results)) for n in range(0, 100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
