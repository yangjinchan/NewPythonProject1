import yaml

env ={
    "default" :"dev",
    "test-studio":{
        "dev":"api.jisuapi.com",
        "test":"httpbin.testing-studio.com"
    }
      }
with open("env.yaml","w",encoding="utf-8") as f:
    yaml.safe_dump(data=env,stream=f)