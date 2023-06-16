#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup

def CoffeeBean_store(result):
    CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()
    
    for i in range(1, 300):
        wd.get(CoffeeBean_URL)
        time.sleep(1) # 웹페이지 연결할 동안 1초 대기
        
        try:
            wd.execute_script("storePop2(%d)" % i)
            time.sleep(1)
            
            html = wd.page_source
            
            soupCB = BeautifulSoup(html, 'html.parser')
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            print(store_name)
            
            store_info = soupCB.select("div.store_txt > table > tbody > tr > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].text
            
            result.append([store_name, store_address,store_phone])
        except:
            continue
    return

def main():
    result = []
    print('CoffeeBean crawling >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    
    CoffeeBean_store(result)
    print(">>>")
    
    cb_df = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    cb_df.to_csv("CoffeeBean_store.csv", encoding='cp949', mode='w', index=True)
    
if __name__ == '__main__':
    main()

