from bs4 import BeautifulSoup as bs
import requests


url = 'https://www.naver.com'

response = requests.get(url).text
# print(response)

soup = bs(response, 'html.parser')
# print(type(soup))


keywords = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div')

for index, keyword in enumerate(keywords):
    print(index, keyword.text)