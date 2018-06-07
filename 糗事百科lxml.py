import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,36)]

def re_scraper(url):
    res = requests.get(url,headers = headers)

    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
    sexs = re.findall('<div class="articleGender (.*?)">',res.text,re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments = re.findall('<i class="number">(\d+)</i> ÆÀÂÛ',res.text,re.S) 
    for id1,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
        info = {'id1':id1,
                'level':level,
                'sex':judgment_sex(sex),
                'content':content,
                'laugh':laugh,
                'comment':comment
                }
        return info

def bs_scraper(url):
    res = requests.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'lxml')
    ids = soup.select('div.author.clearfix > a> h2')
    contents = soup.select('a.contentHerf > div > span')
    laughts = soup.select(' div.stats > span.stats-vote > i')
    comments = soup.select('> i')
