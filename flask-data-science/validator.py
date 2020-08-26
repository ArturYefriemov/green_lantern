import csv

from .app import upload_file
from urllib.request import urlopen
from urllib.error import URLError


def valid_url_check(data_name: str) -> list:
    with open(f'uploads{data_name}.csv') as fill:
        data_read = csv.reader(fill, delimiter=",")

        def validate_web_url(url):
            for url in upload_file:
                try:
                    urlopen(url)
                    return True
                except URLError:
                    return False

        return [line[1] for line in data_read]


