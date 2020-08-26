import json
from pprint import pprint
import subprocess
import time
import urllib.parse

url_base = 'https://www.instagram.com/graphql/query/?'

command_template = '''curl '{url}' \
  -H 'authority: www.instagram.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'accept: */*' \
  -H 'x-ig-www-claim: hmac.AR0idzJi1QWbCkupOEA54oOk9hKgc7DW15x2CREC3SwOXQqu' \
  -H 'x-requested-with: XMLHttpRequest' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36' \
  -H 'x-csrftoken: xKOfq5ITjMDuwAohsu2HcDvemZypa25J' \
  -H 'x-ig-app-id: 936619743392459' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://www.instagram.com/a.yefriemov/followers/?hl=ru' \
  -H 'accept-language: ru-UA,ru;q=0.9,uk-UA;q=0.8,uk;q=0.7,ru-RU;q=0.6,en-US;q=0.5,en;q=0.4' \
  -H 'cookie: ig_did=AC44DC06-BD7B-4CB1-8C01-E453189DCCF9; mid=X0Y49QAEAAHdPIEVtK8dI7w51biC; csrftoken=xKOfq5ITjMDuwAohsu2HcDvemZypa25J; ds_user_id=17224569441; sessionid=17224569441%3AZ7QyCseqzhcbWf%3A28; shbid=10104; shbts=1598437630.9104533; rur=ATN; urlgen="{{\"93.73.230.11\": 25229}}:1kAz8E:fQiKMXOo-ru52RppmMRc5fK8zQ8"' \
  -H 'authorization: Token f66c10830dd6f96591c2d2ff24316401c4d1e82b' \
  --compressed > json/followers_{index}.json'''

index = 1
after = None
followers_in_progress = 0
while True:
    after_value = f',"after":"{after}"' if after else ''
    variables = f'{{"id":"17224569441","include_reel":true,"fetch_mutual":true,"first":50{after_value}}}'
    get_params = {
        'query_hash': 'c76146de99bb02f6415203be841dd25a',
        'variables': variables
    }
    ws_url = url_base + urllib.parse.urlencode(get_params)

    result = subprocess.run(command_template.format(url=ws_url, index=index), shell=True, capture_output=True)
    if result.returncode != 0:
        exit('Произошло зло, убиваемся')

    with open(f'json/followers_{index}.json', 'r') as f:
        data = json.load(f)

    after = data['data']['user']['edge_followed_by']['page_info']['end_cursor']
    all_followers = data['data']['user']['edge_followed_by']['count']
    in_current_batch = len(data['data']['user']['edge_followed_by']['edges'])
    followers_in_progress += in_current_batch
    print(f'Обработано {followers_in_progress}/{all_followers}')

    if not data['data']['user']['edge_followed_by']['page_info']['has_next_page']:
        break

    time.sleep(5 if index % 10 != 0 else 20)
    index += 1

print('#Done')
