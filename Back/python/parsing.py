import requests

token = 'eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MTM0OTI1MzI4MSwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTk0OTI1MywianRpIjoiYjlhOGJlZmQtYzI4ZS00OWFlLWEzNGEtNDBiMzUxY2M1YzA3In0.Nm6QepHWhZiPWNnsYqthKXGstQjdlweYDrk5rLtUK_MxkRC-t8R3jgkzzZQBJ4pcTh6sj-pogQk-w0-CQrnCVRZ0AaKCyjNZ_FthEXsjFww1mAVrSA4L5oy5rI6ndDh5gTBl486pQjylhXVVbKQ2aPQCODYb0NGpF5_2Nq6AQR-Zjuz0z_lfqv-BtDGSjPIEdMOgEhRiSGeQNrGPqWjEzW6KAv6qW4VqH4K5pRrTda7nRM4KO34i456TVjuY7FokZKfc_lIXb9i38dD_Kjue9S61FqgKqeEBJS8Izp2gtVxON-c3POHf4CfdcX2Q7uYWoHKWmXvcnc4Xs4hHleITtQ'

class getLog:

    def req(path, method):
        headers = {
            'Authorization': 'Bearer '+token}
        data = {}
        API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

        url = API_HOST + path
        if method == 'GET':
            return requests.get(url, headers=headers)

    def get_log_list(self):
        resp = getLog.req('?from=1577804400000&to=1609254000000', 'GET')
        resp_body = resp.json()
        print(resp_body["data"])
        return resp_body["data"]
