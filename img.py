# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 05:40:25 2021

@author: asus
"""
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import os

def get_image():
    store=[]
    quote_page = 'https://wantubizhi.com/pic/%E8%A2%81%E4%B8%80%E7%90%A6%E5%9B%BE%E7%89%87%E9%AB%98%E6%B8%85/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=quote_page, headers=headers)
    data =urllib.request.urlopen(req).read()
    soup = BeautifulSoup(data, 'html.parser')
    content = soup.find_all('img',class_='lazyload')
    for i in content:
        store.append(i['data-src'])
    
    return store



   
        
def run_download(array):
    path =input('目錄建立:')
    if not os.path.isdir(path):
        os.mkdir(path)
        print('已建立目錄開始下載圖片')
        for i in range(len(array)):
            with open(path +'/' + str(i) +'.jpg' , 'wb') as f:
                f.write(urllib.request.urlopen(array[i]).read())
        print('下載完成')
      
    else:
        print('目錄已存在')
   
    
    
    

if __name__ == '__main__':
    get = get_image()
    run_download(get)