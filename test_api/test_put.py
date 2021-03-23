import requests

base_url = 'http://localhost:8000/api/v1'

# PUT REQUEST

# Updating a vehicle into parking
params_1 = {
    "plate": "AAA-9999"
}
params_2 = {
    "plate": ""
}
params_3 = {
    "plate": "1111111111111"
}
params_4 = {
    "plate": "111-AAAA"
}
params_5 = {
    "plate": None
}
params_6 = {}
params_7 = {
    "minutes": "",
    "check_out": False,
    "pay": False
}
params_8 = {
    "plate": "AAA-6666",
    "minutes": "",
    "check_out": False,
    "pay": False
}
result = requests.put(f'{base_url}/parking/1/', params_1)
assert result.status_code == 200
result = requests.put(f'{base_url}/parking/1/', params_2)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_3)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_4)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_5)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_6)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_7)
assert result.status_code == 400
result = requests.put(f'{base_url}/parking/1/', params_8)
assert result.status_code == 200

# check_out pay = False
result = requests.put(f'{base_url}/parking/1/out/')
assert result.status_code == 200
# check_out pay = True
result = requests.put(f'{base_url}/parking/2/out/')
assert result.status_code == 200

# pay
result = requests.put(f'{base_url}/parking/2/pay/')
assert result.status_code == 200
# pay
result = requests.put(f'{base_url}/parking/1/pay/')
assert result.status_code == 200

# Checking if minutes have been added after check_out
# check_out = True
result = requests.get(f'{base_url}/parking/2/')
assert result.json()['minutes'] != ''
# check_out = False
result = requests.get(f'{base_url}/parking/1/')
assert result.json()['minutes'] == ''
