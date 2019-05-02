import requests
import os

def setup_tj_api():
	tj_token = os.environ['TJ_TOKEN']
	tj_api_tj_api_address = 'https://api.tjournal.ru/v1.6/'
	device_token_header_name = 'X-Device-Token'

def add_comment(entry_id, attachments):
	response = requests.post(tj_api_address + 'comment/add',
		data = {'id': entry_id, 'reply_to':0, 'text':'[я](https://ya.ru/) 😡', 'attachments':attachments},
		headers = {device_token_header_name: tj_token})

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("error add comment")

def upload_attachment(url):
	response = requests.post(tj_api_address + 'uploader/extract',
		data = {'url': url},
		headers = {device_token_header_name: tj_token})

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("error upload attachment")

	attachment_fixed_format = str(response.json()['result']).replace('\'','"')
	return attachment_fixed_format

def create_entry(attachment):

	entry = {
		'title': 'Тестовый заголовок',
		'subsite_id': 237791,
		'text':'текст текст текст текст',
		'attachments':attachment}

	response = requests.post(tj_api_address + 'entry/create',
		data = entry,
		headers = {device_token_header_name: tj_token})

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("error create entry")

	#print(response.json()['result'])
	return response.json()['result']['id']

def get_coub():
	coub_api_address = 'https://coub.com/api/v2/search/coubs?q=animals&order_by=newest_popular'
	response = requests.get(coub_api_address)

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("get coub error")
	
	return "https://coub.com/view/" + response.json()['coubs'][0]['permalink']

#setup_tj_api()
#attachment = upload_attachment('https://coub.com/view/1mnj6k')
#entry_id = create_entry(attachment)
#add_comment(entry_id, attachment)
#print("entry ID -", entry_id)

coub_url = get_coub()
print(coub_url)