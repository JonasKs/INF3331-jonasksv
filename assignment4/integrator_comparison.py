from integrator import Integrator
from numpy_integrator import numpy_integrator
from numba_integrator import numba, numba_integrate
import cython_integrator
import matplotlib.pyplot as plt
import numpy as np


def test_integrator_comparison():
    f = lambda x: np.sin(x)
    F = lambda x: - np.cos(x)
    expected_answer = F(np.pi) - F(0)
    a, b, N = 0, np.pi, 129000 #Lowest N for normal integrate.
    a, b, B = 0, np.pi, 90700 #Lowest N for mid integrate.
    assert (Integrator.integrate(f, a, b, N)-expected_answer < 1E-10)
    assert (Integrator.midpoint_integrate(f, a, b, B) -expected_answer < 1E-10)

    assert (numpy_integrator.integrator(f, a, b, N) -expected_answer < 1E-10)
    assert (numpy_integrator.midpoint_integrator(f, a, b, B) -expected_answer < 1E-10)

    assert (abs(numba(f, a, b, N)-expected_answer) < 1E-10 )
    assert (abs(numba_integrate(f, a, b, B)-expected_answer) < 1E-10 )

    assert (abs(cython_integrator.integrate_g(a,b,N)-expected_answer < 1E-10))
    assert (abs(cython_integrator.cython_integrate_mid(a,b,B)-expected_answer < 1E-10))

    with open('report6.txt', 'a') as out:
        out.write("Lowest N for normal integrate is: {}.\n".format(N))
        out.write("Lowest N for mid integrate is: {}.\n".format(B)) #Printing result to report3.txt
test_integrator_comparison()
