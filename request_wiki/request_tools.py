import requests


def search_title(q):
    url = 'https://api.wikimedia.org/core/v1/wikipedia/en/search/title'
    search_query = q
    number_of_results = 5
    parameters = {'q': search_query, 'limit': number_of_results}

    headers = {
      'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0Y2M4Mzg3YzI3OWM5MGJiOTQ3NzkyY2Y3ZmEwZTQxOSIsImp0aSI6IjRkNWZhNmFlYWM4ZTM4NDJjYTg2NGE2NDU5Yjg4NGZlNTQ1NmIyYzQ3NTNiNzU2YTlhYmU0YjNhNzg4YmM5OWJiZjJmMmI5YWJjNWE2OGNjIiwiaWF0IjoxNjkyNjQ4MDk5LjQwOTA4OSwibmJmIjoxNjkyNjQ4MDk5LjQwOTA5MywiZXhwIjozMzI0OTU1Njg5OS40MDY1NTUsInN1YiI6IjYxODM5NTMiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsInJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIl19.TPf4ugyHC7boPrYBNUPLuKa9QxL2G0KCUxTaSyRsiiGKNqk0h_848HZk8UxBzhAABmvS_tiSI7zn89FPrR3o0DHEiNxJEVdQ37-c75SIFXKinZuFCUQDZjOEheQzMBWpL2hnSkFYSgtgd-pDzGdNPqoSsEGX0Qg_CcUPt3fNjOaCzo8QQzLRb9EBgxo9eB4yZv_JVHqebAZaz-u9NN85gMqUawO0Bxo_3GJTMW_NGyAtB91X-CxQPuTxdb0asrRxvD2xbSuFwaGMtm_j27Rfa3Ixlyt6Lwi_Wq5_iypISgLPLdMVeIADbhGtQrXwvnv9LcpvSVdvWdzvWvRI9K83F420Ah2uAP34maHDh-bAean55IblFMPV45F-5z3WFOU5P7XZKtSjnIZhbSHMFRrjMwe-4o2lyZlz_iQE3QxtXx5rXhydJVQguLOIDFQ_PV_vWb_Q0Udd6stP7u37oYqnzcyaUqjEDTik9NjU0a-0UUlC1-wET48wEaTbZmFmVXDTQo31LGhlcNPmw8eWCfhWBz5mKWhjJu_UvFbpQePjUCkxxLi4dR12cWsAWUWieMoQAWQQEUiJXDNMBWYBbM8pVHYCKy0XrVoYhWz17BS4FUReRi0vE5oiG1c_FW9MU-iPEIY8apl_Wn8dLeFTCqk7zoWGWjGiBbEzw8X4En4aA5g',
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
