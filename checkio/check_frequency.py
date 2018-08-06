# 
# author gino
# created on 2018/8/5
import string


def checkio(text: str) -> str:
    # temp = {}
    # for item in text.lower():
    #     if item.isalpha():
    #         temp[item] = temp.get(item, 0) + 1
    #
    # temp_list = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
    # return temp_list[0][0]

    return max(string.ascii_lowercase, key=text.lower().count)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
