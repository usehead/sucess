import requests
import json
import urllib
import re









#download
url2="http://dxx.ahyouth.org.cn/api/homeData"
hander2={
         'token':'MHNGlnRhBdZmTDfFr62goGunekJgEDPr',
         'Content-Length':'0',
         'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWeb         Kit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK         /20220204 Mobile Safari/537.36 MMWEBID/8828 MicroMessenger/8.0.20.2100(0x28001438         ) Process/toolsmp WeChat/arm32 Weixin Android Tablet NetType/WIFI Language/zh_CN          ABI/arm64',
         'Content-Type': 'application/json',
         'Accept': '*/*',
         'Origin': 'http://dxx.ahyouth.org.cn',
         'X-Requested-With': 'com.tencent.mm',
         'Referer': 'http://dxx.ahyouth.org.cn/index.html?t=1',
         'Accept-Encoding': 'gzip, deflate',
         'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'

        }
respose2=requests.post(url=url2,headers=hander2)
res1=respose2.text
print('download new lesson sucess')

#completing
q=re.findall(r'\bhttps\S*?html\b',res1)
wangzhi=q[0]
m = re.findall(r"\b\d+\b", res1)
shuzi=m[1]


#upload

url="http://dxx.ahyouth.org.cn/api/oldLearn"
header=   {
        'Content-Length':"9",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebK         it/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3262 MMWEBSDK/         20220204 Mobile Safari/537.36 MMWEBID/9433 MicroMessenger/8.0.20.2100(0x28001438)         Process/toolsmp WeChat/arm32 Weixin Android Tablet NetType/WIFI Language/zh_CN AB         I/arm64',
         'token':'DFhRZQrCAbehEWlbqXwqjunWzJb1OjJe',
        'Content-Type':"application/json",
        'Accept':'*/*',
        'Origin':"http://dxx.ahyouth.org.cn",
        'X-Requested-With':'com.tencent.mm',
        "Referer":"http://dxx.ahyouth.org.cn/",
        'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie':'PHPSESSID=439fed1b2e3414cfe02ed7565324c6eb',
        'Connection':'close',}
        
data=json.dumps({"id":shuzi})
for i in range(10):
 respose=requests.post(url=url,headers=header,data=data)
 print(respose.text)
print('upload data sucess')
#downloadtupan

img_url='https://h5.cyol.com//special//daxuexi//du1nj1a7sg//images/end.jpg'
try:
                    pic = requests.get(url=img_url)
                    local_lujin = '/home/ofsure/sucess'
                    f=open(local_lujin ,"wb")
                    f.write(pic.content)
                    f.close()
                    print("loading picture sucess")
                       
except requests.exceptions.ConnectionError:
                    print('loading faile ')
                                

