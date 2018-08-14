from vm import fibo


def test_1st_and_2nd_shouldbe_1():
    assert 1 == fibo(1)
    assert 1 == fibo(2)

def test_3rd_shouldbe_2():
    assert 2 == fibo(3)

def test_4th_shouldbe_3():
    assert 3 == fibo(4)
