import requests
import re
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject,Signal
import json

# 每一个爬虫任务
class SpiderTask(QObject):  
  
    def __init__(self,url,headers,proxies,user_url, parent=None):  
        super(SpiderTask, self).__init__(parent)  # 正确调用父类的构造函数 
        self.url = url
        self.user_url = user_url

        self.headers = headers
        self.proxies = proxies
        self.count = 20
        self.parmas = {
            'max_cursor':'0',
            'aid':'6383', #可能是某种应用或服务的标识符
            'sec_user_id':"", #作者本身的表示
            'count':self.count, #请求的数量。
            'publish_video_strategy_type':'2',
        }
        self.titles = []
        self.nikename = ''
        self.vedio_addrs = []
        self.get_media_url()

    user_urlChanged = Signal()


    def get_user_url(self):
        return self.user_url
    
    def set_user_url(self,user_url):
        if self.user_url == user_url:
            return
        self.user_url = user_url
        self.user_urlChanged.emit()

    #url格式是否正确
    def get_sec_user_id(self):
        sec_user_id = self.get_user_url().split('?',1)[0].rsplit('/',1)[1]
        self.parmas['sec_user_id'] = sec_user_id



    #获取主页或者视频的title和视频url
    def get_media_url(self):
        self.get_sec_user_id()
        
        resp = requests.get(url=self.url,headers=self.headers,proxies=self.proxies,params=self.parmas,stream=True)
        resp.encoding = 'utf-8'

        data = json.loads(resp.text) 
        self.nikename = data["aweme_list"][0]['author']['nickname']
        length = len(data["aweme_list"])
        for i in range(length):
            title = data["aweme_list"][i]['desc']
            self.titles.append(title)
            vedio_addr = data["aweme_list"][i]['video']['play_addr']['url_list'][0]
            self.vedio_addrs.append(vedio_addr)
        resp.close
        