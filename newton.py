from sympy import *

zeros = []
points_of_interest = []


def get_funcs(exp_str: str):
    x = Symbol("x")
    func = parse_expr(exp_str, locals())
    deriv = diff(func, x)
    return [func, deriv]


def sgn(number):
    if number == 0:
        return 0
    elif number > 0:
        return 1
    else:
        return -1


def get_points_of_interest(func, limits):
    x = Symbol("x")
    for i in range(limits[0] + 1, limits[1]):
        sgn_one = sgn(func.subs(x, i - 1))
        sgn_two = sgn(func.subs(x, i))
        if sgn_one == 0:
            zeros.append(i - 1)
        elif sgn_two == 0:
            zeros.append(i)
        elif sgn_one != sgn_two:
            points_of_interest.append([i - 1, i])


def newtons_method(func, derivative, point, previous_value, accuracy):
    x = Symbol("x")
    value = point - func.subs(x, point) / derivative.subs(x, point)
    print(value)

    if previous_value is not None and round(value, accuracy) == round(
        previous_value, accuracy
    ):
        return round(value, accuracy)

    return newtons_method(func, derivative, value, value, accuracy)


[func, derivative] = get_funcs(input('Įveskite funkciją\n'))
get_points_of_interest(func, [-10, 10])
if len(points_of_interest) != 0:
    for i in range(0, len(points_of_interest)):
        print("\nKeičia ženklą taške:", points_of_interest[i][0])
        newtons_method(func, derivative, points_of_interest[i][0] + 0.3, None, 5)
else:
    print("\nThere are no points of interest")