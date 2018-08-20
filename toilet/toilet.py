# 
# author gino
# created on 2018/8/20
import re

up = 1
down = 0


def convert_str_number(text):
    """
    # 将字符串转换成01序列，忽略大小写，假设只有ud两类字母
    :param text: ud组合字符串
    :return: 01数字序列
    """
    text = text.upper()
    if not re.compile(r'^[UD]+$').search(text):
        raise Exception("{}: invalid arguments".format(text))
    return [up if 'U' == item else down for item in text]


def policy_all(init, person, final):
    """
    # 支持三个策略，统计调整次数，未作入参校验
    :param init: 初始状态
    :param person: 使用者期望状态
    :param final: 策略期望状态，分别对应final为 up，down，None(Like)
    :return: 调整次数
    """
    count = 0
    for item in person:
        count += init ^ item
        if final is None:
            init = item
        else:
            count += item ^ final
    return count


def evaluate(text):
    """
    评估次数并输出
    :param text: 需要评估的额字符串
    """
    data = convert_str_number(text)
    init = data.pop(0)
    one = policy_all(init, data, up)
    two = policy_all(init, data, down)
    three = policy_all(init, data, None)
    print("{}: {:d}, {:d}, {:d}".format(text, one, two, three))


if __name__ == '__main__':
    try:
        evaluate('UUUDDUDU')
        evaluate('DUUDDUDU')
        evaluate('DUUaDUDU')
    except Exception as e:
        print(e)
