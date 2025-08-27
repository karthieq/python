import concurrent.futures
import time


def do_something(sec):
    print(f'Sleeping {sec} secs ...')
    time.sleep(sec)
    return f'Done sleeping {sec} secs ...'

t1 = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

t2 = time.perf_counter()

print(f'Total: {round(t2-t1,2)} secs')
