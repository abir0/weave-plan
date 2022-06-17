import argparse
from weave import Weave


def planner():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fn", "--formula-no", type=str, default="1/1",
                        help="input formula number")
    parser.add_argument("-cr", "--color-ratio", type=str, default="",
                        help="input color ratio")
    parser.add_argument("-c", "--colors", type=str, default="",
                        help="input color string")
    parser.add_argument("-d", "--dim", type=str, default="10x10",
                        help="input shape")
    parser.add_argument("-r", "--show-repeat", action='store_true',
                        help="show repeat unit")
    parser.add_argument("-s", "--save", action='store_true',
                        help="save as image")
    args = parser.parse_args()

    weave = Weave(args.formula_no,
                  args.color_ratio,
                  args.colors,
                  args.dim,
                  args.show_repeat,
                  args.save)

    # weave.show_weave_plan()
    weave.create_color_weave()
    weave.create_figure()


if __name__ == '__main__':
    planner()
