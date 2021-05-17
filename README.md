# Helstrom &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/benedictusalvian/helstrom/blob/main/LICENSE.md) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/benedictusalvian/helstrom/issues)

Helstrom is a quantum state distinguisher with minimum theoretical worst-case probability of error.

## Features

- Distinguish two qubits with minimum worst-case error.
- Obtain POVMs and min_pwc.
- Now available on PyPI!
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

You could install Helstrom via pip by running:
```sh
pip install helstrom
```

Note: MOSEK requires an academic license to operate. Academic faculty, students or staff gets free license. [Apply for a license.](https://www.mosek.com/products/academic-licenses/)

Alternatively, download the code as ZIP, extract it, and enter the folder.
Then, install the dependencies by typing the following command on your terminal:

```sh
cd helstrom-main # Change directory into child directory
pip install -r requirements.txt
```

## Examples

Now run the following command on the terminal to use Helstrom's SDP and the results will be printed:

```sh
python -m helstrom "1 0; 0 0" "1 0; 0 1"
# Pass in desired states of rho_0 and rho_1 as two arguments
```

If the two arguments are not provided, by default, the states rho_0 and rho_1 are:
```sh
rho_0 = [ 1 0 ]    rho_1 =  [ 0.5 0 ]
        [ 0 0 ]             [ 0 0.5 ]
        # "1 0; 0 0"          # "0.5 0; 0 0.5"
```

If Helstrom was downloaded via ZIP, you may run ``helstromSDP.py`` directly.

Helstrom can be used as part of your code. Simply,
```sh
import helstrom
helstrom.sdp(rho_0, rho_1)
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
