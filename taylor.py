from sympy import *
import numpy as np
import matplotlib.pyplot as plt


def taylor_series(func, x0, n):
    x = Symbol("x")
    result = func.subs(x, x0)
    for i in range(1, n + 1):
        result += diff(func, x, i).subs(x, x0) * ((x - x0) ** i) / (factorial(i))
    print(result)
    return result


def draw_graph(func, taylor_func):
    plt.style.use("seaborn-poster")
    plt.figure(figsize=(10, 6))
    x = Symbol("x")
    a = []
    b = []
    c = []

    for i in range(-50, 50, 1):
        y = func.subs(x, i)
        a.append(i)
        b.append(y)
        y = taylor_func.subs(x, i)
        c.append(y)
    plt.plot(a, b, label=("f(x)"))
    plt.plot(a, c, label=("Taylor"))

    plt.xlim(-50, 50)
    plt.ylim(-100, 100)
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    return


func = parse_expr(input("Įveskite funkciją\n"), locals())
x0 = input("Pasirinkite tašką, kurio aplinkoje išvesti Teiloro formulę\n")
n = input("Kiek kartų diferencijuojama funkcija?\n")
taylor_func = taylor_series(func, int(x0), int(n))
draw_graph(func, taylor_func)
