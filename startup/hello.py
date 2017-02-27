#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello, welcome come to python3 world!') 

# test code 1
print('--------------\n')

friends = ['henson', 'david', 'jesong', 'colin', 'sherry', 'vernon']
friends.append('var')
friends.insert(2, 'stany')

print('ths friends value length is', len(friends))

for friendsName in friends: print(friendsName)

# test code 2
print('--------------\n')

a = list(range(101))
b = 0
c = list()
while b < len(a) - 1:
    b += 1
    if b % 2 == 0:
        continue
    c.append(a[b])
print(c, 'END')

c = list()
d = 'this is long long test case for print.'
for x in range(len(d)):
    c.append(d[x])
print('test result is:', c)
c.sort()
print('test sort reslut is:', c)

# test code 3
print('--------------\n')

dictCase = {}       # this is dict
dictCase['KEY1'] = 123
dictCase['KEY2'] = 234
dictCase['KEY1'] = 456
print(dictCase)
print(dictCase, dictCase.pop('KEY1'), dictCase.pop('KEY2'))

setCase = set([1, 2, 3, 4, 5]) # this is set
print(setCase)

setCase1 = set([1, 2, 3, 5, 6, 7, 8])
print(setCase & setCase1)
print(setCase | setCase1)

# test code 4
print('--------------\n')

def selfsum(start, end, func):
    total = 0
    for x in range(start, end + 1):
        total += func(x)
    return total

def xgma1(x):
    return x

def xgma2(x):
    return x ** 2 + 1

print('xgm1 1~100 is', selfsum(1, 100, xgma1))
print('xgm2 1~100 is', selfsum(1, 100, xgma2))
print('sum 1~100 is', sum(x for x in range(1, 101)))
print('sum2 1~100 is', sum(x ** 2 + 1 for x in range(1, 101)))

# test code 5
print('--------------\n')

import math

if not isinstance(dictCase, (int, float, str, set, list, tuple)) :
    print(TypeError('dictCase not is a instance in int, float, str, set, list, tuple'))

#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
def fact(n):
    if n == 1 :
        return 1
    return n * fact(n - 1)

print('fact(1) =', fact(1))
print('fact(5) =', fact(5))
print('fact(100) =', fact(100))

#汉诺塔
def move(n, a, b, c):
    if n != 0:
        move(n-1,a,c,b)
        print('%s --> %s' % (a, c))
        move(n-1,b,a,c)

move(3,'a','b','c')

#杨辉三角
def yangHui(x, cha = 1):
    print('Play YangHuiSanJiao Value is %d, ChaValue is %d' % (x, cha))
    for i in range(x):
        print(yangHuiLine(i + 1, cha))
    print('* * * END * * *')

def yangHuiLine(x, cha = 1):
    if x < 1:
        return

    if x == 1:
        return [1]

    if x > 1:
        result = [1]
        source = 1
        i = 1
        while i <= x - 1:
            source = chaSum(source, cha)
            result.append(source)
            i += 1
        while i < x * 2 - 1:
            source = chaSum(source, cha, -1)
            result.append(source)
            i += 1

        return result

def chaSum(source, cha = 1, d = 1):
    if d == 1:
        return source + cha
    else:
        return source - cha

yangHui(3)
yangHui(5)
yangHui(5, 2)