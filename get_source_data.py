import requests


def get(url):
    headers = {
        # 'Host': 'host',
        # 'Accept': 'accept'
    }
    try:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
        if response.status_code == 403:
            return 'ERR:403'
        if response.status_code == 404:
            return 'ERR:404'
        return None
    except BaseException:
        return 'error'
