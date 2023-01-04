#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = (number*(-1) % 10) * -1

initial_mssg = f'Last digit of {number} is {last_digit} and is'
if last_digit > 5:
    print(f'{initial_mssg} greater than 5')
elif last_digit == 0:
    print(f'{initial_mssg} 0')
elif last_digit < 6 and last_digit != 0 and number < 0:
    print(f'{initial_mssg} less than 6 and not 0')
