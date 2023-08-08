# ********************************************************************
# Python multiprocessing
# ********************************************************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1
def main():
    a = process(target=counter, args=(50000000,))
    b = process(target=counter, args=(50000000,))
    c = process(target=counter, args=(50000000,))
    d = process(target=counter, args=(50000000,))

    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in: ", time.perf_counter(),"seconds")
if __name__ == '__main__':
    main()