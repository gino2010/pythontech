# 
# author gino
# created on 2018/8/20
# up = 1, down = 0

up = 1
down = 0


def convert_str_number(text):
    text = text.upper()
    return [up if 'U' == item else down for item in text]


def policy_one_up(init, person):
    count = 0
    for item in person:
        count += init ^ item
        count += item ^ up
    return count


def policy_two_down(init, person):
    count = 0
    for item in person:
        count += init ^ item
        count += item ^ down
    return count


def policy_three_like(init, person):
    count = 0
    for item in person:
        count += init ^ item
        init = item
    return count


def policy_all(init, person, final):
    count = 0
    for item in person:
        count += init ^ item
        if final is None:
            init = item
        else:
            count += item ^ final
    return count


def evaluate(text):
    data = convert_str_number(text)
    init = data.pop(0)
    # one = policy_one_up(init, data)
    # two = policy_two_down(init, data)
    # three = policy_three_like(init, data)
    one = policy_all(init, data, up)
    two = policy_all(init, data, down)
    three = policy_all(init, data, None)
    print("{}: {:d}, {:d}, {:d}".format(init, one, two, three))


if __name__ == '__main__':
    evaluate('UUUDDUDU')
