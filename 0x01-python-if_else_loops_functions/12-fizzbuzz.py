#!/usr/bin/python3

def fizzbuzz(num1, num2):
    for i in range(num1, num2):
        if i <= num2:
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz", end=" ")
            elif i % 3 == 0:
                print("Fizz", end=" ")
            elif i % 5 == 0:
                print("Buzz", end=" ")
            else:
                print("{:d}".format(i), end=" ")
