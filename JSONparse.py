import json
import urllib.request, urllib.parse, urllib.error
serviceurl='http://py4e-data.dr-chuck.net/comments_792975.json'
data=urllib.request.urlopen(serviceurl).read()
info=json.loads(data)
cnt=0
for line in info['comments']:
    cnt+=int(line['count'])
print(cnt)
