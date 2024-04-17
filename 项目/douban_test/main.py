from python爬虫.项目.douban_test import parse_single_html
from python爬虫.项目.douban_test import down_load_all_htmls
import pandas as pd

htmls = down_load_all_htmls.down_load_all_html()
datas = []
for html in htmls:
    datas = datas + parse_single_html.parse_single_html(html)
df = pd.DataFrame(datas)
df.to_excel('豆瓣影评TOP250.xlsx')
