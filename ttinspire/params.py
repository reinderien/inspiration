from collections import namedtuple

Op = namedtuple('Operation', ('sym', 'fun'))

ops = (Op('+', lambda x, y: x + y),
       Op('-', lambda x, y: x - y),
       Op('*', lambda x, y: x * y),
       Op('/', lambda x, y: x / y))

min_card = 1
max_card = 9
