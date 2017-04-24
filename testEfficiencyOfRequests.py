__author__ = 'leihuang'
import requests
import time
import sys
import matplotlib.pyplot as plt

def calAvgAndSTD(numberList):
    '''
    calculate the average and standard devation of number list
    :param numberList:
    :return average, standard deviation
    '''
    # std = sqrt(Dx) = E(x^2)-(Ex)^2
    avg = 0.0
    size = len(numberList)
    squareAvg = 0.0
    for item in numberList:
        avg += item*1.0/size
        squareAvg += item*1.0/size*item
    return avg, squareAvg - avg*avg

# test the efficiency of requests

# 1.
# requests the same page
# with the request count increaseing, how the time will take
url = "https://www.baidu.com"
requestCount = []
requestTime = []
for count in xrange(1,10001):
    start = time.time()
    requests.get(url)
    now = time.time()
    requestCount.append(count)
    requestTime.append(now-start)

avg,std = calAvgAndSTD(requestTime)
print "avg:%s, std:%s" %(avg, std)

plt.title("request count and time ")
plt.xlabel("count")
plt.ylabel("time/s")
plt.scatter(requestCount,requestTime)
plt.show()

# 2.
# with requesting the different pages, how the time will take
urlSmall = "https://www.baidu.com"
urlMidium = "http://xiaodaoma.baijia.baidu.com/article/819314"
urlBig = "http://news.baidu.com"
urls = [urlSmall,urlMidium,urlBig]
# the size of page
urlSize = []
for index in range(3):
    r = requests.get(urls[index])
    if r.status_code == 200:
        size = sys.getsizeof(r.text)
        print "the size of %s in bytes is %s" %(urls[index], size)
        urlSize.append(size)
# the time spend
timeSize = []
for index in range(3):
    begin = time.time()
    for count in range(100):
        requests.get(urls[index])
    now = time.time()
    timeSize.append((now-begin)/100)
    print "%s spend %s" %(urls[index], now-begin)

plt.title("the size of page and request time")
plt.xlabel("size")
plt.ylabel("average time")
plt.scatter(urlSize,timeSize)
plt.show()






