# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
def get_info(url):
    kugou_data = requests.get(url,headers = headers)
    kugou_top = BeautifulSoup(kugou_data.text,'lxml')
    Nums = kugou_top.select('span.pc_temp_num')
    authors = kugou_top.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    timelongs = kugou_top.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    
    for Num,author,timelong in zip(Nums,authors,timelongs):
        data={
        '排名：':Num.get_text().strip(),
        '歌手：':author.get_text().split('-')[0],
        '歌名：':author.get_text().split('-')[1],
        '歌长：':timelong.get_text().strip()
        }
        print(data)
        writer("酷狗top500.text",data)
        

def writer(path,data):
    write_flag = True
    with open(path,'a',encoding ='utf-8') as f:
        f.writelines(data)
        f.write('\n\n')
    
if __name__ == '__main__':

    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format (number) for number in range(1,24)]
    for single_url in urls:
        get_info(single_url)
        time.sleep(5)