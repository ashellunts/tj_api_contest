import requests
import os

tj_token = os.environ['TJ_TOKEN']
address = 'https://api.tjournal.ru/v1.6/'
device_token_header_name = 'X-Device-Token'

def add_comment(entry_id, attachments):
	response = requests.post(address + 'comment/add',
		data = {'id': entry_id, 'reply_to':0, 'text':'[я](https://ya.ru/) 😡', 'attachments':attachments},
		headers = {device_token_header_name: tj_token})

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("error add comment")

def upload_attachment(url):
	response = requests.post(address + 'uploader/extract',
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

	response = requests.post(address + 'entry/create',
		data = entry,
		headers = {device_token_header_name: tj_token})

	if response.status_code != 200:
		print (response.status_code)
		print (response.text)
		raise BaseException("error create entry")

	#print(response.json()['result'])
	return response.json()['result']['id']

attachment = upload_attachment('https://coub.com/view/1mnj6k')
entry_id = create_entry(attachment)
add_comment(entry_id, attachment)

print("entry ID -", entry_id)
