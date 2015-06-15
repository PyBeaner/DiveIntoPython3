__author__ = 'PyBeaner'

import urllib.request

a_url = 'http://cn.bing.com/'
# data = urllib.request.urlopen(a_url).read()
# print(type(data)) # bytes
# print(data)

from http.client import HTTPConnection
HTTPConnection.debuglevel = 1
response = urllib.request.urlopen(a_url)
"""
send: b'GET / HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: cn.bing.com\r\nConnection: close\r\nUser-Agent: Python-urllib/3.2\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Cache-Control header: Content-Length header: Content-Type header: Vary header: Server header: P3P header: Set-Cookie header: Set-Cookie header: Set-Cookie header: Set-Cookie header: Set-Cookie header: X-MSEdge-Ref header: Set-Cookie header: Set-Cookie header: Set-Cookie header: Set-Cookie header: Date header: Connection
"""

# enable debuglevel when requesting
#User-Agent: Python-urllib/3.2 (Python-urllib/version)
# Accept-Encoding: identity(urllib.request does not support compression)

print(response.headers.as_string())
"""
Content-Length: 95665
Content-Type: text/html; charset=utf-8
Vary: Accept-Encoding
Server: Microsoft-IIS/8.5
P3P: CP="NON UNI COM NAV STA LOC CURa DEVa PSAa PSDa OUR IND"
Set-Cookie: _FS=NU=1; domain=.bing.com; path=/
Set-Cookie: _SS=SID=17646E8FD1B942D087617189340610BB; domain=.bing.com; path=/
Set-Cookie: SRCHD=AF=NOFORM; expires=Wed, 14-Jun-2017 11:47:34 GMT; domain=.bing.com; path=/
Set-Cookie: SRCHUID=V=2&GUID=A008406B64B540718CE2A0229798FC07; expires=Wed, 14-Jun-2017 11:47:34 GMT; path=/
Set-Cookie: SRCHUSR=AUTOREDIR=0&GEOVAR=&DOB=20150615; expires=Wed, 14-Jun-2017 11:47:34 GMT; domain=.bing.com; path=/
X-MSEdge-Ref: Ref A: 15D538A5AABD43E2BD1ABE30631D43C8 Ref B: 49340AA6B6038BD2634576AE8D2A1976 Ref C: Mon Jun 15 04:47:34 2015 PST
Set-Cookie: _EDGE_S=F=1&SID=2D1EEA7A29D2612F248FEDBD2873606A; path=/; httponly; domain=bing.com
Set-Cookie: _EDGE_V=1; path=/; httponly; expires=Wed, 14-Jun-2017 11:47:34 GMT; domain=bing.com
Set-Cookie: MUID=25D0DC8D9ED56B4E3733DB4A9F746ABE; path=/; expires=Wed, 14-Jun-2017 11:47:34 GMT; domain=bing.com
Set-Cookie: MUIDB=25D0DC8D9ED56B4E3733DB4A9F746ABE; path=/; httponly; expires=Wed, 14-Jun-2017 11:47:34 GMT
Date: Mon, 15 Jun 2015 11:47:34 GMT
Connection: close
"""

data = response.read()
print(len(data)) # 95665(not compressed)
# it's only 34977 bytes using browser(or clients support compression)

