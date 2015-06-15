__author__ = 'PyBeaner'


# sample http response
"""
HTTP/1.1 200 OK
Date: Sun, 31 May 2009 17:14:04 GMT
Server: Apache
Last-Modified: Fri, 22 Aug 2008 04:28:16 GMT
ETag: "3075-ddc8d800"
Accept-Ranges: bytes
Content-Length: 12405
Cache-Control: max-age=31536000, public
Expires: Mon, 31 May 2010 17:14:04 GMT
Connection: close
Content-Type: image/jpeg
"""

# There are five important features which all http clients should support.

# Caching
# Cache-Control: max-age=31536000, public
# Expires: Mon, 31 May 2010 17:14:04 GMT
#

# Last-Modified checking
# If-Modified-Since(request headers)
# server return 304 status_code if Last-Modified>If-Modified-Since

import subprocess
print(subprocess.getoutput('curl -I -H "If-Modified-Since: Wed, 21 Jan 2004 19:51:30 GMT" http://img3.douban.com/view/dale-online/dale_ad/public/54251de27e804a9.jpg'))
"""
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
HTTP/1.0 304 Not Modified
Date: Wed, 10 Jun 2015 09:14:22 GMT
Content-Type: image/jpeg
Expires: Thu, 09 Jun 2016 08:46:13 GMT
Last-Modified: Wed, 21 Jan 2004 19:51:30 GMT
Cache-Control: max-age=31536000
Age: 1
X-Via: 1.0 lsh56:3 (Cdn Cache Server V2.0)
Connection: keep-alive
"""


# ETag Checking
# ETag: "3075-ddc8d800"


# Compression
# most common algorithms:gzip and deflate.


# Redirecting
# 302: temporarily redirect
# 301: permanently redirect


# important:
# Python¡¯s http libraries do not support those features, but httplib2 does.
#