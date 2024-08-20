import requests
import json

access_token = 'ZjBkYjQzNWMtNWYyNi00MzU3LTk4YzktMDkyNDliYmU1NDFlMjk1ODAxN2ItZmVm_P0A1_bc884c7a-820b-497b-8b60-00b4d15ea95d'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

params={'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi','max': '10'}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4, ensure_ascii=False).encode('utf8').decode())
