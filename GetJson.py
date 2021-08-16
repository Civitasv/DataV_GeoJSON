import re
import requests
from bs4 import BeautifulStoneSoup as bs
import json
import os
import geopandas


def getLevel(code):
    if (code == '100000'):
        return ''
    elif (code[-4:] == '0000'):
        return 'province'
    elif (code[-2:] == '00'):
        return 'city'
    else:
        return 'county'


def save_text(areaCode, level, content, full=False):
    if (level == ''):
        with open('china/'+('geojson_full/' if full else 'geojson/') + areaCode + '_full.json' if full else '.json', 'w', encoding='utf-8') as f:
            f.write(content)
    elif(level == 'province'):
        with open('china/'+('geojson_full/province/' if full else 'geojson/province/') + areaCode + '_full.json' if full else '.json', 'w', encoding='utf-8') as f:
            f.write(content)
    elif (level == 'city'):
        with open('china/'+('geojson_full/city/' if full else 'geojson/city/') + areaCode + '_full.json' if full else '.json', 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        with open('china/'+('geojson_full/county/' if full else 'geojson/county/') + areaCode + '_full.json' if full else '.json', 'w', encoding='utf-8') as f:
            f.write(content)


def getJson(areaCode, full=False):
    if (full and getLevel(areaCode) == 'county'):
        return
    url = 'https://geo.datav.aliyun.com/areas_v2/bound/' + \
        str(areaCode) + ('_full.json' if full else '.json')
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://datav.aliyun.com',
        'Referer': 'http://datav.aliyun.com/tools/atlas/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    print("areaCode："+str(areaCode))
    with open('china/log.txt', 'w', encoding='utf-8') as f:
        try:
            r = requests.get(url=url, headers=headers)
            mapJson = r.text
            if('Error' in mapJson):
                return
            save_text(str(areaCode), getLevel(areaCode), mapJson, full)
        except:
            print(areaCode)
            f.write(areaCode)
            f.write("\r")
            return


def saveShapefile(code, full=False):
    level = getLevel(code)
    try:
        data = geopandas.read_file(
            'shp_full' if full else 'shp'+'map/city/' + str(code) + '.json')
        localPath = 'map/shp/'  # 用于存放生成的文件
        data.to_file(localPath+str(code)+".shp",
                     driver='ESRI Shapefile', encoding='utf-8')
        print("--保存成功，文件存放位置："+localPath)
    except Exception:
        print("--------JSON文件不存在，请检查后重试！----")
        pass


def getAllCodes():
    f = open("china/code/location.txt",
             encoding='UTF-8')               # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    ls = []
    while line:
        arr = line.split(',')
        ls.append(arr[0])
        line = f.readline()
    f.close()
    return ls


if __name__ == '__main__':
    getJson('100000', False)
    getJson('100000', True)
