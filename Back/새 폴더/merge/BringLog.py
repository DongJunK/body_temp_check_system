import requests
import datetime
import time
from re import search
import os
import json
from get_token_test import GetToken as Token

#token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MTM2NTYzOTIzMSwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTk2NTYzOSwianRpIjoiNWVhNzM2YzktZDcxOS00OTMzLTljYzAtMTg3NGY2OGU5OTQwIn0.EGURrbNdR_myiEs3x-CkPM5QW00o0mKehp6fqUsrcW-Tz9Y7d8ZNgupBF8aODbAZGdaNEGQnz6ugheiO4Ia0Vvb0Mm4eMfxvhPNY0m0SlZ92FMTEFNbONk8TAFKjfcsC5SE46P6VMC9IkUZ9M3KkNwenxeh1FFtMdzlpFkNPLWQ0bSkiH3Ma7M_UZc1qUAVhwqpdbgQgX7KSeu_6U8trTBh2Qldw-FSr1o8OEur3rW_fL9lDSELYhifie47eM5hdrGiHZP7PRuOZ94eSN2A1eKsTHTl0MC3QBC_NiDBaBF_yswIet_sn8YfNW_3Eg1fP3DAPJv0A_qL_ilI-TJ8vkA'
#token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MDY3NjMyNTgyMCwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTI3NjMyNSwianRpIjoiNmQxZTAzYTAtN2I3OS00MWE0LWI0ZGEtNDU0Nzg5ZGI1MDU3In0.MFhpGGMDgNnq3bZ1oPVLoPEjmsfxButL-DzsQLQo0fQVRr1zkcDYA2iaf9kfXyiSZ0tA_uZjVTgIRyRkN6Tvj5uxA1US_SaZILFf1f3d1NbdkLhvdbcRPCn-gRH8jHWCDfn-4OSviJBAkzDR2bQYfzaCElfwpZH_obV0kzmRVlxm2YSY7qgwmzDYpvtVAG6yh-GJdqeRyNN6ULk2Ffs8xmxKwHcalWmhhlKrtdxKHbrEE6mFhkDPdu0qGO36JA_aNrmwOcirLOl-HnB5KKT-eJHWhbEB44OnT8_qrojndbkn8GXicgOTeBY4AsEZBPPKUGJNKoiW4NTKllcpFis7Dw'


class GetLog:
    datetime_from = None
    datetime_to = None
    token_path = os.getcwd() + "\\token.json"


    def __init__(self, datetime_from):
        if datetime_from is None:
            self.datetime_from = 1577804400000
        else:
            self.datetime_from = int(time.mktime(datetime_from.timetuple())*1000+1000) # +1000 is avoid conflict
        self.token = self.getToken_txt(self.token_path)


    def req(self, path, method):
        headers = {
            'Authorization': 'Bearer '+self.token}
        data = {}
        API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

        url = API_HOST + path
        if method == 'GET':
            return requests.get(url, headers=headers)

    def getToken_txt(self, path):
        try:
            with open(path, 'r') as token_json:
                token_data = json.load(token_json)
                token_json.close()
                if token_data['Token'] is None:
                    return self.setToken_txt(self.token_path)
                else:
                    return token_data['Token']
        except FileNotFoundError as f:
            print(f)
        except json.JSONDecodeError as j:
            print(j)
        finally:
            return self.setToken_txt(self.token_path)


    def setToken_txt(self, path):
        getToken_Class = Token()
        # new_token = getToken_Class.req()
        # print(new_token)
        # print(type(new_token))
        # with open(os.getcwd()+'\\iot_token.json','w') as f:
        #     json.dump(new_token, f)
        # f.close()
        del getToken_Class

        #new_token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MTM2NTYzOTIzMSwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTk2NTYzOSwianRpIjoiNWVhNzM2YzktZDcxOS00OTMzLTljYzAtMTg3NGY2OGU5OTQwIn0.EGURrbNdR_myiEs3x-CkPM5QW00o0mKehp6fqUsrcW-Tz9Y7d8ZNgupBF8aODbAZGdaNEGQnz6ugheiO4Ia0Vvb0Mm4eMfxvhPNY0m0SlZ92FMTEFNbONk8TAFKjfcsC5SE46P6VMC9IkUZ9M3KkNwenxeh1FFtMdzlpFkNPLWQ0bSkiH3Ma7M_UZc1qUAVhwqpdbgQgX7KSeu_6U8trTBh2Qldw-FSr1o8OEur3rW_fL9lDSELYhifie47eM5hdrGiHZP7PRuOZ94eSN2A1eKsTHTl0MC3QBC_NiDBaBF_yswIet_sn8YfNW_3Eg1fP3DAPJv0A_qL_ilI-TJ8vkA'
        new_token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MDY3NjMyNTgyMCwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTI3NjMyNSwianRpIjoiNmQxZTAzYTAtN2I3OS00MWE0LWI0ZGEtNDU0Nzg5ZGI1MDU3In0.MFhpGGMDgNnq3bZ1oPVLoPEjmsfxButL-DzsQLQo0fQVRr1zkcDYA2iaf9kfXyiSZ0tA_uZjVTgIRyRkN6Tvj5uxA1US_SaZILFf1f3d1NbdkLhvdbcRPCn-gRH8jHWCDfn-4OSviJBAkzDR2bQYfzaCElfwpZH_obV0kzmRVlxm2YSY7qgwmzDYpvtVAG6yh-GJdqeRyNN6ULk2Ffs8xmxKwHcalWmhhlKrtdxKHbrEE6mFhkDPdu0qGO36JA_aNrmwOcirLOl-HnB5KKT-eJHWhbEB44OnT8_qrojndbkn8GXicgOTeBY4AsEZBPPKUGJNKoiW4NTKllcpFis7Dw'
        token_dic = {'Token': new_token}
        with open(self.token_path, 'w') as token_json:
            json.dump(token_dic, token_json)
        token_json.close()
        return new_token

    def get_log_list(self):

        #resp = GetLog.req('?from=1577804400000&to=1609254000000', 'GET')
        current_timestamp = int(datetime.datetime.now().timestamp()*1000)
        datetime_range = '?from={}&to={}'.format(self.datetime_from, current_timestamp)
        resp = self.req(datetime_range, 'GET')
        resp_body = resp.json()
        print(resp_body)
        try:
            return resp_body["data"]
        except KeyError:
            if search('Access token expired', resp_body['error_description']):
                self.setToken_txt(self.token_path)
                #self.getToken_txt(self.token_path)
            elif search('Cannot Convert access token to JSON', resp_body['error_description']):
                print(resp_body)
            else:
                print(resp_body)



if __name__ == '__main__':
    a = GetLog(None)
    print(a.get_log_list())
    #print(a.setToken_txt(a.token_path))
    #print(a.getToken_txt(a.token_path))

    #a.getToken_txt(GetLog.token_path)