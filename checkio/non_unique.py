# 
# author gino
# created on 2018/8/6


def checkio(data: list) -> list:
    # l = []
    # for item in data:
    #     if data.count(item) > 1:
    #         l.append(item)
    # return l
    filter(lambda i: data.count(i) - 1, data)

    return [item for item in data if data.count(item) > 1]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
