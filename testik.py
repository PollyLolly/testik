import pytest
import datetime

#pip install pytest
#pytest testik.py -r junitxml > result.txt
#pytest testik.py

max = datetime.datetime(2023, 4, 7, 23, 59)

def test1():
    start = datetime.datetime(2023, 4, 7, 4, 79)
    end = datetime.datetime(2023, 4, 7, 5, 0)
    assert end <= max

def test2():
    start = datetime.datetime(2023, 4, 7, 8, 0)
    end = datetime.datetime(2023, 4, 7, 14, 2)
    assert end <= max

def test3():
    start = datetime.datetime(2023, 4, 7, 8, 800, 2000)
    end = datetime.datetime(2023, 4, 7, 22, 0)
    assert end <= max

def test4():
    start = datetime.datetime(2023, 4, 7, 12, 40)
    end = datetime.datetime(2023, 4, 7, 13, 50)
    assert end <= max

def test5():
    start = datetime.datetime(2023, 4, 7, 14, 48)
    end = datetime.datetime(2023, 4, 8, 13, 23)
    assert end <= max

def test6():
    start = datetime.datetime(2023, 4, 7, 30, 48)
    end = datetime.datetime(2023, 4, 7, 4, 15)
    assert end <= max

def test7():
    start = datetime.datetime(2023, 4, 7, 0, 1, 15)
    end = datetime.datetime(2023, 4, 7, 0, 5, 22)
    assert end <= max

def test8():
    start = datetime.datetime(2023, 4, 7, 1, 15)
    end = datetime.datetime(2023, 4, 7, 5, 16)
    assert end <= max

def test9():
    start = datetime.datetime(2023, 4, 7, 1, 0)
    end = datetime.datetime(2023, 4, 7, 5, 0)
    assert end <= max

def test10():
    start = datetime.datetime(2023, 4, 7, 5, 22)
    end = datetime.datetime(2023, 4, 7, 13, 0)
    assert end <= max

def test11():
    start = datetime.datetime(2023, 4, 7, 15, 0)
    end = datetime.datetime(2023, 4, 7, 14002, 0)
    assert end <= max

def test12():
    start = datetime.datetime(2023, 4, 7, 2, 15, 16, 800, 420000000)
    end = datetime.datetime(2023, 4, 7, 5)
    assert end <= max

def test13():
    start = datetime.datetime(2023, 4, 7, 3/14, 1)
    end = datetime.datetime(2023, 4, 7, 0, 0)
    assert end <= max

def test14():
    start = datetime.datetime(2023, 4, 7, 2)
    end = datetime.datetime(2023, 4, 7, '3 енотов')
    assert end <= max

def test15():
    start = datetime.datetime(2023, 4, 7, 1, 0)
    end = datetime.datetime(2023, 4, 7, 2, 0)
    assert end <= max

def test16():
    start = datetime.datetime(2023, 4, 7, 10, 0)
    end = datetime.datetime(2023, 4, 7, 25, 0)
    assert end <= max

def test17():
    start = datetime.datetime(2023, 4, 7, 20, 24)
    end = datetime.datetime(2023, 4, 7, 20, 25)
    assert end <= max

def test18():
    start = datetime.datetime(2023, 4, 7, 15, 30)
    end = datetime.datetime(2023, 4, 7, 17, 30)
    assert end <= max

def test19():
    start = datetime.datetime(2023, 4, 7, 3, 30)
    end = datetime.datetime(2023, 4, 7, 5, 30)
    assert end <= max

def test20():
    start = datetime.datetime(2023, 4, 7, 3, 30)
    end = datetime.datetime(2023, 4, 7, 5, 30)
    assert end <= max

def test21():
    start = datetime.datetime(2023, 4, 7, 3, 0)
    end = datetime.datetime(2023, 4, 7, 5, 0)
    assert end <= max

def test22():
    start = datetime.datetime(2023, 4, 7, 12, 31)
    end = datetime.datetime(2023, 4, 7, 14, 22)
    assert end <= max

def test23():
    start = datetime.datetime(2023, 4, 7, 12, 0, 0)
    end = datetime.datetime(2023, 4, 7, 14, 0, 0)
    assert end <= max

def test24():
    start = datetime.datetime(2023, 4, 7, 21)
    end = datetime.datetime(2023, 4, 7, 21)
    assert end <= max

def test25():
    start = datetime.datetime(2023, 4, 7, 21)
    end = datetime.datetime(2023, 4, 8, 0)
    assert end <= max

def test26():
    start = datetime.datetime(2023, 4, 7, 12, 30)
    end = datetime.datetime(2023, 4, 7, 12, 30)
    assert end <= max

def test27():
    start = datetime.datetime(2023, 4, 7, 12, 30)
    end = datetime.datetime(2023, 4, 7, 12, 40)
    assert end <= max

def test28():
    start = datetime.datetime(2023, 4, 7, 21, 50)
    end = datetime.datetime(2023, 4, 8, 5)
    assert end <= max

def test29():
    start = datetime.datetime(2023, 4, 7, 17)
    end = datetime.datetime(2023, 4, 8, 15)
    assert end <= max

def test30():
    start = datetime.datetime(2023, 4, 7, 1, 30)
    end = datetime.datetime(2023, 4, 7, 1, 30)
    assert end <= max

def test31():
    start = datetime.datetime(2023, 4, 7, 26, 0)
    end = datetime.datetime(2023, 4, 7, 15, 0)
    assert end <= max

def test32():
    start = datetime.datetime(2023, 4, 7, 37, 0)
    end = datetime.datetime(2023, 4, 7, 45, 0)
    assert end <= max

def test33():
    start = datetime.datetime(2023, 4, 7, 14, 0)
    end = datetime.datetime(2023, 4, 8, 1, 0)
    assert end <= max

