# dis_show_code.py

#!/usr/bin/env python3
# encoding: utf-8


def f(*args):
    nargs = len(args)
    print(nargs, args)


if __name__ == '__main__':
    import dis
    dis.show_code(f)
