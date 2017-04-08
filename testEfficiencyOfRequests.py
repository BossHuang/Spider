__author__ = 'leihuang'
import requests
import time
import matplotlib.pyplot as plt

# test the efficiency of requests

url = "https://www.baidu.com"
requestCount = []
requestTime = []
avgRequestTime = []
start = time.time()
for i in xrange(1,10001):
    requests.get(url)
    if i%100 == 0:
        now = time.time()
        requestCount.append(i)
        requestTime.append(now-start)
        avgRequestTime.append(requestTime[-1]*1.0/requestCount[-1])

plt.scatter(requestCount,requestTime)
plt.show()
print requestCount
print requestTime
print avgRequestTime
plt.scatter(requestCount,avgRequestTime)
plt.show()