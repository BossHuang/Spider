__author__ = 'leihuang'
import requests

# get relevant web pages by using baidu search engineer with keywords
# the interface: http://www.baidu.com/s?wd=keyword

keyword = 'deeplearning'
try:
    kv = {'wd':keyword}
    url = "http://www.baidu.com/s"
    r = requests.get(url, params=kv)
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print "some errer in search %s by baidu.com" %(keyword)

# another spider
try:
    url = "http://www.baidu.com/s?wd="
    r = requests.get(url+keyword)
    print r.request.url
    r.raise_for_status()
    print len(r.text)
except:
    print "some errer in search %s by baidu.com" %(keyword)