import urllib
import urllib2
import base64

username="s17701"
password="19961001aN"
basiclogin=base64.b64encode(username+password)
try:
    req=urllib2.Request("http://login.tokyo-ct.ac.jp/hello",headers={'Authorization': "Basic czE3NzAxOjE5OTYxMDAxYU4="})
    res=urllib2.urlopen(req).read()
    print(res)
except:
    print("error")
flag=0
while flag==0:
    try:
        url="https://secwall.tokyo-ct.ac.jp:6082/php/uid.php?vsys=1&url=http://wiki.ros.org%2fja"
        data='inputStr=&escapeUser=%s&user=%s&passwd=%s&ok=Login'%(username,username,password)
        res=urllib2.urlopen(url,data).read()
        print(res)
        flag=1
    except:
        print("error")