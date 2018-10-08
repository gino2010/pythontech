# 
# author gino
# created on 2018/10/8
# 假设一组数字， 463175892 对其进行解密排序后 615947283
# 解密规则规则，移走第一个数字到末尾，取第二个数字，往复，直到全部取出。取出的数字序列则为结果
# 加密规则，与其逻辑相反


def decrypt(text: str) -> str:
    text_list = list(text)
    temp_str = ''
    while len(text_list) != 0:
        text_list.append(text_list.pop(0))
        temp_str += text_list.pop(0)
    return temp_str


def encrypt(text: str) -> str:
    text_list = list(text)
    temp_list = []
    while len(text_list) != 0:
        temp_list.insert(0, text_list.pop())
        temp_list.insert(0, temp_list.pop())

    return ''.join(temp_list)


if __name__ == '__main__':
    print("please input your text:")
    x = input()
    print("encrypt text: %s" % encrypt(x))
    print("original text: %s" % decrypt(encrypt(x)))
