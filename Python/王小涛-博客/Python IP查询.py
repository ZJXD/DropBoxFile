import urllib.request as requests
import json

ip = '101.33.128.216'
key = '9cb9a1624edd4ae668d54ebbd7361628'

url = "http://a.apix.cn/tongyu/iplookup/ip?ip=" + ip

headers = {
    'accept': "application/json",  
    'content-type': "application/json",  
    'apix-key': key 
    }

req = requests.Request(url,headers = headers)
res = requests.urlopen(req).read().decode()
s = json.loads(res)['data']

print (s)
print (s['country'] + ' ' + s['province'] + '省' + s['city'] + '市 ' + s['operator'])
