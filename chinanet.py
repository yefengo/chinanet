import requests
import time

def isLogin():
    # 通过post百度获得网络状态
    url_test = "https://www.baidu.com/"
    try:
        login_code = requests.get(url_test, timeout=2).status_code
        if int(x=login_code) == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        print(time.ctime(), "未连接到chinanet！")
        return False
    except:
        return False


def Login():
    postdata = {
            'username': '8015472502',
            'password': '217083',
            'validateCode': '',
            'postfix': '@wlan.bj.chntel.com',
            'address': 'bj',
            'loginvalue': '1',
            'basePath': 'http://wlan.ct10000.com:80/portal/',
            'language': 'CN_SC',
            'longNameLength': '32',
            'NasType': 'Huawei',
            'NasName': 'BJ-DS-SR-1.M.ME60',
            'OrgURL': 'none',
            'isMobileRand': 'false',
            'isNeedValidateCode': 'false',
            'phone': '',
            'pwd_phone': '217083',
            'validateCode_phone': '',
            'otherUser': '8015472502',
            'address1': 'bj',
            'otherUserPwd': '217083',
            'validateCode_otherUser': '',
            'select2': '-Select Service Provider-',
        }
    url_login = "http://wlan.ct10000.com/portal/login4V2.do"
    print(time.ctime(), "正在尝试登录……")
    try:
        res = requests.post(url_login, data = postdata)
    except:
        pass    
    
def Logout():
    url_logout = "http://wlan.ct10000.com/portal/Logout.do?NasType=Huawei&NasName=BJ-DS-SR-1.M.ME60"
    try:
        res = requests.get(url_logout)
    except requests.exceptions.ConnectionError:
        print(time.ctime(), "logout, 未连接到Chinanet！")
        
if __name__ == '__main__':
    if isLogin():
        print(time.ctime(), "已经连接到网络。")
    while True:
        if not isLogin():
            Login()
            if isLogin():
                print(time.ctime(), "连接成功！")
            else:
                print(time.ctime(), "连接失败，将在5秒后重试……")

        time.sleep(5)