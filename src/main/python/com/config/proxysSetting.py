import re
from bs4 import BeautifulSoup as Soup
import requests

headers = [
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'},

]
def parse_items(items):
    # 存放ip信息字典的列表
    ips=[]
    timePattern = re.compile(r'.*天', re.MULTILINE | re.DOTALL)
    for item in items:
        tds = item.find_all('td')
        divs = item.find_all('div')
        # 从对应位置获取ip，端口，类型
        ip, port, _type, liveTime = tds[1].text, tds[2].text, tds[5].text, divs[0].text
        if (_type == "HTTP"):
            ipFind = re.findall(timePattern, liveTime)
            if (len(ipFind) > 0):
                proxy = "http://" + ip + ":" + port
                if (checkProxy(proxy) == 1):
                    ips.append(proxy)
                    print(ips)
    return ips


def checkProxy(proxy):
    url = "http://service.channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services&Ajax_CallBackMethod=GetSearchResult&Ajax_CrossDomain=1&Ajax_Request" \
          "Url=http%3A%2F%2Fsearch.mtime.com%2Fsearch%2F%3Fq%3D%25E8%2582%2596%25E7%2594%25B3%25E5%2585%258B%25E7%259A%2584%25E6%2595%2591%25E8%25B5%258E&t=201941822383676594" \
          "&Ajax_CallBackArgument0=%E8%82%96%E7%94%B3%E5%85%8B%E7%9A%84%E6%95%91%E8%B5%8E&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=290&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=1"
    response = requests.get(url, headers=headers[0], proxys={"http": proxy})
    if (response == 200):
        return 1
    else:
        return 0


# 获取ip代理
def getIpProxys(ips):
    ipurl = 'http://www.xicidaili.com/nn/'
    html = requests.get(url=ipurl, headers=headers[0]).text
    soup = Soup(html, 'lxml')
    items = soup.find_all('tr')[1:]
    ips = ips.append(parse_items(items))
    return ips
    # regip = r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>\s*?<td>(\d*)</td>\s*?<td>.*</td>\s*?<td>.*HTTP[^S]'
    # matcher = re.compile(regip)
    # ipstr = re.findall(matcher, html)
    # ip_list = []
    # for ipport in ipstr:
    #     print(ipport)
    #     ip_list.append("http://"+ipport[0] + ':' + ipport[1])
    # return ip_list

