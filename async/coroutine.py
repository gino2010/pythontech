# 
# author gino
# created on 2018/4/21


# yield next and send
def generator():
    print('    generator start.....')
    yield 'first'
    print('    generator after first.....')
    n = yield 'second'
    print('    generator after second.....%s' % n)
    yield 'finished'


def grep(pattern):
    print('Looking for %s' % pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    print('ready to create generator')
    gen = generator()
    print('ready to call next')
    t = next(gen)
    print('after call next, return: %s' % t)
    print('ready to call next again')
    t = next(gen)
    print('after call next again, return: %s' % t)
    print('ready to call send')
    t = gen.send('outside')
    print('all %s' % t)

    g = grep('python')
    next(g)
    g.send("Yeah, but no, but yeah")
    g.send("python generators rock!")
    g.send("a series of tubes")

    c = consumer()
    produce(c)
