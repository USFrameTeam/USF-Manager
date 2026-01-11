import json
import re
import os
import requests

class GetDownList:
    def getSource(self,numSource=None):# numSource 下载源编号,如不填写则默认使用一号下载源
        with open('config.json', 'r') as f: # 读取配置文件,获取默认下载源
            config = json.load(f)
            try:
                if int(numSource) == int(f"{config['downSource']}"):    
                   downSource = f"{config['downSource']}"
                else:
                    downSource = int(numSource)
            except:
                downSource = '1'
        with open('data/downSource.json', 'r') as f: # 读取下载源文件
            data = json.load(f)
            for item in data:
                if item['number'] == int(downSource):
                    return item
    
class GetFile:
    def __init__(self, savedir='../data/'):
        self.savedir = os.path(savedir)
 

    def getList(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'

        


data = GetDownList().getSource()
print(data)
