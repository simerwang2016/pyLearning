#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (one, two) = time_string.split(splitter)
    return  one + '.' + two 

def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            data_list = data.strip().split(',')
            print(data_list)
            return {'Name':data_list.pop(0),
                     'DOB':data_list.pop(0),
                     'Time':str(sorted(set([sanitize(t) for t in data_list]))[0:3])}
    except IOError as e:
        print("read file error:" + str(err))
        return none

def print_from_file(name):
    path = 'Data'
    name_data = get_coach_data(os.path.join(path, name + ".txt"))
    print(name_data['Name'] + r"'s faster times are:" + name_data['Time'])  

print_from_file('julie')
print_from_file('james')
print_from_file('mikey')
print_from_file('sally')
print_from_file('sarah')
print_from_file('vera')
