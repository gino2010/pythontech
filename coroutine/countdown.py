#
# author gino
# created on 2018/5/15


# Calling a generator function creates an generator object.
# However, it does not start running the function until call next or send
def countdown(n):
    print("Counting down from", n)
    while n > 0:
        yield n
        n -= 1
    print("\nDone counting down")


if __name__ == '__main__':
    for i in countdown(10):
        print(i, end=' ')
