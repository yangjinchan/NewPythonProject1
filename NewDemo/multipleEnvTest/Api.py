from logging import exception
from requests.auth import HTTPBasicAuth
import requests
import yaml


class Api:
    # try:
    #     with open("env.yaml", "r", encoding="utf-8") as f:
    #         env = yaml.safe_load(f)
    # except FileNotFoundError:
    #     print(f"文件env.yaml未被找到")
    def send_api(self,data:dict):
        # data["url"]=data["url"].replace("httpbin.testing-studio.com",self.env["test-studio"][self.env["default"]])
        r=requests.request(method=data["method"],url=data["url"],auth=HTTPBasicAuth("apple","2233"))
        return r
if __name__=="__main__":
    pass