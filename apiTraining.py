import requests
import json

API_KEY = '6ce0b6f8bee95650d61533cbd42a9e76'
USER_AGENT = 'conorcourtenay'


def lastfm_get(payload):
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = API_KEY
    payload['format'] = 'json'
    response = requests.get(url, headers = headers, params= payload)
    return response


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main ():
    r = lastfm_get({
        'method': 'chart.gettopartists'
    })
    print(r.status_code)
    jprint(r.json()['artists']['@attr'])


if __name__ == '__main__':
    main()

