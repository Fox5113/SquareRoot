#!/bin/python3

import sys
from decimal import *

def sqrt(x):
    def sqrtIter(guess):
        if goodEnaugh(guess):
            return guess
        else:
            return sqrtIter(improve(guess))

    def improve(guess):
        return average(guess, x / guess)

    def average(x, y):
        return (x + y) / 2

    def goodEnaugh(guess):
        if(abs(guess ** 2 - x)< 0.001):
            return 1
        else:
            return 0

    return sqrtIter(1.0)


def sqroot(number, eps):
    if (number >= 0):

        a = float(number)
        x0 = 0
        x1 = a
        while abs(x0 - x1) > eps:
            x0 = x1
            x1 = 0.5 * (x1 + a / x1)
        return x1
    else:
        return "ValueError: math domain error"


if __name__ == '__main__':

    _sqrt =  input(">>>")
    #s = (2)

    #x = 1.0
    #while abs(x * x - s) > 0.000000001:
    #    x = (x * x + s) / 2. / x
    

    print(sqroot(_sqrt, 0.0000000000001))
    #print(sqroot(2,0.001))
    #print(Decimal(x))

    #print(sqrt(9))
