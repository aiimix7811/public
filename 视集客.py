"""
网上收集的脚本, 代码请勿用于非法盈利,一切与本人无关,该代码仅用于学习交流,请阅览下载的24小时内必须删除代码
cron: 0 9 * * *
const $ = new Env("视集客");
"""

import requests
import time
import random
import os
def info(authorization):
    print("======开始执行用户查询======")
    url = "https://app.cqskj.com/index.php/member/member/detail"
    headers = {
        'Authorization': authorization,
        'Host': 'app.cqskj.com',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    response = requests.post(url, headers=headers, json={})
    data = response.json()
    if data["code"] == 1:
        member_info = data["data"]["member_info"]
        nickname = member_info["nickname"]
        credit_money = member_info["credit_money"]
        team_money = member_info["team_money"]
        print("用户:", nickname, "个人任务收益:", credit_money, "广告收益:", team_money)
    else:
        print("获取用户信息失败")
def see(authorization):
    print("======开始执行看广告======")
    url = 'https://app.cqskj.com/index.php/member/ad/see'
    headers = {
        'Authorization': authorization,
        'Host': 'app.cqskj.com',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {"ad_xid": "afdsdcsdcsdcsdc"}
    for i in range(9):
        response = requests.post(url, headers=headers, json=data)
        json_data = response.json()
        msg = json_data['msg']
        print("观看结果:", msg)
        delay = random.randint(15, 25)
        time.sleep(delay)
def withdraw(authorization):
    print("======开始执行广告提现======")
    url = 'https://app.cqskj.com/index.php/member/withdraw/apply'
    headers = {
        'Authorization': authorization,
        'Host': 'app.cqskj.com',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "money": "2",
        "account_type": 2,
        "truename": "李亮",
        "mobile": "18679696759",
        "account_img": "5118",
        "account_name": "",
        "account_card": ""
    }
    response = requests.post(url, headers=headers, json=data)
    json_data = response.json()
    msg = json_data['msg']
    print("提现结果:", msg)
    
def apply(authorization):
    print("======开始执行梯队提现======")
    url = 'https://app.cqskj.com/index.php/member/team_withdraw/apply'
    headers = {
        'Authorization': authorization,
        'Host': 'app.cqskj.com',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "money": "30",
        "account_type": 2,
        "truename": "李亮",
        "mobile": "18679696759",
        "account_img": "5118",
        "account_name": "",
        "account_card": ""
    }
    response = requests.post(url, headers=headers, json=data)
    json_data = response.json()
    msg = json_data['msg']
    print("提现结果:", msg)
authorizations = os.environ.get('skj').split('@')
for auth in authorizations:
    info(auth)
    see(auth)
    withdraw(auth)
    apply(auth)
