import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

urls = [
    'https://www.baidu.com',
    'http://www.gaosiedu.com',
    'https://www.jd.com',
    'https://www.taobao.com',
    'https://news.baidu.com',
]

pool = ThreadPoolExecutor(3)    #线程池
# pools = ProcessPoolExecutor(3)    进程池

def request(url):
    response = requests.get(url)
    return response

def read_data(futuers, *args, **kwargs):
    response = futuers.result()
    requests.encode('utf8')
    print(response.status_code, response.url)

def main():
    for url in urls:
        done = pool.submit(request, url)
        # done = pools.submit(request, url) 进程池
        done.add_done_callback(read_data)

if __name__ == '__main__':
    main()
    pool.shutdown(wait=True)
