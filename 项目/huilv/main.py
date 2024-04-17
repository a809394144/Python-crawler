import pandas as pd

from python爬虫.项目.huilv import down_load_all_htmls, parse_single_html

html_doc = down_load_all_htmls.down_load_html()
datas = parse_single_html.parse_single_html(html_doc)
df = pd.DataFrame(datas)
df.to_excel('汇率表.xlsx')
