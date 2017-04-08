__author__ = 'leihuang'
import requests
url = "http://item.jd.com/11461683.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.text
except:
    print "some errers in get %s" %(url)