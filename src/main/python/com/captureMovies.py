from urllib.parse import quote
import requests
import re
import time
from com.headersSetting import getHeader

if __name__ == '__main__':
    # 输入文件
    movieFileName = "/Users/umeng/bigdata/ml-latest-small/newMoviesSpark.csv"
    # 输出文件
    newMovieFileName = "/Users/umeng/bigdata/ml-latest-small/newMovies.csv"
    write = open(newMovieFileName, "w")
    # 提取图片地址正则表达式
    imgPattern = re.compile(r'cover":"(.*?)"', re.MULTILINE | re.DOTALL)
    # 提取链接地址正则表达式
    urlPattern = re.compile(r'movieUrl":"(.*?)"', re.MULTILINE | re.DOTALL)
    # 打开输入文件
    with open(movieFileName, "r") as read:
        lines = read.readlines()
        count = 0
        for line in lines:
            # 去除空白,按逗号分割每行
            lineData = line.strip().split(',')
            # 取第二列电影名称
            movie = lineData[1]
            # 计数器 计算已爬取电影数量
            count = count + 1
            # 排除文件第一行的列信息
            if movie != "title":
                # 时光网url
                url = "http://service.channel.mtime.com/Search.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Channel.Services" \
                      "&Ajax_CallBackMethod=GetSearchResult&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fsearch.mtime.com" \
                      "%2Fsearch%2F%3Fq%3D%25E8%2582%2596%25E7%2594%25B3%25E5%2585%258B%25E7%259A%2584%25E6%2595%2591%25E8%25B5%258E" \
                      "&t=201941619411174858" \
                      "&Ajax_CallBackArgument0={}&Ajax_CallBackArgument1=1&Ajax_CallBackArgument2=290&Ajax_CallBackArgument3=0&Ajax_CallBackArgument4=1";
                # 对于异常情况下（如超时）的返回代码，循环访问直到返回正常结果
                try:
                    response = requests.get(url.format(quote(movie)), headers=getHeader())
                    print(response)
                except BaseException:
                    print(BaseException.__cause__)
                while response.status_code != 200:
                    try:
                        # response = requests.get(url.format(quote(movie)), headers=getHeader())
                        response = requests.get(url.format(quote(movie)), headers=getHeader())
                    except BaseException:
                        print(BaseException.__cause__)
                        print(response)
                # 根据正则找到对应的图片地址，电影链接
                imgFind = re.findall(imgPattern, response.content.decode('utf-8'))
                urlFind = re.findall(urlPattern, response.content.decode('utf-8'))
                # 若获取到图片地址，则写入对应列中
                if (len(imgFind) > 0 and len(urlFind) > 0):
                    record = line.strip() + "," + imgFind[0] + "," + urlFind[0] + "\n"
                    print(" count = " + str(count) + "  title  " + lineData[1] + "       record:  " + record)
                # 未获得图片地址的，在相应的列处补空
                else:
                    record = line.strip() + ",,\n"
                    print(" count = " + str(count) + "  title  " + lineData[1] + "       record:  " + record)
                    print(response)
                # 写入文件
                write.write(record)
                # 设置访问间隔为5秒
                time.sleep(5)
        read.close()
    write.close()
