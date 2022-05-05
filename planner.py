import argparse
from weave import Weave


def planner():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--formula", type=str, default="11",
                        help="input formula number")
    parser.add_argument("-d", "--dim", type=int, default=10,
                        help="input shape")
    parser.add_argument("-c", "--color", type=str, default="",
                        help="input color ratio")
    parser.add_argument("-s", "--save", action='store_true',
                        help="save as image")
    args = parser.parse_args()

    weave = Weave(args.formula, args.dim, args.color, args.save)

    weave.show_weave_plan()
    weave.create_color_weave()
    weave.create_figure()


if __name__ == '__main__':
    planner()
