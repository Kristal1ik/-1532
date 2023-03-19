import requests
from requests.exceptions import HTTPError
import numpy as np


URL = 'https://dt.miet.ru/ppo_it_final'
try:
    response = requests.get(URL,
                            # params={'': ''},
                            headers={'X-Auth-Token': 'xnufs6fe'})
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    print('Success!')

json_response = response.json()

points = (json_response['message'][1]['points'])
data = []
for point in points:
    data.append(list(point.values()))
print(data)