# -*- coding: utf-8 -*-


# Бульбашкове сортування while
a = [1, 8, 7, 3, 5, 4]

for e in a:
    print e

k = 0
j = 1

while j < len(a):
    while k < (len(a)-1):
        if a[k] > a[k+1]:
            a[k], a[k+1] = a[k+1], a[k]
        k += 1
    j += 1
    k = 0

print a
