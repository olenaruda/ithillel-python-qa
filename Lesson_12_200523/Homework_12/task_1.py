import argparse


def solve_quadratic_equation(a, b, c):
    try:
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            sqrt_discriminant = discriminant**0.5
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            return x1, x2
        elif discriminant == 0:
            x = -b / (2*a)
            return x, x
        else:
            return None
    except ZeroDivisionError:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculation of the quadratic equation')
    parser.add_argument('-a', type=float, default=0, help='This should be a parameter "a" for the quadratic equation')
    parser.add_argument('-b', type=float, required=True,
                        help='This should be a parameter "b" for the quadratic equation')
    parser.add_argument('-c', type=float, required=True,
                        help='This should be a parameter "c" for the quadratic equation')
    args = parser.parse_args()

    first_arg = args.a
    second_arg = args.b
    third_arg = args.c

    roots = solve_quadratic_equation(first_arg, second_arg, third_arg)
    if roots:
        print('Roots of the equation: x1 =', roots[0], ', x2 =', roots[1])
    else:
        print('There is no solution')


# python task_1.py -a=1 -b=2 -c=-3
# (venv) oruda@macbook-pro Homework_12 % python task_1.py -a=1 -b=2 -c=-3
# Roots of the equation: x1 = 1.0 , x2 = -3.0

# (venv) oruda@macbook-pro Homework_12 % python task_1.py -b=3 -c=4
# There is no solution
