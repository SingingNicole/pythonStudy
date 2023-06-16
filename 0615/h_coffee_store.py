#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[2]: 모든 지점(항상 페이지번호 맞춰줄 것)


import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd

def hollys_store(result):
    for page in range(1, 53):
        Hollys_url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=&gugun=&store="% page
        
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = bs(html, 'html.parser')
        
        tag_tbody = soupHollys.find("tbody")
        for store in tag_tbody.find_all('tr'):
            store_td = store.find_all('td')
            s_name = store_td[1].text
            s_sido = store_td[0].string
            s_address = store_td[3].string
            s_phone = store_td[5].string
            
            result.append([s_name, s_sido, s_address, s_phone])
            
    return

def main():
    result = []
    print("Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>")
    hollys_store(result)
    print(">>>")
    hollys_df = pd.DataFrame(result, columns=('store', 'si-do-gu', 'address',' phone'))
    hollys_df.to_csv('hollys.csv', encoding='cp949', mode='w', index=True)
    
if __name__ == '__main__':
    main()
    



# In[32]:


#!/usr/bin/env python
# coding: utf-8

# In[2]: 서울, 종로구 검색(항상 페이지번호 맞춰줄 것)


import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
from urllib import parse # url 인코더

def hollys_store(result, sido='', gugun=''):
    for page in range(1, 3):
        Hollys_url = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=%d&sido=%s&gugun=%s&store="% (page,sido,gugun) 
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = bs(html, 'html.parser')
        
        tag_tbody = soupHollys.find("tbody")
        for store in tag_tbody.find_all('tr'):
            store_td = store.find_all('td')
            s_name = store_td[1].text
            s_sido = store_td[0].string
            s_address = store_td[3].string
            s_phone = store_td[5].string
            
            result.append([s_name, s_sido, s_address, s_phone])
            
    return

def main():
    sido = input("검색할 시/도를 입력하세요 ")
    gugun = input("검색할 구군을 입력하세요 ")
    
    result = []
    print("Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>")
    hollys_store(result, parse.quote(sido), parse.quote(gugun))
    #parse.quote(str) : 단순 문자열을 url인코딩 처리함
    print(">>>")
    hollys_df = pd.DataFrame(result, columns=('store', 'si-do-gu', 'address',' phone'))
    hollys_df.to_csv(sido+gugun+'_hollys.csv', encoding='cp949', mode='w', index=True)
    
if __name__ == '__main__':
    main()
    

