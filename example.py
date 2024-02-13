import math
from time import perf_counter
from multiprocessing import Process


def prime_count(*args):
    n, m = args[0], args[1]

    n = n + 1 if n % 2 == 0 else n
    s = 0
    # ls = []

    for i in range(n, m, 2):
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                break
        else:
            s += 1
            # ls.append(i)
    # if ls[0] == 1:
        # ls[0] = 2
    print(f"In interval [{n}-{m}] has {s} prime count")
    # print(ls)


if __name__ == '__main__':
    processes = []

    start = perf_counter()
    # Create process
    for i in range(1, 1_000_000, 2_50_000):
        process = Process(target=prime_count, args=[i, 2_49_999+i])
        processes.append(process)
        process.start()

    # wait for all processes to finish
    for process in processes:
        process.join()

    end = perf_counter()
    print(f"Process run time: {end - start: .3f}")

# In interval [1-250000] has 22044 prime count
# In interval [250001-500000] has 19494 prime count
# In interval [500001-750000] has 18700 prime count
# In interval [750001-1000000] has 18260 prime count
# Process run time:  1.192
