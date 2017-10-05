import numpy as np
class numpy_integrator:
    def integrator(f, a, b, N):
        x = np.linspace(a, b, N)
        fx = f(x)
        area = np.sum(fx)*(b-a)/N
        return area
