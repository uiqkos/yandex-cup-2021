from dmatrix import solve as solve_wrong
from main import solve as solve_true
from random import choice


wrong_tests = []
powers = [2**i for i in range(10)]

while len(wrong_tests) < 1:

    n, m = choice(powers), choice(powers)

    if solve_wrong(n, m) != solve_true(n, m):
        print(False)
        wrong_tests.append((n, m))

print(wrong_tests)
