from msilib import add_data
from shutil import ExecError

import allure
import pytest
import yaml
from pymysql.constants.FLAG import NOT_NULL


from NewDemo.test_calTest import calc


# #定义一个类来获取yaml文件内容的测试数据
class YamlData:
    def get_data(self,path):
        try:
            with open(path,'r',encoding='utf-8') as file:
                self.data=yaml.safe_load(file)
            return self.data
        except FileNotFoundError:
            print(f"文件{path}未找到")
            return None
        except Exception as e:
            print(f"文件读取时发送错误：{e}")
            return None
#为了当遇到获取不到数据的情况，程序不会停止运行，可以定义获取数据的方法传给测试用例时使用
def load_add_data(key):
    add_datas = YamlData().get_data('/file/NewpythonProject/NewDemo/data/add.yaml')
    if add_datas[key] is None:
        print(f"没有可以处理的加法数据")
        return []
    else:
        return add_datas[key]
def load_div_data(key):
    div_datas = YamlData().get_data('/file/NewpythonProject/NewDemo/data/div.yaml')
    if div_datas[key] is None:
        print(f"没有可以处理的除法数据")
        return []
    else:
        return div_datas[key]
except_data=load_add_data('except')
print("加载的数据是：",except_data)
# print("加载的数据类型是：",type(load_add_data('norm')))

#定义测试类
@allure.feature("测试加法和除法")#在类上添加装饰器@allure.feature，feature相当于一个大的模块，将case分类到某个feature中，相当于testsuite
class TestCalc:
    #通过fixture装饰器获取到测试的方法
    @pytest.fixture(scope="module",autouse=True)
    def handle(self):
        print("测试开始")
        self.calc= calc.Calc()#前置部分
        yield self.calc
        print("\n测试完毕")#yield后面就是后置部分
    #测试加法
    @allure.story("批量测试加法的正常数据")#在方法上添加@allure.story，story相当于模块下的不同场景，分支功能；另外可以在方法内部添加with allure.step("”)
    @pytest.mark.parametrize("test_data",load_add_data("norm") )
    def test_add_norm(self,handle,test_data):
        if test_data is None:
            pytest.skip("跳过测试，因为没有数据")

        result=handle.add(test_data['a'],test_data['b'])
        assert result - test_data["res"] <0.0001
    @allure.story("测试加法的异常数据")
    @pytest.mark.parametrize("test_data",load_add_data("except"))#if load_add_data("except") else []
    @pytest.mark.xfail
    def test_madd_except(self,handle,test_data):
        print(f"阿萨法胜多负少{test_data}")
        if test_data is None:
            print("跳过测试，因为没有数据0")
            pytest.skip("跳过测试，因为没有数据")
        with pytest.raises(TypeError):
            result=handle.add(test_data['a'],test_data['b'])

    #测试除法
    @allure.story("用正常数据批量测试除法")
    @pytest.mark.parametrize("test_data",load_div_data("norm"))
    def test_div_norm(self,handle,test_data):
        if test_data is None:
            pytest.skip("跳过测试，因为没有数据")
        result=handle.div(test_data['a'],test_data['b'])
        assert result - test_data['res']<0.0001
    @allure.story("用异常数据测试除法")
    @pytest.mark.parametrize("test_data",load_div_data("except"))
    @pytest.mark.xfail
    def test_div_except(self,handle,test_data):
        if test_data is None:
            pytest.skip("跳过测试，因为没有数据")
        # with pytest.raises(TypeError):
        #     result = handle.div(test_data['a'], test_data['b'])
        try:
            result = handle.div(test_data['a'], test_data['b'])
        except (TypeError,ZeroDivisionError) as e:
            assert True
            # if type(test_data['b']) == str:
            #     assert isinstance(e,TypeError)
            # elif test_data['b']==0:
            #     assert isinstance(e,ZeroDivisionError)
            # else:
            #     pytest.fail(f"test_data['b']：{test_data['b']}不是预期的数据")













