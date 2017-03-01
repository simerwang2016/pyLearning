#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3
from athletelist import Athletelist

connection = sqlite3.connect('coachdata.sqlite')
cursor = connection.cursor()

#CREATE TABLE
try:
    cursor.executescript("""
        CREATE TABLE athletes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    dob DATE NOT NULL);
                        """)

    cursor.executescript("""
           CREATE TABLE timing_data(
                      athlete_id INTEGER NOT NULL,
                      value TEXT NOT NULL,
                      FOREIGN KEY (athlete_id) REFERENCES athletes)
                      """)
    connection.commit()
except Exception as e:
    print("create table error:" + str(e))
    print("delete table data...")
    cursor.execute("DELETE FROM timing_data")
    cursor.execute("DELETE FROM athletes")
    print("delete table data success.")

#GET DATA
def get_coach_data(filename):
    try:
        with open(filename) as file:
            data = file.readline()
            data_list = data.strip().split(',')
            #print(data_list)
            return Athletelist(data_list.pop(0), data_list.pop(0), data_list)
    except IOError as e:
        print("read file error:" + str(err))
        return None

def getdata_from_file(name):
    path = 'Data'
    nameAthletelist = get_coach_data(os.path.join(path, name + ".txt"))
    return nameAthletelist

athletes = []
athletes.extend([getdata_from_file('julie'), 
    getdata_from_file('james'),
    getdata_from_file('mikey'),
    getdata_from_file('sally'),
    getdata_from_file('sarah'),
    getdata_from_file('vera')]
    )

#INSERT DATA
try:
    for athletelist in athletes:
        name = athletelist.name
        dob  = athletelist.dob
        cursor.execute("INSERT INTO athletes (name,dob) VALUES (?,?)",(name,dob))
        cursor.execute("SELECT id from athletes WHERE name=? AND dob=?",(name,dob))
        the_current_id = cursor.fetchone()[0]
        for each_time in athletelist:
            cursor.execute("INSERT INTO timing_data (athlete_id,value) VALUES (?,?)",
                                    (the_current_id, each_time)) 
        connection.commit()
except Exception as e:
    print("insert table error:" + str(e))

#CHECK DATA
try:
    print("begin check data ...")
    cursor.execute("SELECT * from athletes")
    print("table athletes valus is:")
    print(cursor.fetchall())
    cursor.execute("SELECT * from timing_data")
    print("table timing_data valus is:")
    print(cursor.fetchall())
except Exception as e:
    print("check data error:" + str(e))

connection.close()