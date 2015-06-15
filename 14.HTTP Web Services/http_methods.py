# coding=utf-8
__author__ = 'PyBeaner'
import httplib2
from urllib.parse import urlencode

data = {"status":"Test update from Python 3."}
print(urlencode(data))

h = httplib2.Http(".cache")

# add authentication:
# 401 Unauthorized status code if not authenticated
# add_credentials() method is the domain in which the credentials are valid. You should always specify this!
# If you leave out the domain and later reuse the httplib2.Http object on a different authenticated site,
# httplib2 might end up leaking one site’s username and password to the other site.
h.add_credentials("test","test","identi.ca")

resp,content = h.request("https://identi.ca/api/statuses/update.xml","GET",
                         urlencode(data),headers={'Content-Type': 'application/x-www-form-urlencoded'})
print(resp.items())
print(content)