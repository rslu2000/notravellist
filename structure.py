#!/usr/bin/env python
#_*_ coding: utf-8_*_
import time,requests,urllib2,json,re
from bs4 import BeautifulSoup
from lxml import etree
from collections import OrderedDict
import pandas as pd
import xlwt

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getPage(url):#获取链接中的网页内容
        request = urllib2.Request(url = url, headers = headers)
        response = urllib2.urlopen(request, timeout = 5)
        page = response.read().decode('utf-8')
        return page

def getList():
	place = raw_input('请输入想搜索的区域、类型(如北京、热门景点等)：')
	url = 'http://piao.qunar.com/ticket/list.htm?keyword='+ str(place) +'&region=&from=mpl_search_suggest&page={}'
	i = 1
	sightlist = []
	while i < 10:
		page = getPage(url.format(i))
		selector = etree.HTML(page)
		print '正在爬取第' + str(i) + '页景点信息'
		i+=1
		informations = selector.xpath('//div[@class="result_list"]/div')
		for inf in informations: #获取必要信息
                .....

	return sightlist,place

def listToExcel(list,name):
	df = pd.DataFrame(list,columns=['景点名称','级别','所在区域','起步价','销售量','热度','地址','标语','详情网址'])
	df.to_excel(name + '景点信息.xlsx')

def getBaiduGeo(sightlist,name):
	ak = 'UAedX6ygGjGzZ1n7g2vkn6XpLUxCKCNc'
	url = 'http://api.map.baidu.com/geocoder/v2/?address=' + address  + '&output=json&ak=' + ak
	json_data = requests.get(url = url).json()
	json_geo = json_data['result']['location']

def main():
	sightlist,place = getList()
	listToExcel(sightlist,place)
	getBaiduGeo(sightlist,place)

if __name__=='__main__':
	main()
