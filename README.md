[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
# Helstrom

Helstrom is a quantum state distinguisher with minimum theoretical worst-case probablity of error.

## Features

- Distinguish two qubits with minimum worst-case error.
- Obtain POVMs and min_pwc.
- Support for qudits and entangled states coming soon!

## Tech

Helstrom uses a number of open source projects to work properly:

- [CVXPY] - Python-embedded modeling language for convex optimization problems!
- [MOSEK] - The package for large scale convex, conic and mixed-integer optimization.
- [NumPy] - The fundamental package for scientific computing with Python.

And of course Helstrom itself is a free and open-source software with a [public repository][helstrom] 
on GitHub.

## Installation

Helstrom has been developed and tested to run on [Python 3.8](https://www.python.org/downloads/release/python-3810/).

Install [Python](https://www.python.org/downloads/release/python-3810/) if you have not already.
Download the code as ZIP, and extract it.
Install the dependencies by typing the following command on your terminal:

```sh
cd Helstrom # Change directory into Helstrom
pip install -r requirements.txt
```

Under the ``if __name__ == "__main__": `` heading, modify rho_0 and rho_1 to desired state.
Now run ``helstromSDP.py`` directly, or via the following command on the terminal:
```sh
python -m helstromSDP
```

By default, the states of rho_0 and rho_1 is:
```sh
rho_0 = [ 1 0 ]    rho_1 =  [ 0.5 0 ]
        [ 0 0 ]             [ 0 0.5 ]
```

## Development

Want to contribute? Great!

Helstrom uses Python for developing.
Make changes in your file and create a pull request!

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [CVXPY]: <https://www.cvxpy.org/>
   [MOSEK]: <https://www.mosek.com/>
   [NumPy]: <https://numpy.org/>
   [helstrom]: <https://github.com/benedictusalvian/helstrom>
