def parse():
    from argparse import ArgumentParser

    parser = ArgumentParser(
        prog='python -m ttinspire',
        description='Explore the PyCon 2015 Thumbtack Inspiration Challenge')
    parser.add_argument(dest='inputs', metavar='n', type=int, nargs='+',
                        help='LHS integers to permute')
    parser.add_argument(dest='desired', metavar='d', type=int, nargs=1,
                        help='Desired RHS integer')
    return parser.parse_args()


def once(inputs, desired, exhaust=False):
    # Attempt a single problem with a non-exhaustive solution
    from .algos.naïve import Naïve

    n = Naïve(inputs, desired, exhaust)
    n.run()
    n.print_full()


def run_cli():
    # Regular run of the CLI with parsed args
    args = parse()
    once(args.inputs, args.desired)


def find_tough(count):
    # Look for difficult inputs (taking a long time to get a first answer)

    from .algos.naïve import Naïve
    from .params import min_card, max_card

    slowest = 0

    def recurse(cards=(), depth=0):
        if depth == count:
            inputs = cards[:-1]
            dest = inputs[-1]
            algo = Naïve(inputs, dest, exhaust=False)
            algo.run()
            nonlocal slowest
            if algo.answers and slowest < algo.first_leaf:
                print('Tried ', inputs, '=', dest)
                slowest = algo.first_leaf
                algo.print_full(check=True)
        else:
            for x in range(min_card, max_card+1):
                recurse(cards+(x,), depth+1)

    recurse()
