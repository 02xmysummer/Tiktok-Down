import requests
import re
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QObject,Signal
import json

# 整个爬虫的管理类
class SpiderMgr(QObject):  
  
    def __init__(self, parent=None):  
        super(SpiderMgr, self).__init__(parent)  # 正确调用父类的构造函数 
        self.url = "https://www.douyin.com/aweme/v1/web/aweme/post/"
        self.user_url = ""

        self.headers = {
            'Cookie':'bd_ticket_guard_client_web_domain=2; d_ticket=baeb31a3db1fe3ec1339b4f7ca099e7384d0d; n_mh=ME6bkfEUXrDFkoQ55OjWhZ_hd3X8eioD8sgJoqWoXBk; LOGIN_STATUS=1; store-region=cn-cq; store-region-src=uid; live_use_vvc=%22false%22; my_rd=2; SEARCH_RESULT_LIST_TYPE=%22single%22; UIFID_TEMP=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c2cc7e51ca9ba1b8765e697f1e1e13925604f5605cc2b7e40fb90e64156746922d406335b1229f43a225b78b20ef76720e; fpk1=U2FsdGVkX1+flH4UaK+iYCpB11TemEcxGynYaTLW49MzvripLSHZAoboijdLm4hMRDSbmog+l7ESDlJw6OO5qw==; fpk2=f1f6b29a6cc1f79a0fea05b885aa33d0; UIFID=3c3e9d4a635845249e00419877a3730e2149197a63ddb1d8525033ea2b3354c2e86eb3a7075fc5e8708f21849e6a855fabaf43a77ebf265bc793e93d21fdc70402e69210fee0eff482481e8d528b5ab5a3e6a1bee65c275e80804d347043af438eb59148709a50f06a6cf07b1393ac50018fffa8bbd7bd837dcc2e3a368ce18b6b476ac1cf812b885594165faef320ba0682934f78d038dbb149274f434da8c8923c61c26190d9dbb44428182cc10521cd9a048d30dc9837c08ed423729ad508; xgplayer_device_id=18588662961; xgplayer_user_id=293288278505; hevc_supported=true; is_staff_user=false; passport_assist_user=CkGQnugH7B3nA-1cSuvgRKlZue5DQdGsqPL-mr9AlmGmwA6q5Nx952S0Vz4FmVdlZQLWglLYriybCLD5AcHANmxBvxpKCjzJBOAOht-2HLSEwM0x7NZfmLg495eLAt9R7mnmLA8EeUfsKKU9XAVJjmYk6yFbHfLHX8uQu8HyDZVXCEEQ_qvaDRiJr9ZUIAEiAQMRfRnd; uid_tt=a11061fc9db4a21bd889a16d81421593; uid_tt_ss=a11061fc9db4a21bd889a16d81421593; sid_tt=be098562a18d0b89f30cbc4983b82d22; sessionid=be098562a18d0b89f30cbc4983b82d22; sessionid_ss=be098562a18d0b89f30cbc4983b82d22; _bd_ticket_crypt_cookie=fb3cc88b11ecd17eb25ce9037a90bfac; dy_swidth=1536; dy_sheight=864; SelfTabRedDotControl=%5B%7B%22id%22%3A%226980977437903423518%22%2C%22u%22%3A124%2C%22c%22%3A124%7D%5D; sid_guard=be098562a18d0b89f30cbc4983b82d22%7C1728736420%7C5184000%7CWed%2C+11-Dec-2024+12%3A33%3A40+GMT; sid_ucp_v1=1.0.0-KDRmNGVjYWExMzJiZWYxM2FmZTE3OGExNGE1YTNjNDI2NzI4NGI2OGIKGwjQmuDXhPTnBRCk2am4BhjvMSAMOAVA-wdIBBoCbGYiIGJlMDk4NTYyYTE4ZDBiODlmMzBjYmM0OTgzYjgyZDIy; ssid_ucp_v1=1.0.0-KDRmNGVjYWExMzJiZWYxM2FmZTE3OGExNGE1YTNjNDI2NzI4NGI2OGIKGwjQmuDXhPTnBRCk2am4BhjvMSAMOAVA-wdIBBoCbGYiIGJlMDk4NTYyYTE4ZDBiODlmMzBjYmM0OTgzYjgyZDIy; publish_badge_show_info=%220%2C0%2C0%2C1729709539645%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=574d0f2af7cef638ab5ce69890758b6c; s_v_web_id=verify_m2oh1zk7_RaMX5QdW_6HEX_4Svu_9m8T_70QIIrWb8B7C; passport_csrf_token=fb62ac90adc657285bf083c757595230; passport_csrf_token_default=fb62ac90adc657285bf083c757595230; ttwid=1%7C6Re9BLSv7Xpn1I-f6cLW8W42qmv6yKWgTy7ra0kcjbQ%7C1729877545%7C241ec8e6ff1dcc4643ea3949ac586d490f6ab37f953b1045fc09e389ce111131; passport_fe_beating_status=true; FOLLOW_RED_POINT_INFO=%221%22; webcast_local_quality=origin; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.7%7D; __live_version__=%221.1.2.4540%22; webcast_leading_last_show_time=1730061381264; webcast_leading_total_show_times=2; live_can_add_dy_2_desktop=%221%22; download_guide=%220%2F%2F1%22; strategyABtestKey=%221730161376.996%22; biz_trace_id=e7fde2e7; pwa2=%220%7C0%7C3%7C1%22; __ac_signature=_02B4Z6wo00f01nqk4YQAAIDDpf8SydvBzSp6hOUAAPmYba; xg_device_score=7.773323026485472; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAHksfFzylMIQuEVM2eu8Xf0YK_1cK2jB7LYevDAZ9sey-yVv_1tAnRuLouGKM2t4K%2F1730217600000%2F0%2F1730174375582%2F0%22; WallpaperGuide=%7B%22showTime%22%3A0%2C%22closeTime%22%3A0%2C%22showCount%22%3A0%2C%22cursor1%22%3A126%2C%22cursor2%22%3A40%2C%22hoverTime%22%3A1730162991690%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAHksfFzylMIQuEVM2eu8Xf0YK_1cK2jB7LYevDAZ9sey-yVv_1tAnRuLouGKM2t4K%2F1730217600000%2F0%2F1730177105583%2F0%22; __ac_nonce=06720d8d400070c725e19; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1536%2C%5C%22screen_height%5C%22%3A864%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQ3U0eWRpSTg3TDZsb1NYS3lKVnRya3B6REc4Y1A3N0d1Q2lPVGJwTlU5cXVIR2hTVjNYTnczZ0dNZld6ZVYveXVPRGNzZDAyVTJqZVV0TDI3MXJaek09IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; IsDouyinActive=false; home_can_add_dy_2_desktop=%220%22; odin_tt=83f679ad456f6b429d6a1227efff3fe7bc8220c5843dd486608a72d1707edb6cfe142676cff02cd07cd6654ddb2b6581'
            ,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
            ,'Referer':self.user_url
        }
        self.proxies = {
            "http":"http://47.94.207.215:3128"
        }
        self.count = 20
        self.parmas = {
            'max_cursor':'0',
            'aid':'6383', #可能是某种应用或服务的标识符
            'sec_user_id':"", #作者本身的表示
            'count':self.count, #请求的数量。
            'publish_video_strategy_type':'2',
        }
        self.titles = []
        

    user_urlChanged = Signal()


    def get_user_url(self):
        return self.user_url
    
    def set_user_url(self,user_url):
        if self.user_url == user_url:
            return
        self.user_url = user_url
        self.user_urlChanged.emit()

    def get_sec_user_id(self):
        # 注意这里的+表示至少有一个字符，如果允许空ID则改为*?  
        pattern = r'^https://www\.douyin\.com/user/[A-Za-z0-9_-]+\?'  
        match = re.match(pattern, self.get_user_url())
        if match:
            sec_user_id = self.get_user_url().split('?',1)[0].rsplit('/',1)[1]
            self.parmas['sec_user_id'] = sec_user_id
            return True
        else:
            print("url地址解析失败")
            return False


    #获取主页或者视频的title和视频url
    def get_media_url(self):
        if not self.get_sec_user_id():
            return

        resp = requests.get(url=self.url,headers=self.headers,proxies=self.proxies,params=self.parmas,stream=True)
        resp.encoding = 'utf-8'

        data = json.loads(resp.text) 
        length = len(data["aweme_list"])
        for i in range(length):
            title = data["aweme_list"][i]['desc']
            # vedio_addr = data["aweme_list"][i]['video']['play_addr']['url_list'][0]
            print(title)
            # print(vedio_addr)
        # print(data["aweme_list"][0]['desc'])
        resp.close
        