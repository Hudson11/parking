import requests

base_url = 'http://localhost:8000/api/v1'

# GET REQUEST
result = requests.get(f'{base_url}/parking/')

# Testing if the endpoint is correct
assert result.status_code == 200

# Testing return by id
# Case 1 -> for existing record
result_by_id = requests.get(f'{base_url}/parking/1/')
assert result_by_id.status_code == 200
# Case 2 -> for not existent record
result_by_id = requests.get(f'{base_url}/parking/300/')
assert result_by_id.status_code != 200


