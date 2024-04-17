import requests


def down_load_html():
    """
    下载网页信息
    :return: str--->列表的text
    """
    r = requests.get('https://gushitong.baidu.com/top/foreign-全部-fund-常用')
    r.encoding = 'UTF-8'
    if r.status_code != 200:
        raise Exception('error')
    return r.text


if __name__ == '__main__':
    print(down_load_html())
