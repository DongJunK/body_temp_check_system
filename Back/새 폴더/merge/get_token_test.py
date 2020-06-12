import requests
import base64
import json
def getInfo():
	global iot_info
	with open('./config/iot_config.json','r') as f:
		iot_info = json.load(f)

def req():
	appId = iot_info['appId']
	secret = iot_info['secret']
	userId = "'"+iot_info['userId']+"'"
	userPW = "'"+iot_info['userPW']+"'"
	data = {
		'grant_type':'password',
		'username':userId,
		'password':userPW
	}
	print(appId)
	print(secret)
	print(userId)
	print(userPW)

	send = appId + ':' + secret
	send_encode = send.encode('UTF-8')
	code = base64.b64encode(send_encode)
	headers = {
		'Authorization':'Basic ' + code.decode('utf-8')
	}

	url = 'https://iotmakers.kt.com/oauth/token'
	result = requests.post(url, headers=headers, data=data)
	return result.json()

def req_test():
	token = req()
	headers = {'Authorization':'Bearer ' + token['access_token']}
	API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

	url = API_HOST + '?from=1577804400000&to=1590678000000'
	result = requests.get(url, headers=headers)
	return result.json()

getInfo()
result = req_test()
print(result)
