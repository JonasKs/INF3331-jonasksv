The reports have a short description of what I struggled with and the end result. (Everything should be working as intended)

The assignment4 folder have the python files, the test files are in assignment4/test


Build by running:
`python3 setup.py build_ext --inplace`

Make a package by running:
`python3 setup.py sdist`

Install the package by running:
`sudo python3 setup.py install`
(I have noticed on one ubuntu machine that the error:
`ValueError: 'assignment4/*.pyx' doesn't match any files` come when run. Open setup.py and comment out the line with the content:
`ext_modules=cythonize("assignment4/*.pyx")`  
Try again.
Please note that using cython_integrator functions does not work, if the .pyx file gives the error above. If something with my package don't work, I'd simply clone it.. Seems like it behaves differently on my debian and my ubuntu VM for some reason)
