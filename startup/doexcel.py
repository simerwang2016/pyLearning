#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import datetime
import sys
  
filename = "file/timesheet.xlsx"
bk = xlrd.open_workbook(filename)
shxrange = range(bk.nsheets)
print(str(shxrange))
try:
 	sh = bk.sheet_by_name("Sheet1")
except:
 	print("no sheet in %s named Sheet1" % filename)

#获取行列数
nrows, ncols = sh.nrows, sh.ncols
print ("nrows %d, ncols %d" % (nrows,ncols))

#获取万信号列表
wangxinname = set({})
for i in range(1, nrows):
	wangxinname.add(sh.cell(i, 3).value)
print(wangxinname)
  
#定义要分析数据类型
class employee():
	def __init__(self, username):
		wangxinname = username
		ztime = list()
		wtime = list()

	def setTime(self, z, w):
		ztime.extend()
		wtime.extend()

	def getTimeDifference(self, z, w, resultType = 'hour'):
		inz = datetime.datetime.strptime(z,  '%Y/%m/%d %H:%M')
		inw = datetime.datetime.strptime(z,  '%Y/%m/%d %H:%M')
		intimevalue = inw - inz
		if resultType == 'hour':
			return intimevalue.hours
		else:
			return intimevalue.minuters

	def getSumWorkTime(self, resultType = 'hour'):
		dTime = list()
		for x in range(ztime.len):
			dTime.append(self.getTimeDifference(ztime[x], wtime[x], resultType))
			
		return sum(dTime)

	def getAvrageWorkTime(self):
		return self.getSumWorkTime()/ztime.len
		
'''
row_list = []
for i in range(1, nrows):
 	row_data = sh.row_values(i)
 	row_list.append(row_data)

 result_list = []

 	#增加最大值,最小值,平均值
 	row_list.append()
 '''