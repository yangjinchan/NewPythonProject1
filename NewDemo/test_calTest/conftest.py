
#过滤测试项：从测试集中，过滤掉名字含有’div‘的测试函数
# def pytest_collection_modifyitems(config,items):
    # items[:]=[item for item in items if 'div' not in item.name]#对item列表进行切片赋值，原地修改item列表的内容
    # for item in items:
    #     print(f"打印item==》{item}")

#修改列表顺序，按照测试项名称字母重新排序
# def pytest_collection_modifyitems(config,items):
#     items.sort(key=lambda item:item.name)

# def pytest_collection_modifyitems(config,items):
#     for item in items:
#         print(f"item.keywords==>{item.keywords}")