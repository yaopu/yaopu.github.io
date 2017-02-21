#!/usr/bin/python
#-*- coding: utf-8 -*-
#baiduyun.py

import urllib,urllib.request
import webbrowser
import re
def yunpanSearch(key):
        keyword = key
        keyword = keyword.encode('utf-8')
        keyword = urllib.request.quote(keyword)
        url = "http://www.baidu.com" + keyword +"&wp=0&start=0"
        req = urllib.request.Request(url,hearders = {
            
        })
        opener = urllib.request.urlopen(req)
        html = opener.read().decode('utf-8')
        p = re.compile(r'https?://pan.baidu.com.*\?uk=[0-9]{0}.*[\d+?]"')
        source = p.findall(html)
        if source !='':
            print('\n 爬虫成功，连接如下：！\n')
            for i in source:
                print(i)





