import requests

# http://docs.python-requests.org/en/master/api/
_TIMEOUT = 0.3


# GET
resp = requests.get('http://127.0.0.1:5000/hello', timeout=_TIMEOUT)
print(resp.status_code, resp.text)
# http://docs.python-requests.org/en/master/api/#requests.codes
# vs. http.HTTPStatus.OK https://docs.python.org/3/library/http.html
assert resp.status_code == requests.codes.ok


# GET
resp = requests.get('http://127.0.0.1:5000/users/2010', timeout=_TIMEOUT)
print(resp.status_code, resp.json())
assert resp.status_code == requests.codes.ok


# POST
json_data = {'_id': 2010, 'name': 'Cleese'}
resp = requests.post('http://127.0.0.1:5000/users/2010', json=json_data, timeout=_TIMEOUT)
print(resp.status_code, resp.json())
assert resp.status_code == requests.codes.created

# POST
headers = {'test_header': '123'}
params = {'param_1': 1, 'param_2': (2, 3)}
data = 'some data'
resp = requests.post('http://127.0.0.1:5000/users/2010', params=params,
                     data=data, headers=headers, timeout=_TIMEOUT)
print(resp.status_code, resp.text)
assert resp.status_code == requests.codes.bad_request
