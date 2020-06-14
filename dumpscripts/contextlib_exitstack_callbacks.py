# contextlib_exitstack_callbacks.py

import contextlib


def callback(*args, **kwds):
    print('callback di chiusura({}, {})'.format(args, kwds))


with contextlib.ExitStack() as stack:
    stack.callback(callback, 'arg1', 'arg2')
    stack.callback(callback, arg3='val3')
