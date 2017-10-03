import matplotlib.pyplot as plt
import numpy as np

class Integrator:
    def integrate(f, a, b, N):
        width = float(b-a)/N
        areal = float(0)
        for i in range(N):
            areal += f(a + i*width)
        return (areal * width)

    def plot_dat(f, a, b, N):
        n = np.linspace(a,b,N)
        plt.plot(n,f(n),color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Numerical approximation: Rectangular')
        for i in range(1,len(n)):
            c = n[i-1]
            d = n[i]
            plt.plot([c,c],[0,f((c+d)/2)],color='black')
            plt.plot([d,d],[0,f(d)],color='black')
            plt.plot([c,d],[f((c+d)/2),f((c+d)/2)],color='black')
        plt.savefig('quadratic_error.png') #Show is the "end of the plot", so this must be before we show the plot.
        plt.show()
        return 0

