__author__ = 'leihuang'
import requests
import time
import sys

# test the efficiency of requests

# 1.
# requests the same page
# with the request count increaseing, how the time will take
url = "https://www.baidu.com"
requestCount = []
requestTime = []
avgRequestTime = []
start = time.time()
for count in xrange(1,10001):
    requests.get(url)
    if count%100 == 0:
        now = time.time()
        requestCount.append(count)
        requestTime.append(now-start)
        avgRequestTime.append(requestTime[-1]*1.0/requestCount[-1])

print requestCount
print requestTime
print avgRequestTime

# 2.
# with requesting the different pages, how the time will take
urlSmall = "https://www.baidu.com"
urlMidium = "http://xiaodaoma.baijia.baidu.com/article/819314"
urlBig = "http://news.baidu.com"
urls = [urlSmall,urlMidium,urlBig]
# the size of page
for index in range(3):
    r = requests.get(urls[index])
    if r.status_code == 200:
        print "the size of %s in bytes is %s" %(urls[index], sys.getsizeof(r.text))
# the time spend
for index in range(3):
    begin = time.time()
    for count in range(100):
        requests.get(urls[index])
    print "%s spend %s" %(urls[index], time.time()-begin)
