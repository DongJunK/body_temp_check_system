import requests



class getLog:

    def req(path, method):
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJzdmNfdGd0X3NlcSI6IjEwMDAwMDg2NjkiLCJ1c2VyX25hbWUiOiJza2RsdG0zNTciLCJwdWJfdGltZSI6MTU5MDY3NjMyNTgyMCwibWJyX2lkIjoic2tkbHRtMzU3IiwibWJyX3NlcSI6IjEwMDAwMDg1MzQiLCJtYnJfY2xhcyI6IjAwMDMiLCJhdXRob3JpdGllcyI6WyJST0xFX09QRU5BUEkiLCJST0xFX1VTRVIiXSwicGxhdGZvcm0iOiIzTVAiLCJ0aGVtZV9jZCI6IlBUTCIsImNsaWVudF9pZCI6Ik1qWmlaV014T0dOaU5qZzBOR1UyWldKbFl6WXhZbVZoTlRabE9XSXhaREV4TkRNeU1qQTJPVGc0T1RVMCIsImF1ZCI6WyJJT1QtQVBJIl0sInVuaXRfc3ZjX2NkIjoiMDAxIiwic2NvcGUiOlsidHJ1c3QiXSwiZHN0cl9jZCI6IjAwMSIsImNvbXBhbnkiOiJLdCIsIm1icl9ubSI6Iuq5gOuPmeykgCIsImV4cCI6MTU5MTI3NjMyNSwianRpIjoiNmQxZTAzYTAtN2I3OS00MWE0LWI0ZGEtNDU0Nzg5ZGI1MDU3In0.MFhpGGMDgNnq3bZ1oPVLoPEjmsfxButL-DzsQLQo0fQVRr1zkcDYA2iaf9kfXyiSZ0tA_uZjVTgIRyRkN6Tvj5uxA1US_SaZILFf1f3d1NbdkLhvdbcRPCn-gRH8jHWCDfn-4OSviJBAkzDR2bQYfzaCElfwpZH_obV0kzmRVlxm2YSY7qgwmzDYpvtVAG6yh-GJdqeRyNN6ULk2Ffs8xmxKwHcalWmhhlKrtdxKHbrEE6mFhkDPdu0qGO36JA_aNrmwOcirLOl-HnB5KKT-eJHWhbEB44OnT8_qrojndbkn8GXicgOTeBY4AsEZBPPKUGJNKoiW4NTKllcpFis7Dw'}
        data = {}
        API_HOST = 'https://iotmakers.kt.com:443/api/v1/streams/iot/log'

        url = API_HOST + path
        if method == 'GET':
            return requests.get(url, headers=headers)

    def get_log_list(self):
        resp = getLog.req('?from=1577804400000&to=1590678000000', 'GET')
        resp_body = resp.json()
        print(resp_body["data"])
        return resp_body["data"]
