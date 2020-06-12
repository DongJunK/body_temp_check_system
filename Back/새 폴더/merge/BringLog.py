import requests
import datetime
import time
token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MTM2NTYzOTIzMSwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTk2NTYzOSwianRpIjoiNWVhNzM2YzktZDcxOS00OTMzLTljYzAtMTg3NGY2OGU5OTQwIn0.EGURrbNdR_myiEs3x-CkPM5QW00o0mKehp6fqUsrcW-Tz9Y7d8ZNgupBF8aODbAZGdaNEGQnz6ugheiO4Ia0Vvb0Mm4eMfxvhPNY0m0SlZ92FMTEFNbONk8TAFKjfcsC5SE46P6VMC9IkUZ9M3KkNwenxeh1FFtMdzlpFkNPLWQ0bSkiH3Ma7M_UZc1qUAVhwqpdbgQgX7KSeu_6U8trTBh2Qldw-FSr1o8OEur3rW_fL9lDSELYhifie47eM5hdrGiHZP7PRuOZ94eSN2A1eKsTHTl0MC3QBC_NiDBaBF_yswIet_sn8YfNW_3Eg1fP3DAPJv0A_qL_ilI-TJ8vkA'


class GetLog:
    datetime_from = None
    datetime_to = None

    def __init__(self, datetime_from):
        if datetime_from is None:
            self.datetime_from = 1577804400000
        else:
            self.datetime_from = int(time.mktime(datetime_from.timetuple())*1000+1000) # +1000 is avoid conflict

    def req(path, method):
        headers = {
            'Authorization': 'Bearer '+token}
        data = {}
        API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

        url = API_HOST + path
        if method == 'GET':
            return requests.get(url, headers=headers)

    def get_log_list(self):
        #resp = GetLog.req('?from=1577804400000&to=1609254000000', 'GET')
        current_timestamp = int(datetime.datetime.now().timestamp()*1000)
        #print(current_timestamp)
        datetime_range = '?from={}&to={}'.format(self.datetime_from, current_timestamp)
        resp = GetLog.req(datetime_range, 'GET')
        resp_body = resp.json()
        #print(resp_body["data"])
        #print(resp_body)
        return resp_body["data"]
