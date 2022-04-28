import time

def measure(func,*args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    time_elapsed = end_time - start_time
    print("Time Elapsed: " + str(round(time_elapsed * 1000, 2)) + "ms or " + str(round(time_elapsed, 2)) + "s")