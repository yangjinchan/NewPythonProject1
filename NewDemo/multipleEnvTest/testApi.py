import yaml

from NewDemo.multipleEnvTest.Api import Api


class TestApi:
    try:
        with open("env.yaml", "r", encoding="utf-8") as f:
            env = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"文件env.yaml未被找到")
    data={
        "method":"get",
         "url":env["test-studio"][env["default"]],#"http://httpbin.testing-studio.com/basic-auth/apple/2233",
        "auth":("apple","2233")
    }

    def test_api(self):
        api=Api()
        print(self.data)
        text=api.send_api(self.data).text
        print(text)