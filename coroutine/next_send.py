# 协程
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
    gen.close()
