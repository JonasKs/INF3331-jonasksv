from integrator import Integrator
from numpy_integrator import numpy_integrator
from numba_integrator import numba
import matplotlib.pyplot as plt
import numpy as np
import time

def test_integral_of_constant_function():
    """ Integral of f(x) = 2. From 0 to 1 with 100k steps """
    f = lambda x: 2
    F = lambda x: 2 * x
    expected_answer = F(1) - F(0)
    a, b, N = 0, 1, 100000
    assert abs(Integrator.integrate(f, a, b, N) - expected_answer) < 1E-11

def test_integral_of_linear_function():
    """Integral of f(x) = 2x from 0 to 1 with 1m steps"""
    f = lambda x: 2 * x
    F = lambda x: 2 * x ** 2 / 2
    expected_answer = F(1) - F(0)
    a, b, N = 0, 1, 1000000
    assert abs(Integrator.integrate(f, a, b, N) - expected_answer) < 1E-5


def test_integral_task_4_2():
    """approximate the integral of f(x) = x2 from 0 to 1 with 100k steps"""
    f = lambda x: x ** 2
    F = lambda x: x ** 3 / 3
    expected_answer = F(1) - F(0)
    a, b, N = 0, 1, 100000000
    ###Comparing the selfmade "pure" version with the Numpy one###
    t0 = time.clock()
    assert abs(Integrator.integrate(f, a, b, N) - expected_answer) < 1E-5 #Normal integrate function
    t1 = time.clock()
    t2 = time.clock()
    assert abs(numpy_integrator.integrator(f, a, b, N) - expected_answer) < 1E-5 #Numpy integrate function
    t3 = time.clock()
    t6 = time.clock()
    assert abs(numba(f, a, b, N) - expected_answer) < 1E-5 #Numba integrate function
    t7 = time.clock()
    with open('report3.txt', 'a') as out:
        out.write("N is: {}\nPure function time: {}\n".format(N,(t1-t0))) #Printing result to report3.txt
        out.write("Numpy function time: {}\n".format(t3-t2)) #Printing result to report3.txt
        out.write("Numba function time: {}\n".format(t7-t6)) #Printing result to report3.txt
def test_create_plot():
    """Just creating the plot"""
    f = lambda x: x ** 3 / 3
    a, b, N = 0, 1, 10
    Integrator.plot_dat(f,a,b,N)

test_integral_of_constant_function()
test_integral_of_linear_function()
test_integral_task_4_2()
#test_create_plot()
