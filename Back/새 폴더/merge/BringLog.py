import requests
import datetime
import time
from re import search
import os
import json
from get_token_test import GetToken as Token

class GetLog:
    datetime_from = None
    datetime_to = None
    token_path = os.getcwd() + "\\token.json"

    def __init__(self, datetime_from):
        if datetime_from is None:
            self.datetime_from = 1577804400000
        else:
            self.datetime_from = int(time.mktime(datetime_from.timetuple())*1000+1000) # +1000 is avoid conflict
        self.token = self.getToken_json(self.token_path)

    def req(self, path, method):
        headers = {
            'Authorization': 'Bearer '+self.token['access_token']}
        data = {}
        API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

        url = API_HOST + path
        if method == 'GET':
            # Try Exception - requests.exceptions.ConnectionError
            # If disconnect internet
            try:
                return requests.get(url, headers=headers)
            except requests.exceptions.ConnectionError as c:
                return None



    def getToken_json(self, path):
        try:
            with open(path, 'r') as token_json:
                token_data = json.load(token_json)
                token_json.close()
                if token_data["access_token"] is not None:
                    return token_data["access_token"]
        except FileNotFoundError as f:
            print(f)
        except json.JSONDecodeError as j:
            print(j)
        return self.setToken_json(self.token_path)

    def setToken_json(self, path):
        getToken_Class = Token()
        new_token = getToken_Class.req()
        with open(os.getcwd()+'\\iot_token.json','w') as f:
            json.dump(new_token, f)
        f.close()
        del getToken_Class

        token_dic = {'access_token': new_token}
        with open(self.token_path, 'w') as token_json:
            json.dump(token_dic, token_json)
        token_json.close()
        return new_token

    def get_log_list(self):

        #resp = GetLog.req('?from=1577804400000&to=1609254000000', 'GET')
        current_timestamp = int(datetime.datetime.now().timestamp()*1000)
        datetime_range = '?from={}&to={}'.format(self.datetime_from, current_timestamp)
        resp = self.req(datetime_range, 'GET')
        if resp is None:
            return None
        resp_body = resp.json()
        try:
            if search('OK', resp_body['responseCode']):
                return resp_body.get('data')
        except KeyError:
            # if resp_body['responseCode'] !='OK'
            if search('Access token expired', resp_body['error_description']):
                print(resp_body)
            elif search('Cannot Convert access token to JSON', resp_body['error_description']):
                print(resp_body)
            self.setToken_json(self.token_path)
#
# if __name__ == '__main__':
#     a = GetLog(None)
#     print(a.get_log_list())
