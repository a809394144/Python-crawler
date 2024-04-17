from bs4 import BeautifulSoup


def parse_single_html(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    lists = (
        soup.find('div', class_='list')
        .find_all('div', class_='list-item')
    )
    datas = []
    for div in lists:
        id = div['data-id']
        if id >= 100:
            break
        name = div.find('div', class_='table-left').find('div').find('div').find('div', class_='stock-marking').find(
            'div', class_='name c-color').get_text()
        money = div.find('div', class_='table-right').find_all('div')
        price = money[0].find('div', class_='right-label-item').find('span').get_text()
        zhangfu = money[1].find('div', class_='right-label-item').find('span').get_text()
        zhange = money[2].find('div', class_='right-label-item').find('span').get_text()
        datas.append({
            '名称': name,
            '最新价': price,
            '涨跌幅': zhangfu,
            '涨幅额': zhange
        })
    return datas