def test34():
    start = datetime.datetime(2023, 4, 7, 0, 3, 0, 3)
    end = datetime.datetime(2023, 4, 7, 10, 12)
    assert end <= max

def test35():
    start = datetime.datetime(2023, 4, 7, 16)
    end = datetime.datetime(2023, 4, 8, 12)
    assert end <= max

def test36():
    start = datetime.datetime(2023, 4, 7, 14)
    end = datetime.datetime(2023, 4, 8, 1)
    assert end <= max

def test37():
    start = datetime.datetime(2023, 4, 7, 2)
    end = datetime.datetime(2023, 4, 8, 1)
    assert end <= max

def test38():
    start = datetime.datetime(2023, 4, 7, 17)
    end = datetime.datetime(2023, 4, 8, 15)
    assert end <= max

def test39():
    start = datetime.datetime(2023, 4, 7, 5)
    end = datetime.datetime(2023, 4, 8, 3)
    assert end <= max

def test40():
    start = datetime.datetime(2023, 4, 7, 0)
    end = datetime.datetime(2023, 4, 7, 4)
    assert end <= max

def test41():
    start = datetime.datetime(2023, 4, 7, 18)
    end = datetime.datetime(2023, 4, 7, 20)
    assert end <= max

def test42():
    start = datetime.datetime(2023, 4, 7, 5, 30)
    end = datetime.datetime(2023, 4, 7, 5, 30)
    assert end <= max

def test43():
    start = datetime.datetime(2023, 4, 7, 5, 30)
    end = datetime.datetime(2023, 4, 7, 5, 40)
    assert end <= max

def test44():
    start = datetime.datetime(2023, 4, 7, 5, 30)
    end = datetime.datetime(2023, 4, 8, 5, 10)
    assert end <= max

def test45():
    start = datetime.datetime(2023, 4, 7, 2, 30)
    end = datetime.datetime(2023, 4, 7, 2, 50)
    assert end <= max

def test46():
    start = datetime.datetime(2023, 4, 7, 21, 50)
    end = datetime.datetime(2023, 4, 8, 5)
    assert end <= max

def test47():
    start = datetime.datetime(2023, 4, 7, '9 ночи вечера')
    end = datetime.datetime(2023, 4, 7)
    assert end <= max

def test48():
    start = datetime.datetime(2023, 4, 7, 21, 50)
    end = datetime.datetime(2023, 4, 8, 12)
    assert end <= max

def test49():
    start = datetime.datetime(2023, 4, 7, 23, 53)
    end = datetime.datetime(2023, 4, 8, 12)
    assert end <= max

def test50():
    start = datetime.datetime(2023, 4, 7, 12, 30)
    end = datetime.datetime(2023, 4, 7, 12, 50)
    assert end <= max

def test51():
    start = datetime.datetime(2023, 4, 7, 12, 30)
    end = datetime.datetime(2023, 4, 7, 12, 40)
    assert end <= max

def test52():
    start = datetime.datetime(2023, 4, 7, 12, 30)
    end = datetime.datetime(2023, 4, 7, 12, 30)
    assert end <= max

def test53():
    start = datetime.datetime(2023, 4, 7, 0, 0)
    end = datetime.datetime(2023, 4, 7, 4, 0)
    assert end <= max

def test54():
    start = datetime.datetime(2023, 4, 7, 9, 0)
    end = datetime.datetime(2023, 4, 8, 0, 0)
    assert end <= max

def test55():
    start = datetime.datetime(2023, 4, 7, 9, 0)
    end = datetime.datetime(2023, 4, 8, 0, 0)
    assert end <= max

def test56():
    start = datetime.datetime(2023, 4, 7, 5)
    end = datetime.datetime(2023, 4, 7, 16)
    assert end <= max

def test57():
    start = datetime.datetime(2023, 4, 7, 12, 53)
    end = datetime.datetime(2023, 4, 7, 21, 22)
    assert end <= max

def test58():
    start = datetime.datetime(2023, 4, 7, 0, 0)
    end = datetime.datetime(2023, 4, 7, 4, 0)
    assert end <= max

def test59():
    start = datetime.datetime(2023, 4, 7, 0, 0)
    end = datetime.datetime(2023, 4, 7, 4, 0)
    assert end <= max


def test60():
    start = datetime.datetime(2023, 4, 7, 0, 0, 0)
    end = datetime.datetime(2023, 4, 7, 4)
    assert end <= max


def test61():
    start = datetime.datetime(2023, 4, 7, 0)
    end = datetime.datetime(2023, 4, 7, 4)
    assert end <= max

def test62():
    start = datetime.datetime(2023, 4, 7, 14)
    end = datetime.datetime(2023, 4, 8, 3)
    assert end <= max

def test63():
    start = datetime.datetime(2023, 4, 7, 2)
    end = datetime.datetime(2023, 4, 7, 3)
    assert end <= max

def test64():
    start = datetime.datetime(2023, 4, 7, 14)
    end = datetime.datetime(2023, 4, 7, 15)
    assert end <= max

def test65():
    start = datetime.datetime(2023, 4, 7, 14, 5)
    end = datetime.datetime(2023, 4, 7, 16, 27)
    assert end <= max

def test66():
    start = datetime.datetime(2023, 4, 7, 2, 30)
    end = datetime.datetime(2023, 4, 7, 5, 17)
    assert end <= max

def test67():
    start = datetime.datetime(2023, 4, 7, 8)
    end = datetime.datetime(2023, 4, 7, 9)
    assert end <= max

def test68():
    start = datetime.datetime(2023, 4, 7, 1)
    end = datetime.datetime(2023, 4, 7, 1)
    assert end <= max


