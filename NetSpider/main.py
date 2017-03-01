#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib
import os

from collections import deque

def saveFile(data):
    print(data)
    '''
    save_path = 'D:\\temp.out'
    with open(save_path, 'a') as file : # wb 表示打开方式
        file.write(data)
    '''
queue = deque()
visited = set()

url = 'http://ffce.ffan.com/'  # 入口页面, 可以换成别的

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()  # 队首元素出队
    visited |= {url}  # 标记为已访问

    print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
    cnt += 1
    # 避免程序异常中止, 用try..catch处理异常
    try:
        req = urllib.request.Request(url, headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        urlop = urllib.request.urlopen(req)
        if 'html' not in urlop.getheader('Content-Type'):
            continue

        data = urlop.read().decode('utf-8')
        saveFile(data)
        #print(data)
    except SyntaxError as e:
        print("throw some error:" + e)
        continue

    # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'html' in x and x not in visited:
            inurl = x
            if 'http' not in x : inurl =  url + x
            print("inurl=:" + inurl)
            queue.append(inurl)
            print('加入队列 --->  ' + inurl)