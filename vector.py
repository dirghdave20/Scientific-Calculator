import math


def add_vectors(a, b):
    return [a[i] + b[i] for i in range(len(a))]


def subtract_vectors(a, b):
    return [a[i] - b[i] for i in range(len(a))]


def dot_product(a, b):
    total = 0

    for i in range(len(a)):
        total = total + a[i] * b[i]

    return total


def magnitude(a):
    total = 0

    for value in a:
        total = total + value * value

    return math.sqrt(total)


def scalar_multiply(a, number):
    return [value * number for value in a]