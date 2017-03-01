#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' this is python3 class3 module '

__author__ = 'Simer Wang'

import sys
from PIL import Image

print('hello, welcome come to python3 class3!') 

# test code 1
print('--------------\n')
'''
imgPath = './img/'
im = Image.open(imgPath + 'test.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save(imgPath + 'thumb.jpg', 'JPEG')
'''
# test code 2
print('--------------\n')

class Student(object):
    """docstring for Student"""
    def __init__(self, arg):
        super(Student, self).__init__()
        self.arg = arg
        
    def print_score(self):
        print('%s: %s' % (self.arg[0], self.arg[1]))


class BigStudent(Student):
    def print_score(self):
        print('%s: %s, Level=%s' % (self.arg[0], self.arg[1], 1))  #scoreLevel(self.arg[1])

    def scoreLevel(x):
        if x >= 80 : 
            return 'A'
        elif x >= 60 : 
            return 'B'
        elif x >= 40 : 
            return 'C'
        else:
            return 'E'

students = [Student(('Simer', 89)),
            Student(('Vernor', 19)),
            Student(('Stany', 56)),
            Student(('Jesong', 88))]

for x in students : x.print_score()
lubuu = BigStudent(('Lubuu', 85))
lubuu.print_score()

