import requests

get_result = 'http://%s:%s/add/%s/%s' % ("localhost", 5000, str(5), str(6))
resp = requests.get(get_result)
print(resp.text)

