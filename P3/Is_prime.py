import sys
import nose.tools as nt
def is_prime(n):
    """Checks if n is prime. n must be an integer"""
    if not isinstance(n, int):
        raise ValueError("Argument must be integer")

    if n <= 1: return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def test_is_prime():
    nt.assert_equal(is_prime(2),True)
    nt.assert_equal(is_prime(11),True)

    nt.assert_equal(is_prime(1),False)
    nt.assert_equal(is_prime(-1),False)
    nt.assert_equal(is_prime(10),False)

@nt.raises(ValueError)
def test_string():
    is_prime("10")

@nt.raises(ValueError)
def test_float():
    is_prime(10.)
