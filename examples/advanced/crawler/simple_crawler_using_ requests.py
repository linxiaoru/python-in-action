import json
import requests

class SimpleCrawler:
    init_url = "https://zhuanlan.zhihu.com/api/columns/pythoneer/followers"
    offset = 0

    def crawl(self, params=None):
        # 必须指定 UA，否则知乎服务器会判定请求不合法
        headers = {
            "Host": "zhuanlan.zhihu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }

        response = requests.get(self.init_url, headers=headers, params=params)
        print(response.url)
        data = response.json()
        # 7000表示所有关注量
        # 分页加载更多，递归调用
        while self.offset < 7000:
            self.parse(data)
            self.offset += 20
            params = {"limit": 20, "offset": self.offset}
            self.crawl(params)
    
    def parse(self, data):
        # 以 json 格式储存到文件
        with open("followers.json", "a", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item))
                f.write('\n')

if __name__ == '__main__':
    SimpleCrawler().crawl()

"""
1.python扩展包的安装
	pip install requests
    同时安装了 python2 和 python3 时，如果想为 python3 安装扩展包：
        python3 -m pip install requests

2.requests 中文文档：
    http://docs.python-requests.org/zh_CN/latest/user/quickstart.html

3.if __name__ == '__main__':
   一个python的文件有两种使用的方法，
   第一是直接作为脚本执行，
   第二是import到其他的python脚本中被调用（模块重用）执行。
   因此if __name__ == 'main':
   的作用就是控制这两种情况执行代码的过程，
   在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
   而import到其他脚本中是不会被执行的。
"""