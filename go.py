#!/usr/bin/env python
#!coding=utf-8

import urllib2, re

ip = "{query}"
# ip = "112.112.112.1"
url = "http://www.baidu.com/s?wd="+ip

r = urllib2.urlopen(url)
raw = r.read()

info_list = re.findall('''<span class="c-gap-right">IP地址:&nbsp;(.*?)</span>(.*?)</td>''', raw)

if info_list:
    ip = info_list[0][0]
    location = info_list[0][1]
    print '''<?xml version="1.0"?><items><item arg="%s" valid="yes" ><title>Geo Info</title><subtitle>IP %s is from %s</subtitle><icon>ip.png</icon></item></items>''' % (ip, ip, location)
else:
    print '''<?xml version="1.0"?><items><item valid="yes" ><title>Geo Info</title><subtitle>The IP address is invalid or there is no geo info for it.</subtitle><icon>ip.png</icon></item></items>'''