import ssl

from urllib.request import Request
from urllib.request import urlopen

context = ssl._create_unverified_context()

request = Request(url="https://foofish.net/pip.html",
                    method="GET",
                    headers={"Host": "foofish.net"},
                    data=None)

response = urlopen(request, context=context)        # urlopen 函数会自动与目标服务器建立连接，发送 HTTP 请求，该函数的返回值是一个响应对象 Response，里面有响应头信息，响应体，状态码之类的属性。          
headers = response.info()
content = response.read()
code =  response.getcode()

print('response', response)
print('headers', headers)
print('content', content)
print('code', code)