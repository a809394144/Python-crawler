from bs4 import BeautifulSoup


def parse_single_html(html):
    """
    解析单个html，得到数据
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    article_items = (
        soup.find('div', class_='article').
        find('ol', class_='grid_view').find_all('div', class_='item')
    )
    datas = []
    for article_item in article_items:
        rank = article_item.find('div', class_='pic').find('em').get_text()
        info = article_item.find('div', class_='info')
        title = info.find('div', class_='hd').find('a').find('span', class_='title').get_text()
        stars = (info.find('div', class_='bd').find('div', class_='star')
                 .find_all('span')
                 )
        rating_star = stars[0]['class'][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append({
            '排序': rank,
            '标题': title,
            '星级': rating_star.replace('rating', '').replace('-t', ''),
            '评分': rating_num,
            '评价数': comments.replace('人评价', '')
        })

    return datas
