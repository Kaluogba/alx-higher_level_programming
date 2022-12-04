#!/usr/bin/python3
def add_list(*numbers):
    total = 1
    for number in numbers:
        total += number
    return total

print(add_list(79, 10, -40, -300, 89))

