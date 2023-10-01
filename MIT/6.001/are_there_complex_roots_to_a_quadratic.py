#!/usr/bin/env python
import math

class Quadratic:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z
    def print(self):
        print(self.a, "* x^2 +", self.b, "x + ", self.c)

    def find_discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    # def find_roots(self):
    #     discriminant = self.find_discriminant()
    #     x_pos = ((- self.b + math.sqrt(discriminant)) / (2 * self.a))
    #     x_neg = ((- self.b - math.sqrt(discriminant)) / (2 * self.a))
    #     print(x_pos,"------", x_neg)

    def check_for_complex_roots(self):
        disc = self.find_discriminant()
        if disc < 0:
            print("There are no real roots.")
        elif disc > 0:
            print("The roots are real and unequal.")
        else:
            print("The roots are real and equal.")

def __main__():
    qe = Quadratic(-1,-1,-1)
    qe.check_for_complex_roots()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    __main__()
