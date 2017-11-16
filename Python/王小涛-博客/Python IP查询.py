import urllib.request as requests
import json

ip = '221.2.2.15'
key = '9cb9a1624edd4ae668d54ebbd7361628'

url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip=" + ip

headers = {
    'accept': "application/json",  
    'content-type': "application/json",  
    'apix-key': key 
    }

req = requests.Request(url,headers = headers)
res = requests.urlopen(req).read().decode()
res = res[20:len(res)-1]
s = json.loads(res)

print (s)
print (s['country'] + ' ' + s['province'] + '省 ' + s['city'] + '市 ' + s['district'])
