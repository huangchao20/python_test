import gevent
from gevent import monkey
from gevent import pool
import requests

monkey.patch_all()
urls = [
    'https://www.baidu.com',
    'http://www.sina.com.cn',
    'https://news.baidu.com',
]
def task(url):
    response = requests.get(url)
    print(response.status_code)

if __name__ == '__main__':
    pool.Pool(5)        #Pool控制每次请求的数量。
    for u in urls:
        gevent.joinall([
        gevent.spawn(task, url=u),
            ])