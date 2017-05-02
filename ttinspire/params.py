from collections import namedtuple
import operator as opr

Op = namedtuple('Operation', ('sym', 'fun'))

ops = (Op('+', opr.add),
       Op('-', opr.sub),
       Op('*', opr.mul),
       Op('/', opr.truediv))

min_card = 1
max_card = 9
