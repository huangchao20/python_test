import requests

# 获取请求结果
# kind 搜索关键字
# page 页码 默认是1

def get_json(kind, page=1,):
    # post请求参数
    param = {
        'first': 'true',
        'pn': page,
        'kd': kind
    }

    header = { 'Host': 'www.lagou.com',
           'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
           }

    proxies = [
        {'http': '140.143.96.216:80', 'https': '140.143.96.216:80'},
        {'http': '119.27.177.169:80', 'https': '119.27.177.169:80'},
        {'http': '221.7.255.168:8080', 'https': '221.7.255.168:8080'}
    ]

    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
    response = requests.post(url, headers=header, data=param)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        response = response.json()
        return response['content']['positionResult']
    return None
