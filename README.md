# Overview

This repository will hold many projects to learn how to craft efficient backends.

# General Rules

- A `README.md` file, at the root of the folder of the project, is mandatory
- Allowed editors: `vi`, `vim`, `emacs`



## Python projects


- Corrections will run on Ubuntu 20.04 LTS.
- Python version used for correction: Python 3.8.x.
- Every Python file must start exactly with:  
  `#!/usr/bin/env python3`
- Every Python file must:
  * Be executable.
  * End with a newline.
  * Be PEP8 compliant (pycodestyle 2.5|7.x).
  * Output must match expected formatting exactly.
  * No external libraries are allowed unless explicitly requested.
- All your functions and coroutines must be type-annotated.
  * **Use the right type-annotation types that works with version 3.8 of Python**
- All of your code source must be documented: a documentation is not a simple word, it&#39;s a real sentence explaining what&#39;s the purpose of the module, class or method (the length of it will be verified)
  * Modules (`python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;`)
  * Functions (`python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;`
- The length of your files will be tested using `wc`


# Exercises

Confer each directory for dedicated README with related objectives and list of tasks.

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
