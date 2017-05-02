from functools import reduce
from itertools import chain, permutations, product
from . import Algorithm
from ..params import ops


class Naïve(Algorithm):

    def __init__(self, inputs, dest, exhaust=False):
        super().__init__(inputs, dest, exhaust)

    def run(self):
        for permuted in permutations(self.inputs):
            for operators in product(ops, repeat=len(permuted)-1):
                f_and_x = tuple(zip(operators, permuted[1:]))
                lhs = reduce(lambda x, fx: fx[0].fun(x, fx[1]),
                             f_and_x, permuted[0])
                if self.check_leaf(lhs):
                    expr = (permuted[0],) + tuple(chain.from_iterable(
                        (f, x) for f, x in f_and_x))
                    self.answers.append(expr)
                    if not self.exhaust:
                        return
