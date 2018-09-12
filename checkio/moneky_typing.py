# 
# author gino
# created on 2018/9/12
# https://py.checkio.org/en/mission/monkey-typing/


def checkio(text: str, words: set) -> int:
    # count = 0
    # text = text.lower()
    # for item in words:
    #     if item.lower() in text:
    #         count += 1
    # return count
    return sum(w.lower() in text.lower() for w in words)


if __name__ == '__main__':
    print(checkio("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
    print(checkio("Bananas, give me bananas!!!", {"banana", "bananas"}))
    print(checkio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}))
