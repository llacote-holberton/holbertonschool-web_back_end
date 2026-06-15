#!/usr/bin/env python3
"""Mini script just demonstrating custom decorators definition"""


def track_runtime(func):
    def wrapper(*args, **kwargs):
        print("track_runtime: avant appel")
        result = func(*args, **kwargs)
        print("track_runtime: après appel")
        return result
    return wrapper


def debug_display(func):
    def wrapper(*args, **kwargs):
        print("debug_display: AVANT")
        result = func(*args, **kwargs)
        print("debug_display: APRES")
        return result
    return wrapper


@debug_display
@track_runtime
def hello():
    print("hello!")


if __name__ == "__main__":
    hello()
