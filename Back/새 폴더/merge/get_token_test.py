import requests
import base64
import json

class GetToken():
	iot_info = None
	json_file = None

	def __init__(self):
		with open('./config/iot_config.json', 'r') as self.json_file:
			self.iot_info = json.load(self.json_file)

	def __del__(self):
		self.json_file.close()

	def req(self):
		appId = self.iot_info['appId']
		secret = self.iot_info['secret']
		userId = self.iot_info['userId']
		userPW = self.iot_info['userPW']
		data = {
			'grant_type':'password',
			'username':userId,
			'password':userPW
		}
		# print(appId)
		# print(secret)
		# print(userId)
		# print(userPW)

		send = appId + ':' + secret
		send_encode = send.encode('UTF-8')
		code = base64.b64encode(send_encode)
		headers = {
			'Authorization':'Basic ' + code.decode('utf-8')
		}

		url = 'https://iotmakers.kt.com/oauth/token'
		result = requests.post(url, headers=headers, data=data)
		return result.json()

	def req_test(self):
		token = self.req()
		headers = {'Authorization':'Bearer ' + token['access_token']}
		API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

		url = API_HOST + '?from=1577804400000&to=1590678000000'
		result = requests.get(url, headers=headers)
		return result.json()



if __name__ == '__main__':
	a = GetToken()
	print(a.req())
	print(a.req_test())
