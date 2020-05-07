# Data Structures Exercises 1
# By Gabriel Smith

import math


def solve_quadratic(a, b, c):
    answer1 = ((-b + math.sqrt(b**2 - (4*a*c)))/(2*a))
    answer2 = ((-b - math.sqrt(b**2 - (4*a*c)))/(2*a))
    return((answer1, answer2))


def main():
    print(str(solve_quadratic(1, -3, 2)))
    print(str(solve_quadratic(1, 2, 1)))


if __name__ == "__main__":
    main()
