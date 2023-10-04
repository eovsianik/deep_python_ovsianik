import time


def mean(k):
    times = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(times) == k:
                times.pop(0)
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            times.append(end_time - start_time)
            print(f"Average time of the last {k} calls: {sum(times)/len(times)}")
            return result

        return wrapper

    return decorator
