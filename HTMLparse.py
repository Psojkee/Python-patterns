import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


url=input('Enter')
cnt=int(input('Enter'))
pos=int(input('Enter'))
html=urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup('a')
for i in range(cnt):
    q=tags[pos].get('href', None)
    print(tags[pos].contents[0])
    html=urlopen(q).read()
    soup=BeautifulSoup(html, "html.parser")
    tags = soup('a')




##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl

##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
#sum=0
#url=input('URL')
#html = urllib.request.urlopen(url).read()
#soup = BeautifulSoup(html,'html.parser')
#tags = soup('span')
#for tag in tags:
#    sum+=int(tag.contents[0])
#print(sum)
