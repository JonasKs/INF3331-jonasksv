from polynomials import Polynomial

def test_evaluate_polynomial():
    #Testing with normal numbers
    p = Polynomial([1, 2, 3]) #3x^2, 2x, 1 -> 3*2^2 = 3*4 + 2*2 + 1 = 17
    assert Polynomial.__call__(p,2) == 17
    #Testing with 0's only
    p1 = Polynomial([0, 0, 0])
    assert Polynomial.__call__(p1,2) == 0
    #Testing with numbers and ending with 0's
    p2 = Polynomial([5, 2, 3, 0, 0, 0])
    assert Polynomial.__call__(p2,2) == 21



def test_adding_polynomial(): #x = 2
    #Testing with different lenght and results
    p = Polynomial([1,2,3])
    q = Polynomial([5,6])
    assert Polynomial.__add__(p,q) == [6,8,3]
    #Opposite lenght
    a = Polynomial([1,2])
    b = Polynomial([2,1,0])
    assert Polynomial.__add__(a,b) == [3,3]

def test_sub_polynomial(): #x = 2
    #Testing with different lenghts
    p = Polynomial([5,6,3])
    q = Polynomial([4,3])
    assert Polynomial.__sub__(p,q) == [1,3,3]
    #Testing with different lenghts and negative answers
    a = Polynomial([3,1])
    b = Polynomial([4,1,0])
    assert Polynomial.__sub__(a,b) == [-1,0,]

def test_degree():
    #Assuming this is what you actually ment: Return the index of the highest nonzero coefficient.
    p = Polynomial([1,2,5,4])
    assert Polynomial.degree(p) == 3

    p = Polynomial([1])
    assert Polynomial.degree(p) == -1

def test_coefficients():
    #Get-function
    p = Polynomial([1,2,3,4])
    assert Polynomial.coefficients(p) == [1,2,3,4]

def test_eq():
    #Checking if they are the same.
    p = Polynomial([1,2,3,4])
    q = Polynomial([1,2,3,4])
    assert Polynomial.__eq__(p,q) == True

def test_repr():
    #Testing positive numbers
    p = Polynomial([10,11,-12,13,14,15]) # 4,3,2,1 -> 4x^3, 3x^2, 2x, 1
    assert Polynomial.__repr__(p) == "15x^5 + 14x^4 + 13x^3 - 12x^2 + 11x + 10"

    #Testing negative numbers
    p1 = Polynomial([-10,11,-12,13,14,-15]) # 4,3,2,1 -> 4x^3, 3x^2, 2x, 1
    assert Polynomial.__repr__(p1) == "- 15x^5 + 14x^4 + 13x^3 - 12x^2 + 11x - 10"

    #Testing if it actually removes 0's
    p1 = Polynomial([-10,11,-12,0,14,-15]) # 4,3,2,1 -> 4x^3, 3x^2, 2x, 1
    assert Polynomial.__repr__(p1) == "- 15x^5 + 14x^4 - 12x^2 + 11x - 10"

def test_mul():
    #Multiplies
    p = Polynomial([1,2,3])
    c = 2
    assert Polynomial.__mul__(p,c) == [2,4,6]


####TESTS####
test_evaluate_polynomial()
test_adding_polynomial()
test_sub_polynomial()
test_degree()
test_coefficients()
test_eq()
test_repr()
test_mul()
