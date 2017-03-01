#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class Athletelist(list):
    """docstring for Athletelist"""
    def __init__(self, a_name, a_dob = None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(set([self._sanitize(t) for t in a_times]))
        print("SELF CHECK:" + str(self))

    def _sanitize(self, time_string):
        if '-' in time_string:
            splitter = '-'
        elif ':' in time_string:
            splitter = ':'
        else:
            return time_string

        (one, two) = time_string.split(splitter)
        return  one + '.' + two 

    def top3(self):
        return sorted(self)[0:3]

def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            data_list = data.strip().split(',')
            print(data_list)
            return Athletelist(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as e:
        print("read file error:" + str(err))
        return none

def print_from_file(name):
    path = 'Data'
    nameAthletelist = get_coach_data(os.path.join(path, name + ".txt"))
    nameAthletelist.extend(['1.11','8.88','9.99'])
    print(nameAthletelist.name + r"'s faster times are:" + str(nameAthletelist.top3())) 

print_from_file('julie')
print_from_file('james')
print_from_file('mikey')
print_from_file('sally')
print_from_file('sarah')
print_from_file('vera')