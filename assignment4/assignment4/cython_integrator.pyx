from libc.math cimport sin

cdef double f(double x):
    return (x**2)


cpdef double integrate_f(double a, double b, int N):
    cdef double s=0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):
        s += f(a+i*dx)
    return(s*dx)


cdef double midf(double x):
    return (sin(x))

cpdef cython_integrate_mid(double a, double b, int N):
    cdef double h = (b-a)/N
    cdef double result = 0
    cdef double tall = 2
    cdef int i
    for i in range(N):
        result += midf((a + h/tall) + i * h)
    result *= h
    return (result)

cpdef double integrate_g(double a, double b, int N):
    cdef double s=0
    cdef double dx = (b-a)/N
    cdef int i
    for i in range(N):
        s += midf(a+i*dx)
    return(s*dx)
