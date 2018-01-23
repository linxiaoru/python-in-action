# -*- coding: utf-8 -*-

import requests

def crawl():
    url="https://mp.weixin.qq.com/mp/profile_ext?" \
    "action=home" \
    "&__biz=MjM5MzgyODQxMQ==" \
    "&scene=124&devicetype=iOS11.2.2" \
    "&version=16060125&lang=zh_CN" \
    "&nettype=WIFI&a8scene=3" \
    "&fontScale=100&pass_ticket=DMymS6ygO4IlBTqQrlBafZj7IHoBK4is18KGLbEWMrZXztAvVeHx22BcdN5ft2Tl" \
    "&wx_header=1"

    headers = """
    Host: mp.weixin.qq.com
    Cookie: devicetype=iOS11.2.2; lang=zh_CN; pass_ticket=DMymS6ygO4IlBTqQrlBafZj7IHoBK4is18KGLbEWMrZXztAvVeHx22BcdN5ft2Tl; version=16060125; wap_sid2=CMSUh9YCElw2UmRwM1dMeUJxajBuVkdhcDdYNGp1c3QwZHpnaGowUTR3bHJlZUdiNHd0elA5TjQxVnhsRDlEd2VyM1pNZ3laaEJmaktueFlzZjhvTFRmazRHV3ZYcXdEQUFBfjC+hZjTBTgMQJRO; wxuin=717343300
    X-WECHAT-KEY: c84b833784e89b0076effac45022daaf9211274bb7f81b2a745973f5b0e2611c1eb746847fd915727851c310c5fbe046d7c6569bfdcb81beb350f17e3b7d7c5dc3eed2c06a6e28fced90a0804ea961c9
    X-WECHAT-UIN: NzE3MzQzMzAw
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN
    Accept-Language: zh-cn
    Accept-Encoding: br, gzip, deflate
    Connection: keep-alive
    """

    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    if '<title>验证</title>' in response.text:
        raise Exception("获取微信公众号文章失败，可能是因为你的请求参数有误，请重新获取")
    data = extract_data(response.text)
    for item in data:
        print(item)

# 把相应结果另存为 html 文件
with open("weixin_history.html", "w", encoding="utf-8") as f:
    f.write(response.text)


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles

# requests.get 方法里面的 headers 参数必须是字典对象
def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com"
        "Connection": "keep-alive"
        "Cache-Control": "max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        h = h.strip()
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


if __name__ == '__main__':
    crawl()