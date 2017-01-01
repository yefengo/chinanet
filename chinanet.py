# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
#from __future__ import unicode_literals
import requests
import time
import os.path
import sys
from subprocess import Popen


def isLogin():
    # 通过post百度获得网络状态
    url_test = "https://www.baidu.com/"
    try:
        islogin_code = requests.get(url_test, timeout=5).status_code
    except requests.exceptions.ConnectionError:
        print(time.ctime(), u"未连接到chinanet！")
        return False
    except:
        return False

    if int(islogin_code) == 200:
            return True
    else:
        return False

#os.path.exists(file_path)
def getAccount():
    file_name = 'account.ini'
    app_path = sys.path[0]
    file_path = os.path.join(os.path.abspath(app_path), file_name)
    if not os.path.exists(file_path):
        account = input(u"请输入chinanet帐号 > ")
        passwd = input(u"请输入chinanet密码 > ")
        su_passwd = input(u"请输入sudo密码 > ")
        with open(file_path, "w") as f:
            f.write("acount: %s\n" % account)
            f.write("passwd: %s\n" % passwd)
            f.write("su_passwd: %s\n" % su_passwd)
    else:
        with open(file_path, 'r') as f:
            account = f.readline().split(':')[-1].strip()
            passwd = f.readline().split(':')[-1].strip()
            su_passwd = f.readline().split(':')[-1].strip()

    return account, passwd, su_passwd


def Login(account, passwd):
    postdata = {
            'username': account,
            'password': passwd,
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
            'pwd_phone': passwd,
            'validateCode_phone': '',
            'otherUser': account,
            'address1': 'bj',
            'otherUserPwd': passwd,
            'validateCode_otherUser': '',
            'select2': '-Select Service Provider-',
        }
    url_login = "http://wlan.ct10000.com/portal/login4V2.do"
    print(time.ctime(), u"正在尝试登录……")
    try:
        res = requests.post(url_login, data = postdata)
    except:
        my_cmd = "echo ", su_passwd, "| sudo -S ifconfig en0 down && sudo ifconfig en0 up"   # might be wlan0
        my_cmd = ''.join(my_cmd)
        proc = Popen(my_cmd, shell=True)
        print(time.ctime(), u"Login, 连接失败!")

def Logout():
    url_logout = "http://wlan.ct10000.com/portal/Logout.do?NasType=Huawei&NasName=BJ-DS-SR-1.M.ME60"
    try:
        res = requests.get(url_logout)
        print(time.ctime(), u"logout, 已注销Chinanet帐号！")
    except requests.exceptions.ConnectionError:
        print(time.ctime(), u"logout, 失败！")

if __name__ == '__main__':

    account, passwd, su_passwd = getAccount()
    if isLogin():
        print(time.ctime(), u"已经连接到网络。")
    while True:
        if not isLogin():
            #Logout()
            Login(account, passwd)
            time.sleep(10)
            if isLogin():
                print(time.ctime(), u"连接成功！")
            else:
                print(time.ctime(), u"连接失败，将在5秒后重试……")
        time.sleep(10)
