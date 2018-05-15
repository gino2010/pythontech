# 
# author gino
# created on 2018/5/15
from coroutine import coroutined


@coroutined
def grep(pattern):
    print('Looking for %s' % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("done")


if __name__ == '__main__':
    g = grep('python')
    g.send("python line")
