#!/usr/bin/python3
for i in range(90):
    if i < 88:
        a = i // 10
        b = i % 10
        if a < b:
            print('{}{}'.format(a, b), end=', ')
print('{}'.format(i))
