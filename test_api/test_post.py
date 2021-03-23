import requests

base_url = 'http://localhost:8000/api/v1'

# POST REQUEST

# Inserting a new vehicle into parking
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
result = requests.post(f'{base_url}/parking/', params_1)
assert result.status_code == 201
result = requests.post(f'{base_url}/parking/', params_2)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_3)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_4)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_5)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_6)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_7)
assert result.status_code == 400
result = requests.post(f'{base_url}/parking/', params_8)
assert result.status_code == 201
