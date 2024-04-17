import requests


def down_load_all_html():
    '''
    下载10页html网页的文本格式
    :return:list()
    '''
    page_index = range(0, 250, 25)

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    htmls = []
    for idx in page_index:
        html = f'http://movie.douban.com/top250?start={idx}&filter='
        print('craw html:', html)
        r = requests.get(html, headers=headers)
        r.encoding = 'UTF-8'
        if r.status_code != 200:
            raise Exception('error')
        htmls.append(r.text)
    return htmls


if __name__ == '__main__':
    print(down_load_all_html()[0])