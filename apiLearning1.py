import json
import requests
from datetime import datetime

parameters = {
    'lat': 43.65,
    'lon': -79.34
}
response = requests.get("http://api.open-notify.org/iss-pass.json", parameters)
pass_times = response.json()['response']
rise_times = []
times = []


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def main():
    jprint(pass_times)
    for i in pass_times:
        time = i['risetime']
        rise_times.append(time)
    print(rise_times)

    for i in rise_times:
        time = datetime.fromtimestamp(i)
        times.append(time)
        print(time)


if __name__ == '__main__':
    main()