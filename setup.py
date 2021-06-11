import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='helstrom',
    packages=find_packages(),
    version='0.3',
    license='MIT',
    description=' A quantum state distinguisher with minimum theoretical worst-case probability of error.',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Benedictus Alvian Sofjan',
    author_email='benedictus.sofjan@gmail.com',
    url='https://github.com/benedictusalvian/helstrom',
    keywords=['python', 'quantum', 'quantum-computing',
              'quantum-information', 'quantum-theory', 'helstrom', 'distinguisher'],
    install_requires=[
        'cvxpy >= 1.1.12',
        'Mosek >= 9.2.43',
        'numpy >= 1.20.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "helstrom=helstrom.__main__:main",
        ]
    },
)
