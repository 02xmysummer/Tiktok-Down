import requests
import re
from PySide6.QtWidgets import QMainWindow,QMessageBox
from PySide6.QtCore import QObject,Signal
import json
import os
import aiohttp
import aiofiles
import asyncio
from custom_classes.spiderTask import SpiderTask
# 整个爬虫的管理类
class SpiderMgr(QObject):  
  
    def __init__(self,parent=None):  
        super(SpiderMgr, self).__init__(parent)  # 正确调用父类的构造函数 
        self.url = "https://www.douyin.com/aweme/v1/web/aweme/post/"

        self.tasks = []

    def set_configs(self,configs):
        self.configs = configs
        if self.configs['use_proxies']:
            self.proxies = {
                "http":f"http://{self.configs['proxies']['http']['ip']}:{self.configs['proxies']['http']['port']}"
            }
        else:
            self.proxies = {}
    #判断user_url是否正确
    def check_user_url(self,user_url):
        pattern = r'^https://www\.douyin\.com/user/[A-Za-z0-9_-]+\?'  
        match = re.match(pattern, user_url)
        return match

    #添加一个爬虫任务
    def addTask(self,user_url):
        res = self.check_user_url(user_url)
        if not res:
            print('链接解析失败')
            return False
        headers = {
            'Cookie':self.configs['cookies']
            # ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
            ,'User_Agent':self.configs['user_agent']
            ,'Referer':user_url
        }
        task = SpiderTask(url=self.url,headers=headers,proxies=self.proxies,user_url=user_url)
        self.tasks.append(task)
        return True

    #删除一个爬虫任务
    def delTask(self,task):
        self.tasks.remove(task)

    async def down_vedio(self,nikename,titles,vedio_addrs,indexs,user_url):
        headers = {
            'Cookie':self.configs['cookies']
            ,'User-Agent':self.configs['user_agent']
            ,'Referer':user_url
        }
        down_addr = self.configs['down_addr'].replace("\\", "\\\\")
        filepath = f'{down_addr}\\vedio\\{nikename}'
        if not os.path.exists(filepath) or not os.path.isdir(filepath):  
            os.makedirs(filepath)        
        tasks = []
        async with aiohttp.ClientSession() as session:
            for index in indexs:
                url = vedio_addrs[index]
                filename = titles[index]
                task = asyncio.create_task(self.download_vedio(session,url,headers,filepath,filename))
                tasks.append(task)
            await asyncio.wait(tasks)

        
    async def download_vedio(self,session,url,headers,filepath,filename):
        async with session.get(url,headers=headers) as resp: 
            async with aiofiles.open(f'{filepath}\\{filename}.mp4','wb') as f:
                await f.write(await resp.content.read())