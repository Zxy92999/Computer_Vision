import urllib


# 根据之前对动态加载过程中请求参数的分析，定义get_param()函数，该函数根据输入的keyword和paginator参数，生成请求参数

def get_param(keyword, paginator):
    # 将中文关键词转换为符合规则的编码
    keyword = urllib.parse.quote(keyword)
    params = []
    # 为爬取的每页链接定制参数
    for i in range(1, paginator + 1):
        params.append(
            'tn=resultjson_com&logid=5780503607997087233&ipn=rj&ct='
            '201326592&is=&fp=result&fr=&word=%E9%B2%9C%E8%8A%B1&queryWord='
            '%E9%B2%9C%E8%8A%B1&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st='
            '-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height='
            '&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn=270&rn'
            '=30&gsm=10e&1689120237384='.format(keyword, keyword, 30 * i))
    return params  # 返回链接参数


# 定义get_urls()函数，拼接形成每一项的完整请求链接
def get_urls(url, params):
    urls = []
    for param in params:
        # 拼接每页的链接
        url.append(url + param)
    return urls  # 返回每页链接

# 定义get_image_url()函数，利用requests.get(url,headers)方法发起请求，获取页面响应，将响应转换为json格式。

