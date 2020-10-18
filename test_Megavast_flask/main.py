import io
import requests
import json
from oauthlib.common import to_unicode
from requests.exceptions import HTTPError


class GetGameNames:
    for url in ['https://www.magrtic.com/c/test?api=1&token=Artur_Yefriemov']:
        try:
            response = requests.get(url)

            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            with open('data.txt', 'w') as f:
                with io.open('data.json', 'w', encoding='utf8') as outfile:
                    str_ = json.dumps(response,
                                      indent=4, sort_keys=True,
                                      separators=(',', ': '), ensure_ascii=False)
                    outfile.write(to_unicode(str_))
