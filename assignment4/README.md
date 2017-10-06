### Short description
The reports have a short description of what I struggled with and the end result. (Everything should be working as intended)

The assignment4 folder have the python files, the test files are in assignment4/test


### How to use the packet found in /dist/
Build by running:
`python3 setup.py build_ext --inplace`

Make a package by running:
`python3 setup.py sdist`

Install the package by running:
`sudo python3 setup.py install` or `sudo pip3 install .`


Check if functions works by e.g. writing `python3` to open a python shell and write:
```
>>> from assignment4.integrator import Integrator
>>> f = lambda x: x ** 2
>>> a,b,N = 0,1,100
>>> print (Integrator.integrate(f,a,b,N))
0.32835000000000003
```

Run tests to check the code. Read reportX.txt to check output of tests. 

### Note
Note that if there is any issues with the package itself, I would recommend doing it manually:
```>git clone URL
>cd INF3331-jonasksv/assignment4
>python setup.py build_ext --inplace
```
You should now be able to use the code as intended. Test by running the test scripts. ` python3 assignment4/test/test_integrator.py` 
