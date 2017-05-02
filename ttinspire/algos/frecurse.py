from itertools import permutations
from . import Algorithm
from ..params import ops


class Recurse(Algorithm):

    def __init__(self, inputs, dest, exhaust=False):
        super().__init__(inputs, dest, exhaust)

    def recurse(self, val_so_far, expr, operands):
        """
        Recurse brute-force through operations
        :param val_so_far: the value from the left to here
        :param expr: the expression from the left to here
        :param operands: the inputs from here to the right
        :return: true to halt
        """
        if not operands:
            if self.check_leaf(val_so_far):
                self.answers.append(expr)
                return not self.exhaust
            return False
        for op in ops:
            halt = self.recurse(
                val_so_far=op.fun(val_so_far, operands[0]),
                expr=expr + (op, operands[0]),
                operands=operands[1:])
            if halt:
                return halt

    def run(self):
        for permuted in permutations(self.inputs):
            halt = self.recurse(
                val_so_far=permuted[0],
                expr=(permuted[0],),
                operands=permuted[1:])
            if halt and not self.exhaust:
                return
