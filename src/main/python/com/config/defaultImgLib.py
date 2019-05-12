import random

img_list = [
    "http://img31.mtime.cn/mt/2014/02/23/022326.14558340_96X128.jpg",
    "http://img5.mtime.cn/mt/2019/03/20/135500.29577024_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/22/225854.10630971_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/22/231843.50107097_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/23/031930.57004148_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/23/001447.60947401_96X128.jpg",
    "http://img5.mtime.cn/mt/2019/03/20/135500.29577024_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/22/225212.84162134_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/23/011714.79302869_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/22/230311.40465578_96X128.jpg",
    "http://img21.mtime.cn/mt/2011/05/17/172910.95395807_96X128.jpg",
    "http://img5.mtime.cn/mt/2017/09/14/161300.20797275_96X128.jpg",
    "http://img31.mtime.cn/mt/2014/02/23/070027.65991754_96X128.jpg"
]
def getImg():
    return random.choice(img_list)
