# 
# author gino
# created on 2018/5/15


def grep(pattern):
    print('Looking for %s' % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


if __name__ == '__main__':
    g = grep('python')
    next(g)
    g.send("Yeah, but no, but yeah")
    g.send("python generators rock!")
    g.send("a series of tubes")
    g.close()
