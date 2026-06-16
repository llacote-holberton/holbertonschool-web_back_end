# Overview

This repository will hold exercises related to the most modern implementation
  of concurrency processing in Python (async/await syntax with asyncio module)

# General Rules
- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.7.x).
  * Output must match expected formatting exactly.
  * No external libraries are allowed unless explicitly requested.
  * The length of your files will be tested using wc
- All code source must be properly documented, modules and functions.

# Exercises

| Task name                                                     | Filename                        |
|---------------------------------------------------------------|---------------------------------|
| 0. Async Generator                                            | 0-async_generator.py            |
| 1. Async Comprehensions                                       | 1-async_comprehension.py        |
| 2. Run time for four parallel comprehensions                  | 2-measure_runtime.py            |


# Resources

The following are recommended resources and tools


## Documentation

- Internal docs:
    * [Python - Asynchronous execution](https://intranet.hbtn.io/concepts/1173)
    * [Python - Asynchronous Programming](https://intranet.hbtn.io/concepts/1174)
- External:
    * [Real Python: Hands-on on async](https://realpython.com/async-io-python/)
    * [Official asyncio module doc](https://docs.python.org/3/library/asyncio.html)
    * [Official random module doc](https://docs.python.org/3/library/random.html#random.uniform)
    * [Démystifier Python Async (FR)](https://www.metal3d.org/blog/2020/d%C3%A9mystifier-python-async/)
    * [Plongée au cœur de l'asynchrone en Python (FR)](https://zestedesavoir.com/articles/3306/plongee-au-coeur-de-lasynchrone-en-python/)

## Tools
- Online prototyper: https://pythontutor.com/visualize.html#
- Debugger tool: https://docs.python.org/3/library/pdb.html
- Codestyle checker: https://pypi.org/project/pycodestyle/
