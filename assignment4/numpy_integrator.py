import numpy as np
class numpy_integrator:
    def integrator(f, a, b, N):
        x = np.linspace(a, b, N)
        fx = f(x)
        area = np.sum(fx)*(b-a)/N
        return area

#####For testing in integrator_comparison.py
    def midpoint_integrator(f, a, b, N):
        h = float(b-a)/N
        x = np.linspace(a + h/2, b - h/2, N)
        fx = f(x)
        return h*sum(f(x))
