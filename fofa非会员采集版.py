
from urllib import parse
import requests
import json
import base64

header={
    'Host': 'api.fofa.so',
    'Authorization': '',#抓包替换
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Origin': 'https://fofa.so',
    'Referer': 'https://fofa.so/',
}
f=open("fofa_fifth.txt","a",encoding='utf-8')       
o=open("edu.txt","r",encoding='utf-8')
for line in o.readlines():
    newline = "title=" + f'"{line.strip()}"'
    keyword3 = str(base64.b64encode(newline.encode('utf-8')), "utf-8")
    keyword2 = parse.quote(newline)
    uuurl='https://api.fofa.so/v1/search?q='+keyword2+'&qbase64='+keyword3+'&full=false&pn=4&ps=10' #修改页数 非会员前5页
    print(uuurl)
    req_fofa=requests.request("get",uuurl,headers=header)
    for i in range(1,10):
        try:
            data=json.loads(req_fofa.text)
            print(data)
            url=data["data"]["assets"][i]["link"]
            print(url)
            f.write(url+'\n')
        except:
            pass
            continue
f.close()