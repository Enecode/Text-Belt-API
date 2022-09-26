import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': 'YOUR_PHONE_NUMBER',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())
