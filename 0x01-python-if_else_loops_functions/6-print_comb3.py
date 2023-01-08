#!/usr/bin/python3
for f1_number in range(0, 10):
    for f2_number in range(0, 10):
        if f1_number < f2_number:
            if f1_number < 8 and f2_number <= 9:
                print('{}{}'.format(f1_number, f2_number), end=", ")
            else:
                print('{}{}'.format(f1_number, f2_number))
