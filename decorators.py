from time import time


def timer(function):
    def inner(*args, **kwargs):
        start = time()
        ret = function(*args, **kwargs)
        end = time()

        diff = end - start
        if diff < 1:
            took = f'{diff * 1000:.0f} milliseconds'
        elif diff < 60:
            took = f'{diff:.1f} seconds'
        elif diff < 3600:
            took = f'{diff / 60:02.0f}:{diff % 60:02.0f} mm:ss'
        else:
            took = f'{diff / 3600:.0f}:{(diff / 60) % 60:02.0f}:{diff % 60:02.0f} *h:mm:ss'

        a = [str(x) for x in args]
        kwa = [f'{x}={y}' for x, y in kwargs.items()]
        rep = f'{function.__name__}({", ".join(a + kwa)})'

        print(f'it took {took} to run {rep}')
        return ret

    return inner
