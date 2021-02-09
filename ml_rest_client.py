import json
import requests

url = 'http://da203f8e224e.ngrok.io/predict'

request_data = json.dumps({'age':40,'salary':20000})
response = requests.post(url,request_data)
print (response.text)



