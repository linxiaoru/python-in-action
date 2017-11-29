# -*- coding: utf-8 -*-
# 定义一个函数 quadratic(a, b, c)，接收三个参数，返回一元二次方程：
# ax^2 + bx + c = 0
# 的两个解
import math
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type')
    elif not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    elif not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    else:
        pass
    nx  = (-b + math.sqrt(power(b) - 4 * a * c)) / (2 * a)
    ny  = (-b - math.sqrt(power(b) - 4 * a * c)) / (2 * a)
    return nx, ny

def power(x):
    return x * x

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))