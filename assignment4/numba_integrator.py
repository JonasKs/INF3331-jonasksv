from numba import jit

def numba(f, a, b, N):
    """Take a Python function as argument, and maybe call f(x) N times"""
    f_jit = jit("f8(f8)", nopython=True)(f) #Structure taken from piazza's teacher answer.

    @jit("f8(f8,f8,i8)", nopython=True) #changed from void to f8 from the teachers example on piazza.
    def integrate(a, b, N): #Passing in my own arguments like before, using the pure python method inside to see the difference.
        width = float(b-a)/N
        areal = float(0)
        for i in range(N):
            areal += f_jit(a + i*width)
        return (float(areal * width))
    return integrate(a, b, N)
