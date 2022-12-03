#!/usr/bin/python3
def magic_calculation(a, b, c):
    while a < b:
        return c
    while b > c:
        return a + b
    return(a * b - c)

import dis
dis.dis(magic_calculation)
