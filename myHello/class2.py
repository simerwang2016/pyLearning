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

print([x ** 2 for x in range(1,11) if x % 2 ==0])
for index in (x ** 2 for x in range(1,11) if x % 2 ==0) : print(index)

def feb(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

print(feb(2))
print(feb(8))

def feb1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for x in feb1(8) : print(x)

def triangles(max):
    L = [1]
    n = 0
    while n < max:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]
        n += 1

for x in triangles(5): print(x)

# test code 4
print('--------------\n')

from math import sqrt

def testMath(list=[], *func):
    return [f(x) for x in list for f in func]

print(testMath([1,2,3,4], abs, sqrt))

def f(value):return value ** 2
print('test lambda:', list(map(lambda x:x*x,[1,2,3,4,-5])))

l1 = list(map(f, list(map(f,[1,2,3,4,-5]))))
print('test double map:', l1)

def normalize(x):
    return x[0:1].upper() + x.lower()[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# test code 5
print('--------------\n')

def notEmpty(x): return x and x.strip()
    
print(list(filter(notEmpty, ['A','SIMER','','  ', None,'  S  k  '])))

def is_palindrome(x): #利用filter()滤掉非回数
    return x == int(str(x)[::-1])

l = list(filter(is_palindrome, range(1, 1000)))
print(sorted(l, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def fn1(x): return x[0].upper()
def fn2(x): return x[1]
print('fn1=', sorted(L,key=fn1), '\nfn2=', sorted(L,key=fn2,reverse=True))

#test code 6

import functools

def log(logtext):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (logtext, func.__name__))
            return func(*args, **kw), print('%s is end.' % func.__name__)
        return wrapper  
    return decorator

@log('simer being execute')
def fn3(x): return x.lower()
print(fn3('This is Decorator Test'))

int2 = functools.partial(int, base = 2)
print('int2(10010)=', int2('10010'))

