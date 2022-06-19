import requests
import pytest


@pytest.fixture()
def test_fix():
    print("\nthis is fixture")


def test_first(test_fix):
    print("\nthis is Not fixture")
    assert 10 == 10
    assert 12 == 12, "test failed"

    print("\nhellloo")
    print1()


def test_second(test_fix):
    print("\nthis is Not fixture")
    assert 10 == 10
    assert 12 == 12, "test failed"

    print("\nhellloo")
    print1()


def print1():
    a, b = 0, 2
    try:
        # open('123.txt', "r")
        print(b / a, a * b)
    except ZeroDivisionError as e:
        print("exception caught ")
    finally:
        print("Lets go home now")
