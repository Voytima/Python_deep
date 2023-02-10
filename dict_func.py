"""
📌 Напишите функцию, принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ - значение переданного аргумента, а
значение - имя аргумента. Если ключ не хэшируем, используйте его строковое
представление.
"""


def dict_return(string='Help!', lst=[1, 2, 3], tup=(1, 2, 3), num=1, dct={1: 2, 3: 4}):
    k_args = dict(string=string, lst=lst, tup=tup, num=num, dct=dct)
    res = {}
    for key, val in k_args.items():
        if type(val) == list or type(val) == dict or type(val) == set or type(val) == bytearray:
            res[str(val)] = key
        else:
            res[val] = key
    return res


print(dict_return())
