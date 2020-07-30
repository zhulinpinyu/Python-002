import requests, os
from fake_useragent import UserAgent

def login(url):
    ua = UserAgent(verify_ssl=False)
    headers = {
        'user-agent': ua.random,
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'referer': 'https://shimo.im/login?from=home',
        'origin': 'https://shimo.im',
        'x-requested-with': 'XmlHttpRequest'
    }

    s = requests.Session()

    body = {
        'email': os.getenv('EMAIL'),
        'mobile': '+86undefined',
        'password': os.getenv('PASSWORD')
    }

    #登录
    s.post(url, data=body, headers=headers)

    #登录后在同一个session下继续获取用户个人信息
    res = s.get('https://shimo.im/lizard-api/users/me', headers=headers)
    print(res.json())

login('https://shimo.im/lizard-api/auth/password/login')