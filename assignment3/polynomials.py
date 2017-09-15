from itertools import zip_longest


class Polynomial:

    def __init__(self, coefficients):
        """coefficients should be a list of numbers with
        the i-th element being the coefficient a_i."""
        #removing last 0's if there are any..Makes all tests actually pass.
        self.coefficients = coefficients
        while self.coefficients[-1] == 0:
            if len(self.coefficients) == 1:
                break
            else:
                self.coefficients.pop()

    def degree(self):
        """Return the index of the highest nonzero coefficient.
        If there is no nonzero coefficient, return -1."""
        if len(self.coefficients) == 1:
            return(-1)
        else:
            return(len(self.coefficients)-1)
    def coefficients(self):
        """Return the list of coefficients.
        The i-th element of the list should be a_i, meaning that the last
        element of the list is the coefficient of the highest degree term."""
        return self.coefficients

    def __call__(self, x):
        """Return the value of the polynomial evaluated at the number x"""
        value = 0
        first = 0
        indexvalue = 0
        for element in self.coefficients:
            if indexvalue == 0:
                first = element
            else:
                value += element * (x ** indexvalue)
            indexvalue+=1
        return (value+first)

    def __add__(self, p):
        """Return the polynomial which is the sum of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.
        If p is not an int or Polynomial, should raise ArithmeticError."""

        if isinstance(p,Polynomial) or p is int:
            asd = [x + y for x,y in zip_longest(self.coefficients,p.coefficients,fillvalue=0)]
            return(asd)
        else:
            raise ArithmeticError

    def __sub__(self, p):
        """Return the polynomial which is the difference of p and this polynomial
        Should assume p is Polynomial([p]) if p is int.

        If p is not an int or Polynomial, should raise ArithmeticError."""
        if isinstance(p,Polynomial) or p is int:
            asd = [x - y for x,y in zip_longest(self.coefficients,p.coefficients,fillvalue=0)]
            return(asd)
        else:
            raise ArithmeticError


    def __mul__(self, c):
        """Return the polynomial which is this polynomial multiplied by given integer.
        Should raise ArithmeticError if c is not an int."""
        if isinstance(c,int):
            d = [i * c for i in self.coefficients]
            return(d)
        else:
            raise ArithmeticError


    def __rmul__(self, c):
        """Return the polynomial which is this polynomial multiplied by some integer"""
        if isinstance(c,int):
            raise ArithmeticError
        else:
            d = [i * c for i in self.coefficients]
            return(d)

    def __repr__(self):
        """Return a nice string representation of polynomial.
        E.g.: x^6 - 5x^3 + 2x^2 + x - 1
        """
        #[1,2,3,4] ->
        string = ""
        if len(self.coefficients) == 0:
            raise ArithmeticError
        #for element in range(len(self.coefficients)):
        #    posisjon = len(self.coefficients)-element-1
        posisjon = len(self.coefficients)
        for i in reversed(self.coefficients):
            posisjon-=1
            if i == 0:
                string += ""
            elif posisjon == 1:
                if i < 0:
                    string += "- "+str(abs(i))+"x "
                else:
                    string += "+ "+str(i)+"x "
            elif posisjon == 0:
                if i < 0:
                    string += "- "+str(abs(i))
                else:
                    string += "+ "+str(i)
            elif posisjon == (len(self.coefficients)-1):
                if i > 0:
                    string += str(abs(i))+"x^"+str(posisjon)+" "
                else:
                    string += "- "+str(abs(i))+"x^"+str(posisjon)+" "
            else:
                if i < 0:
                    string += "- "+str(abs(i))+"x^"+str(posisjon)+" "
                else:
                    string += "+ "+str(i)+"x^"+str(posisjon)+" "
        return(string)


    def __eq__(self, p):
        """Check if two polynomials have the same coefficients."""
        if self.coefficients == p.coefficients:
            return(True)
        else: return(False)


def sample_usage():
    p = Polynomial([1, 2, 1]) # 1 + 2x + x^2
    q = Polynomial([9, 5, 0, 6]) # 9 + 5x + 6x^3


    print("The value of {} at {} is {}".format(p, 7, p(7)))

    print("The coefficients of {} are {}".format(p, p.coefficients()))


    print("\nAdding {} and {} yields {}".format(p, q, p+q))

    p, q, r = map(Polynomial,
                  [
                      [1, 0, 1], [0, 2, 0], [1, 2, 1]
                  ]
    )

    print("\nWill adding {} and {} be the same as {}? Answer: {}".format(
        p, q, r, p+q == r
    ))
    print("\nIs {} - {} the same as {}? Answer: {}".format(
        p, q, r, p-q == r
    ))
