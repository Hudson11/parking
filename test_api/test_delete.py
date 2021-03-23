import requests

base_url = 'http://localhost:8000/api/v1'

# DELETE REQUEST

# Testing return by id
# Case 1 -> for existing record
result_by_id = requests.delete(f'{base_url}/parking/2/')
assert result_by_id.status_code == 204
# Case 2 -> for not existent record
result_by_id = requests.delete(f'{base_url}/parking/300/')
assert result_by_id.status_code != 204
