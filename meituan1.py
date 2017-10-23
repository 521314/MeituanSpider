import requests
import gzip

cookies = {
    '_lxsdk_cuid': '15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8',
    '_lxsdk': '15f336a3999c8-042db71adeba35-574e6e46-3d10d-15f336a399ac8',
    '_ga': 'GA1.2.1160483408.1508395875',
    '_gid': 'GA1.2.1915325613.1508395875',
    'wx_channel_id': '0',
    'webp': '1',
    'utm_source': '0',
    'w_latlng': '23129163,113264435',
    'wm_poi_view_id': '287098077500822',
    'poiid': '287098077500822',
    'w_cid': '110100',
    'w_cpy': 'beijing',
    'w_cpy_cn': '%E5%8C%97%E4%BA%AC',
    'w_visitid': '9465eba6-c50d-406e-b197-8763496bf50c',
    '__mta': '87858855.1508395879768.1508490339911.1508516292290.19',
    '_lxsdk_s': '15f3a93ec6c-ebe-4de-570%7C%7C2',
    'terminal': 'i',
    'w_utmz': 'utm_campaign=(direct)&utm_source=5000&utm_medium=(none)&utm_content=(none)&utm_term=(none)',
    'w_uuid': 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX',
    'JSESSIONID': '14hzj21kblcohe40gkopamuey',
}

headers = {
    'Origin': 'http://i.waimai.meituan.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'Referer': 'http://i.waimai.meituan.com/channel?category_type=101065&sort_type=2',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

params = (
    ('category_type', '101065'),
    ('sort_type', '2'),
    ('_token', 'eJydjl9rgzAUxb9LwL0s1EQXGwUZSi3o1sLU mCRkTlnQ/1TNWuVse  lDnGXne58Dv3cLicD9D7r8DCSI4JgRikJogSbOiUEGMJQf7XMzUDgpc WQFrv0QUmsTIrkYo7z02NQQxoiiDP5roGdTu5F5TvgyBgxAnS1X54sJ4zfiiLrh4Z80ib2s1P7CmKar7nImibPvpWUynwsYII4PcDG0vvg0NwP / TWLUdiKt1RcT6Ge4pmKoyvmGsimdSybSh5nspli5sDLBligCMY44qMfe7d4m4SPMR DOKfnrr2cu ji0BJtVvm4wTt3omlFHtgxEWXajW/VOgjd1J92jrc9RuTJtsHnF2kkd I='),
)

data = [
  ('uuid', 'zLSZ6qkn47NTdNdbDnS0dnfYQeH0v6L6fxfPmNA4QDix0Wr8NFNj1DzGDMFjV9YX'),
  ('platform', '3'),
  ('partner', '4'),
  ('page_index', '0'),
  ('apage', '1'),
]

response = requests.post('http://i.waimai.meituan.com/ajax/v6/poi/filter', headers=headers, params=params, cookies=cookies, data=data)
print response.text
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# requests.post('http://i.waimai.meituan.com/ajax/v6/poi/filter?category_type=101065&sort_type=2&_token=eJydjl9rgzAUxb9LwL0s1EQXGwUZSi3o1sLU+mCRkTlnQ/1TNWuVse++lDnGXne58Dv3cLicD9D7r8DCSI4JgRikJogSbOiUEGMJQf7XMzUDgpc+WQFrv0QUmsTIrkYo7z02NQQxoiiDP5roGdTu5F5TvgyBgxAnS1X54sJ4zfiiLrh4Z80ib2s1P7CmKar7nImibPvpWUynwsYII4PcDG0vvg0NwP+/+TWLUdiKt1RcT6Ge4pmKoyvmGsimdSybSh5nspli5sDLBligCMY44qMfe7d4m4SPMR+DOKfnrr2cu+ji0BJtVvm4wTt3omlFHtgxEWXajW/VOgjd1J92jrc9RuTJtsHnF2kkd+I=', headers=headers, cookies=cookies, data=data)
