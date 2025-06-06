from ast import Param
import requests
from requests.auth import HTTPBasicAuth


class TestDemo:
#     def test_getProjectConfig(self):
#         # token = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTc0MjEwNzkzNywiaWF0IjoxNzM0MzMxOTM3LCJqdGkiOiJjdGZzczhlYWtxY3AzZ3VsbXEzZyIsInR5cCI6ImFjY2VzcyIsImFwcF9pZCI6ImtpbWkiLCJzdWIiOiJjcTcycjMxcDJrMTIycjZpcWdsMCIsInNwYWNlX2lkIjoiY3E3MnIzMXAyazEyMnI2aXFnMWciLCJhYnN0cmFjdF91c2VyX2lkIjoiY3E3MnIzMXAyazEyMnI2aXFnMTAifQ.zRYkQWOdyWVDR_a_S5PtelyBEhmcz501HzItmG-e6WWiyh1zinr0oDaXT1DSvO-biIZ5kwm3PdBJh81H7oFNgQ"
#         # header = {"authorization": f"Bearer{token}"}
#         url="https://www.googleapis.com/identitytoolkit/v3/relyingparty/getProjectConfig"
#         param= {"key":"AIzaSyDdoWgStfhP7nRtaKs-SmeMVp8D3G8-CWA","cb":"7343324345"}
#         response=requests.get(url=url,params=param)
#         print(f"json:{response.json()}")
#         assert response.status_code==200
#     def test_login(self):
#         url="http://ana-portal-dev.gea.io/ana/login"
#         data={"oauthIdToken":"eyJhbGciOiJSUzI1NiIsImtpZCI6IjU2NGZlYWNlYzNlYmRmYWE3MzExYjlkOGU3M2M0MjgxOGYyOTEyNjQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTAyNjg3MzQzNjk0Mi04bWtrMWI2MWw0OTZqcHFnNGZyZHVncWplbmM3OWJncC5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjEwMjY4NzM0MzY5NDItOG1razFiNjFsNDk2anBxZzRmcmR1Z3FqZW5jNzliZ3AuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTcwOTkyODQxNjg2MjU4OTI1MTMiLCJoZCI6InNpbm9keW5hbWljLmNvbSIsImVtYWlsIjoic3VtbWVyLnlhbmdAc2lub2R5bmFtaWMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImF0X2hhc2giOiJHRTRGdGc1b0JMUWhkUzhETGZSWkF3IiwiaWF0IjoxNzM0NDIzNDQxLCJleHAiOjE3MzQ0MjcwNDF9.j4aOQ1qOaoUM-AQWmzt4o2Wx_zD603B3pUiuj0Zs5LlQGOKmmRTZrBqG0Frl9pp9Gs7mzRRu8FnbpKlGr00Rm8UluTZV2Sh2g9-o2swjZUr3Z6aNAS4kcK_iOcmXGzjy64aTc9LO9D8J88qgZgMiOmmltRd3NMGlGMA4sqvtUIUYYYsYZPKEiRfQGC6YaQlVIzjO7YD14l3rtHqYBJjoHb9BRs8DVYxb-NrJIANO6yOMr4nzhYKeu3G4ox0bRiowY4Dbrj6WXkjwThIM-WJWKEgs8AJwCSHQc1E35USpYXIoziRvIQD2lP2bNMzUaLvAQohTpbz7Izfr0WdvjMfvHw","userInfo":{"providerId":"google.com","isNewUser":"false","profile":{"name":"Summer Yang","granted_scopes":"https://www.googleapis.com/auth/userinfo.profile openid https://www.googleapis.com/auth/userinfo.email","id":"117099284168625892513","verified_email":"true","given_name":"Summer ","hd":"sinodynamic.com","family_name":"Yang","email":"summer.yang@sinodynamic.com","picture":"https://lh3.googleusercontent.com/a/ACg8ocJm3BaHKKSSYAzUz-Ir9pm3VzIaB58NmzvkK45mh90RpMd53w=s96-c"}}}
#         response = requests.post(url=url, data=data)
#         print(f"json:{response.json()}")
#         assert response.status_code == 200
    def test_oauth(self):
        url="http://httpbin.testing-studio.com/basic-auth/apple/2233"
        auth=("apple","2233")
        response=requests.get(url=url,auth=HTTPBasicAuth("apple","2233"))
        print(response.text)

