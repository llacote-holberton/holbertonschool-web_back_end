#!/usr/bin/env python3
import random
import asyncio
import time  # on s'en servira après

# Code adapted from examples illustrating
# https://www.metal3d.org/blog/2020/d%C3%A9mystifier-python-async/
# Improved it by renaming each main/run variants and using a
#   decorator for timetracking.


def track_runtime(func):
    """@decorator to track time spent to complete function call"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Total time ({func.__name__}): {end - start:.4f} seconds")
        return result
    return wrapper


def debug_display(func):
    """@decorator to add/remove when we want extra info outputted"""

    # WARNING: executed EACH TIME a function is decorated with it.
    # Because the "main body" of decorator is executed whenever
    # a function decorated with it IS DEFINED. NOT WHEN IT IS CALLED.
    print("Inside debug display")

    # ONLY THIS PART runs at CALL time. In practice, "decoration" doesn't
    #   modify the original function: it keeps it alive (referenced via
    #   the closure) and REBINDS the outer name (e.g. run_concurrent) to
    #   point to a new object (`wrapper`) instead.
    #   Think of it like a pointer: the name's "address" changes, and the
    #   new target itself holds a (hidden) pointer back to the original
    #   function — which stays alive precisely because of that reference.
    def wrapper(*args, **kwargs):
        print(f"\n---- START processing of called {func.__name__} ----")
        result = func(*args, **kwargs)
        print(f"---- {func.__name__} ENDED ----\n")
        return result
    return wrapper


# async => la fonction est une coroutine
async def bigWork(i):
    print('Big work %d starts' % i)
    delay = random.uniform(0, 1.5)
    # surtout n'utilisez pas time.sleep()
    # pour rappel, il faut avoir un appel à await pour que
    # la coroutine bigWork puisse laisser une chance aux autres
    # de tourner
    await asyncio.sleep(delay)
    print('Big work %d ends after %.2f seconds' % (i, delay))


# Async but fully sequential example
async def main_fully_sequential():
    # on va lancer 5 coroutines
    for i in range(5):
        await bigWork(i)


def run_sequential():
    start = time.time()
    asyncio.run(main_fully_sequential())  # on démarre ici
    end = time.time() - start
    print('Total time: %.2f' % end)


async def main_concurrent():
    tasks = []
    for i in range(5):
        tasks.append(bigWork(i))

    # on attend que la liste
    # de coroutines soit terminée
    await asyncio.wait(tasks)


@debug_display
@track_runtime
def run_concurrent():
    # "Manual time tracking" replaced by decorator
    # start = time.time()
    asyncio.run(main_fully_sequential())  # on démarre ici
    # end = time.time() - start
    # print('Total time: %.2f' % end)


@debug_display
@track_runtime
def test_decorators():
    print("Coucou")


if __name__ == "__main__":
    run_sequential()
    run_concurrent()
