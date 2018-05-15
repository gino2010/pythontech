# 
# author gino
# created on 2018/5/15


def coroutined(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr

    return start
