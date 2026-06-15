#!/usr/bin/env python3
import random
import asyncio
import time  # on s'en servira après

# Code adapted from examples illustrating
# https://www.metal3d.org/blog/2020/d%C3%A9mystifier-python-async/
# Improved it by renaming each main/run variants and using a
#   decorator for timetracking.


# ===== DECORATORS =====
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


# ===== TUTO EXAMPLES ADAPTED =====

# Defining a Coroutine subtype of function
async def bigWork(i):
    print('Big work %d starts' % i)
    delay = random.uniform(0, 1.5)
    # surtout n'utilisez pas time.sleep()
    # pour rappel, il faut avoir un appel à await pour que
    # la coroutine bigWork puisse laisser une chance aux autres
    # de tourner
    await asyncio.sleep(delay)
    print('Big work %d ends after %.2f seconds' % (i, delay))


# === Example 1: async but fully sequential

# Because we use a for loop  which forcefully creates a sequence...
async def main_fully_sequential():
    # on va lancer 5 coroutines
    for i in range(5):
        await bigWork(i)


def run_sequential():
    start = time.time()
    asyncio.run(main_fully_sequential())  # on démarre ici
    end = time.time() - start
    print('Total time: %.2f' % end)


# === Example 2: async and "concurrent" through "cooperation"
# With also examples of what NOT to do. ^^ŝ

# WARNING: WILL RAISE EXCEPTION: SAME PROBLEM AS what was commented above
async def faulty_main():
    tasks = []
    for i in range(5):
        # We are actually adding Coroutines
        tasks.append(bigWork(i))

    for t in tasks:
        # Coroutine is NOT an "Awaitable" object -> TypeError:
        # An asyncio.Future, a coroutine or an awaitable is required
        await t


async def main_concurrent():
    tasks = []
    # WARNING from 3.8 onwards giving Coroutines and not Tasks
    #   is deprecated. AND a STRICT ERROR from 3.14 onwards.
    # for i in range(5):
    #     # Calling bigwork returns a Coroutine, not a Task!
    #     tasks.append(bigWork(i))
    # await asyncio.wait(tasks)

    # Option 1: method gather() which accepts Coroutines
    # my_coroutines = []
    # for i in range(5):
    #     my_coroutines.append(bigWork(i))
    # # Gather expects positional arguments so we use list unpacking with '*'
    # await asyncio.gather(*my_coroutines)
    # # Gather automatically returns a list of results in same order as "input"

    # Option 2: method create_task, encapsulates a Coroutine in a Task
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(bigWork(i)))
    await asyncio.wait(tasks)


"""
    Differences (summarized) between COROUTINE and TASK
    COROUTINE is technically a suspendable function which is paused immediately
      after being "called".
        With culinary metaphor it would be "a recipe".
    TASK is an object representing the integration of the coroutine in a list
      of instructions to execute, aka planning the actual execution of the
      target function in the event loop managed by an orchestrator.
        With culinary metaphor the event loop manager the "cook chief", and
        the task would be a saucepan set to cook, with a ticket returned so the
        waiter can track how it goes and when it finishes.
    Oneliner: Coroutine is "WHAT TO DO",
              Task is "WHEN AND HOW IT WILL/HAS BEEN DONE"
    Which is why Task "encapsulates" Coroutine and not reverse,
    since it is Task which holds the "state info" on the process.
"""


@debug_display
@track_runtime
def run_concurrent():
    # "Manual time tracking" replaced by decorator
    # start = time.time()
    asyncio.run(main_concurrent())  # on démarre ici
    # end = time.time() - start
    # print('Total time: %.2f' % end)


# === Example 3: "sequential mode", explicitely creating tasks ===
async def main_explicit_sequential():
    tasks = []
    for i in range(5):
        coroutine = bigWork(i)
        # NOTE: create_task SCHEDULES the task to start, not immediately
        #   (synchronously) *but* as soon as the event loop gets control back
        #   (i.e. at the next `await`).
        task = asyncio.create_task(coroutine)
        tasks.append(task)
    for t in tasks:
        # Despite awaiting in order, the underlying tasks were ALL already
        #   scheduled (via create_task) before this loop even started, so
        #   they're running concurrently in the background. This loop just
        #   controls the ORDER in which we retrieve results/exceptions,
        #   not WHEN the work happens. Total time should be close to
        #   main_concurrent's, NOT main_fully_sequential's.
        await t


@debug_display
@track_runtime
def test_decorators():
    print("Coucou")


if __name__ == "__main__":
    run_sequential()
    run_concurrent()
