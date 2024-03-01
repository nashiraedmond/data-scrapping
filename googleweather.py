from requests_html import HTMLSession

s=  HTMLSession()

query = 'denmark'
url = f'https://www.google.com/search?q=weather+{query}'

header = {
"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
"Accepted-Language": 'en-GB, en;q-0.5',
# 'Referer': 'https://www.google.com/',
'Dnt': 1,
}
r = s.get(url, headers=header)

temp = r.html.find('span#wob_tm', first=True).text
units = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
precipate = r.html.find('div.wtsRwe span#wob_pp', first=True).text
humidity = r.html.find('div.wtsRwe span#wob_hm', first=True).text
wind = r.html.find('div.wtsRwe span#wob_ws', first=True).text
day_time = r.html.find('div.VQF4g', first=True).find('div#wob_dts', first=True).text
day_clouds = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

