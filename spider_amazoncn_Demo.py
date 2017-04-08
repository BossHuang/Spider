__author__ = 'leihuang'
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"

# protend  a browser to spider pages
hd = {'User-Agent':'Chrome/56.0.2924.87'}
r = requests.get(url,headers = hd)

if r.status_code == 200:
    print r.text[0:1000]
else:
    print "some errer in get %s" %(url)

