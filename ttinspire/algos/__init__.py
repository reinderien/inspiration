class Algorithm:
    def __init__(self, inputs, dest, exhaust, n_leaves_worst):
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
        self.n_leaves_worst = n_leaves_worst
        self.first_leaf = None

    def print_full(self, check=False):
        if self.exhaust:
            print('%d answers' % len(self.answers))
        if len(self.answers):
            print('Index of first answer leaf: %d/%d (%.2g)' %
                  (self.first_leaf, self.n_leaves_worst, self.first_leaf/self.n_leaves_worst))

        for answer in self.answers:
            self.print_ans(answer, check)

    def print_ans(self, answer, check=False):
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
        if not len(self.answers):
            print('None')
            return
        self.print_ans(self.answers[0], check)
