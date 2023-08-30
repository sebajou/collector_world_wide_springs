import requests
import os

WIKIMEDIA_TOKEN: str = os.getenv(
    "WIKIMEDIA_TOKEN"
)

def search_title(q):
    url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/title'
    search_query = q
    number_of_results = 5
    parameters = {'q': search_query, 'limit': number_of_results}

    headers = {
      'Authorization': WIKIMEDIA_TOKEN,
      'User-Agent': 'collector-world-wide-springs'
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    return data


def search_result_to_title(d):
    return d['pages'][0]['title']

def get_summary_from_title(t):
    url = f'https://en.wikipedia.org/api/rest_v1/page/summary/{t}'
    parameters = {
        'accept': 'application/json',
        'charset': 'utf-8',
        'profile': 'https://www.mediawiki.org/wiki/Specs/Summary/1.4.2',
    }

    response = requests.get(url, params=parameters)
    data = response.json()

    return data['description']


def query_to_description(q):
    d = search_title(q)
    t = search_result_to_title(d)
    r = get_summary_from_title(t)

    return r
