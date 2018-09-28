# *- coding:utf8 *-


def get_str(args, key):
    """
    获取请求下发参数中如果包含Unicode参数，转置为utf-8
    :param args: 所有参数
    :param key: 需要获取的key值
    :return: 一定是utf-8的value
    """
    name = args.get(key)
    return name
