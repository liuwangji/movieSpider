# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7

from urllib.parse import quote, unquote
import requests
import re
import random
import time

headers = [
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'},

]

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}


# 读取数据函数,返回list类型


def loadData(fileName):
    movies = []
    with open(fileName) as txtData:
        lines = txtData.readlines()
    for line in lines:
        lineData = line.strip().split(',')  # 去除空白和逗号“,”
        movies.append(lineData[1])  # 测试数据集
    return movies


if __name__ == '__main__':
    movieFileName = "/Users/umeng/bigdata/ml-latest-small/newMoviesSpark.csv"
    newMovieFileName = "/Users/umeng/bigdata/ml-latest-small/newMovies.csv"
    write = open(newMovieFileName, "w")
    # movies = loadData(movieFileName)
    imgPattern = re.compile(r'cover":"(.*?)"', re.MULTILINE | re.DOTALL)
    urlPattern = re.compile(r'movieUrl":"(.*?)"', re.MULTILINE | re.DOTALL)

    movie = "the Beloved Country Cry"

    if movie != "title":
        url1 = "http://service.channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services" \
               "&Ajax_CallBackMethod=GetSearchResult&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fsearch.mtime.com" \
               "%2Fsearch%2F%3Fq%3D{}%26t%3D1%26i%3D0%26c%3D290" \
               "&t=2019418083240085" \
               "&Ajax_CallBackArgument0={}&Ajax_CallBackArgument1=1&Ajax_CallBackArgument2=290&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=1"

        # print("url1" + unquote(url1,'utf-8',None))
        url = "http://service.channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services" \
              "&Ajax_CallBackMethod=GetSearchResult&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fsearch.mtime.com" \
              "%2Fsearch%2F%3Fq%3D%25E8%2582%2596%25E7%2594%25B3%25E5%2585%258B%25E7%259A%2584%25E6%2595%2591%25E8%25B5%258E" \
              "&t=201941619411174858" \
              "&Ajax_CallBackArgument0={}&Ajax_CallBackArgument1=0&Ajax_CallBackArgument2=290&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=1";
        response = requests.get(url.format(quote(movie)), headers=header, timeout=3000)
        imgFind = re.findall(imgPattern, response.content.decode('utf-8'))
        urlFind = re.findall(urlPattern, response.content.decode('utf-8'))
        print(response )
        print(len(imgFind))