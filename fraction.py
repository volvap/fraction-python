# python3
# coding: utf-8

import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction():
    def __init__(self, numerator, denominator):
        if gcd(numerator, denominator) == 1:
            self.numerator = numerator
            self.denominator = denominator
        else:
            self.numerator = numerator // gcd(numerator, denominator)
            self.denominator = denominator // gcd(numerator, denominator)

    def __add__(self, other):
        temp = Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)
        return temp

    def str_fraction(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __div__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        temp = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return temp.reduce_fraction()

    def reduce_fraction(self):
        if gcd(self.numerator, self.denominator) == 1:
            return self
        else:
            return Fraction(self.numerator // gcd(self.numerator, self.denominator),
                            self.denominator // gcd(self.numerator, self.denominator))

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)


if __name__ == '__main__':
    fraction1 = Fraction(4, 5)
    print((fraction1 + Fraction(1, 8)))

    print(Fraction(40, 70))

    print((Fraction(1, 6) + Fraction(1, 3)))

    fraction5 = Fraction(5, 7) / 10
    print(fraction5)

    print((Fraction(1, 2) + Fraction(3, 4) + Fraction(1, 9) * Fraction(3, 5)))
