#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, welcome come to python3 class2!') 

# test code 1
print('--------------\n')

L1 = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L2 = list(range(100))

print(L1[:], L1[::], L1[::1], L1[::-1])
print(L1[:3], L1[1:3], L1[2:4], L1[2:])
print(L1[-1:], L1[-1:1], L1[-1:-1], L1[-1:-3])
print(L1[-2:], L1[-2:1], L1[-2:-1], L1[-2:-3])
print(L1[-3:], L1[-3:1], L1[-3:-1], L1[-3:-3], L1[-4:-1:-1])

print(L2[:10], L2[-10:], L2[:10:2], L2[-10::2], L2[::10])

print((0,1,2,3,4,5,6,7,8)[:4], 'INAMEISSIMER'[::2])

# test code 2
print('--------------\n')

from collections import Iterable
print(isinstance('abc', Iterable), isinstance([1,2,3], Iterable), isinstance(123, Iterable))
for index, value in enumerate(L1): print(index, value)

print([m + n + str(o) for m in 'ABC' for n in 'XYZ' for o in [1,2,3]])

import os
for d, dirname in enumerate(os.listdir('..')): print(d, dirname)
print([x.upper() for x in L1 if isinstance(x, str)])

# test code 3
print('--------------\n')

print(list(range(1, 99)))
print([x ** 2 for x in range(1,11) if x % 2 ==0])
for index in (x ** 2 for x in range(1,11) if x % 2 ==0) : print(index)