#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import sys
import urllib.request
import datetime
import time
import json

client_id = '0LHQM4VX_MQM6JfkXofa'
client_secret = 'OcPgqpswCg'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",client_id)
    req.add_header("X-Naver-Client-Secret",client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearch(node, srcText, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameter = "?query=%s&start=%s&display=%s"%(urllib.parse.quote(srcText),page_start,display)
    
    url = base + node + parameter
    
    responseDecode = getRequestUrl(url)
    
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')
    
    jsonResult.append({'cnt':cnt, 'title':title,'description':description, 
                       'org_link':org_link, 'link':link, 'pDate':pDate })
    
    returndef

def main():
    node = 'news'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []
    
    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse['total']
    
    while jsonResponse != None and jsonResponse['display'] != 0 :
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)
        
        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)
    
    print('%s 검색 : %d 건' %(node, total))
    
    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4,     )
        outfile.write(jsonFile)
    
    print("가져온 데이터 : %d 건" %(cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))


if __name__ == '__main__':    #임포트되지 않고 직접 실행하는 경우라면
    main()

