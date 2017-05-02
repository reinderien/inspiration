from math import fabs, factorial
from ..params import ops


class Algorithm:
    def __init__(self, inputs, dest, exhaust, n_leaves_worst=None):
        """
        Abstract algorithm parent
        :param inputs: The integers on the left-hand side of the equation
        :param dest: The integer on the right-hand side of the equation
        :param exhaust: Whether to find all answers (true) or only the first (false)
        :param n_leaves_worst: The worst-case search space size
        """
        self.inputs = [float(i) for i in inputs]
        self.dest = dest
        self.exhaust = exhaust
        self.answers = []
        self.n_leaves = 0
        if n_leaves_worst is None:
            # Default for Naïve and related algos
            n_leaves_worst = len(ops)**(len(inputs)-1) * factorial(len(inputs))
        self.n_leaves_worst = n_leaves_worst
        self.first_leaf = None

    def name(self):
        return self.__class__.__name__

    def print_full(self, check=False):
        """
        Print all answers determined during run(), in detail
        :param check: Whether to re-evaluate the expr while printing
        """
        if self.exhaust:
            print('%d answers' % len(self.answers))
        if len(self.answers):
            print('Index of first answer leaf: %d/%d (%.2g)' %
                  (self.first_leaf, self.n_leaves_worst, self.first_leaf/self.n_leaves_worst))

        for answer in self.answers:
            self.print_ans(answer, check)

    def print_ans(self, answer, check=False):
        """
        Print a single answer
        :param answer: An answer tuple, with interleaved x and op objects
        :param check: Whether to re-evaluate the expr while printing
        """
        it = iter(answer)
        val = next(it)
        print('%d ' % val, end='')
        for op in it:
            n = next(it)
            print('%s %d ' % (op.sym, n), end='')
            if check:
                val = op.fun(val, n)
        if not check:
            val = self.dest
        print('= %d' % val)

    def print_first(self, check=False):
        """
        Print only the first answer
        :param check: Whether to re-evaluate the expr while printing
        """
        if not len(self.answers):
            print('None')
            return
        self.print_ans(self.answers[0], check)

    def matches(self, lhs):
        """
        Check for equality between an evaluated LHS and the destination
        :param lhs: The float result of evaluating the LHS
        :return: True if the answer is close enough to be considered a match
        """
        return fabs(lhs - self.dest) < 1e-3

    def check_leaf(self, lhs):
        """
        Do some busywork when checking equality - count the number of leaves in the search tree 
        that were evaluated, and track the first leaf matched as an answer
        :param lhs: The float result of evaluating the LHS
        :return: True if the answer is close enough to be considered a match
        """
        self.n_leaves += 1
        if not self.matches(lhs):
            return False

        if self.first_leaf is None:
            self.first_leaf = self.n_leaves
        return True

from .naïve import Naïve
from .frecurse import Recurse
all_algos = (Naïve, Recurse)
