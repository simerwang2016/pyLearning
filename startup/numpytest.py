#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
from numpy import *

v = arange(15).reshape(3, 5)

print(v)
print(type(v))
print(v.ndim)
print(v.shape)
print(v.size)
print(v.dtype)
print(v.data)
print('---------')
v = arange(2,20,5.5)
print(v)

print('---------')
z = zeros((3, 4))
o = ones((2, 4))
e = empty((2, 3))
print(z)
print(o)
print(e)

print('---------')
a1 = arange(10)
a2 = arange(5, 50, 5)
print(a1 ** 2)
print(a2 < 30)

print('---------')
a = array( [[1,1],
            [0,1]] )
b = array( [[2,0],
            [3,4]] )
print(b - a)
print(a * b)
print(dot(a,b))
a += b
print(a.sum())
print(a.max())
print(a.min())

print('---------')
print(arange(10000).reshape(100,100))


print('---------')
b = arange(12).reshape(3, 4)
print(b)
print(b.sum(axis = 0))
print(b.max(axis = 0))
print(b.sum(axis = 1))
print(b.min(axis = 1))
print('---------')
print(exp(b))
print(sqrt(b))
print(add(sin(b), cos(b)))
print('---------')

print(b)
print(b[1], b[2], b[0][1], b[0,1])
print(b[1][1:])
print(b[:,1])
print(b[1:,:])
print(b[1,...])

print('---------')
for v in b.flat:
	print(v)
print(b.shape)
print(b.ravel())
print('---------')

print(b)
b.resize((4,3))
print(b)

c = arange(12).reshape(4,3)
c += 100
d = c + 100
e = d + 100
print(c)
print(vstack((b,c)))
print(hstack((b,c,d,e)))