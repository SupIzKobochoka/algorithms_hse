import time

def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        return res, end_time - start_time
    return wrapper
