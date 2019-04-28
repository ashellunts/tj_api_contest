import requests

address = 'https://api.tjournal.ru/v1.6/'
token = ''
device_token_header_name = 'X-Device-Token'

response = requests.post(address + 'comment/add',
	data = {'id': 94289, 'reply_to':0, 'text':'test'},
	headers = {device_token_header_name: token})

print(response.status_code)

print(response.json())