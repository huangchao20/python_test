import random
import urllib.parse
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
# import time


class EbaySpider(object):

    def __init__(self):
        self.file_object = open("amazon.txt", 'a')
        self.file_object.write("asin, state\n")

    def randHeader(self):
        head_connection = ['Keep-Alive', 'close']
        head_accept = ['text/html, application/xhtml+xml, */*']
        head_accept_language = ['zh-CN,fr-FR;q=0.5', 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
        head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                           'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                           'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                           'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                           'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                           'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                           'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11'
                           ]

        header = {
            'Connection': head_connection[0],
            'Accept': head_accept[0],
            'Accept-Language': head_accept_language[1],
            'User-Agent': head_user_agent[random.randrange(0, len(head_user_agent))]
        }
        return header

    def getBeautifulSoup(self, query_rl):
        req = urllib.request.Request(url=query_rl, headers=self.randHeader())
        webpage = urllib.request.urlopen(req)
        html = webpage.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def search(self, serchWords):
        serchWords = str(serchWords).replace(" ", "%20")
        # _ipg=100每页100 ，
        query_rl = "https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=100&rt=nc&_nkw=" + serchWords + "&_pgn=1&_skc=0"
        soup = self.getBeautifulSoup(query_rl)
        # print(soup.prettify())
        content = soup.find("span", "rcnt")
        itemSize = int(content.string)
        pageSize = int(itemSize / 100)
        if itemSize % 100 != 0:
            pageSize += 1

        print("总计" + str(itemSize) + "项，共" + str(pageSize) + "页（每页100条）")
        print("第1页....")
        result = []
        content = soup.find_all("div", "lvpic pic img left")
        for i in content:
            s = str(i)
            l = s.find("iid=")
            if l == -1:
                continue
            r = s.find("\">")
            result.append(str(s[l + 5:r]))

        for _pgn in range(2, pageSize + 1):
            print("第" + str(_pgn) + "页....")
            query_rl = "https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=100&rt=nc&_nkw=" + serchWords + "&_pgn=" + str(
                _pgn) + "&_skc=" + str((_pgn - 1) * 100)
            soup = self.getBeautifulSoup(query_rl)
            content = soup.find_all("div", "lvpic pic img left")
            for i in content:
                s = str(i)
                l = s.find("iid=")
                if l == -1:
                    continue
                r = s.find("\">")
                result.append(str(s[l + 5:r]))

        return result


if __name__ == '__main__':
    ebay = EbaySpider()
    result = ebay.search("2016 nerf bar Silverado 2500")
    for i in range(len(result)):
        print(str(i), end="\t")
        print(result[i])