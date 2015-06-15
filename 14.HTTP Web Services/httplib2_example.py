__author__ = 'PyBeaner'

import httplib2

httplib2.debuglevel = 1

# you should always create an httplib2.Http object with a directory name
h = httplib2.Http('.cache')
response, content = h.request('http://img3.douban.com/view/dale-online/dale_ad/public/54251de27e804a9.jpg')
print(response.status)
print(len(content))
print(response.fromcache) # the first time it's False;then it was cached,so fromcache is true
# 