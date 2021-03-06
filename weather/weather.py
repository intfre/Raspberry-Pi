#!/usr/bin/env python3
# -*- coding:utf-8  -*-
import requests
from bs4 import BeautifulSoup
import csv

def myAlign(string, length=0):
	if length == 0:
		return string
	slen = len(string)
	re = string
	if isinstance(string, str):
		placeholder = ' '
	else:
		placeholder = u'　'
	while slen < length:
		re += placeholder
		slen += 1
	return re

def get_content(url, data=None):
    rep = requests.get(url, timeout=60)
    rep.encoding = 'utf-8'
    return rep.text


def get_data(htmltext, city):
    content = []
    bs = BeautifulSoup(htmltext, "html.parser")
    body = bs.body
    data = body.find('div', {'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')
    for day in li:
        line = [city]
        date = day.find('h1').string
        line.append(date)
        text = day.find_all('p')
        line.append(text[0].string)
        if text[1].find('span') is None:
            temperature_H = '22℃'
        else:
            temperature_H = text[1].find('span').string.replace('℃', '℃')
        temperature_L = text[1].find('i').string.replace('℃', '℃')
        line.append(temperature_H)
        line.append(temperature_L)
#        print (myAlign(line[0],3),myAlign(line[1],3),myAlign(line[2],10),myAlign(line[3],5),myAlign(line[4],3))
        print (line[0].ljust(4),line[1].ljust(4),line[2].ljust(10),line[3].rjust(20),line[4].ljust(30))
        content.append(line)
#	print (line) 
    return content


def save_data(data, filename):
    with open(filename, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


def get_url(city_name):
    url = 'http://www.weather.com.cn/weather/'
    with open('city.txt', 'r', encoding='UTF-8') as fs:
        lines = fs.readlines()
        for line in lines:
            if(city_name in line):
                code = line.split('=')[0].strip()
                return url + code + '.shtml'
    raise ValueError('invalid city name')


if __name__ == '__main__':
#    cities = input('city name: ').split(' ')
    cities = ['西安']
    for city in cities:
        url = get_url(city)
        html = get_content(url)
        print ("url:%s\n"%(url))
        result = get_data(html, city)
#        save_data(result, 'weather.data')
