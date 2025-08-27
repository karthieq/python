import threading
import time

def do_something(secs):
    print(f'Sleeping {secs} secs ...')
    time.sleep(secs)
    print(f'Done sleeping {secs} secs ...')

t1 = time.perf_counter()

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

t2 = time.perf_counter()

print(f'Total: {round(t2-t1,2)} secs')
