import time

def main():
    test_vals = [5, 10, 15, 20, 25, 30]
    recur_times = []
    iter_times = []
    for test_val in test_vals:
        # time recursive
        start_time = time.time()
        print fib(test_val)
        recur_times.append(time.time() - start_time)
        # time iterative
        start_time = time.time()
        print iter_fib(test_val)
        iter_times.append(time.time() - start_time)
    # print out recursive and iterative timings
    for t in recur_times:
        print("[recursive] %s seconds" % t)
    for t in iter_times:
        print("[iterative] %s seconds" % t)

# recursive
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# iterative
def iter_fib(n):
    cur_fib = 0
    prev_fib = 1
    temp_fib = 0
    for i in range(1, n):
        temp_fib = cur_fib + prev_fib
        prev_fib = cur_fib
        cur_fib = temp_fib
    return fib


if __name__ == '__main__':
    main()