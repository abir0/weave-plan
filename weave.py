import argparse
import math
from itertools import cycle
from PIL import Image, ImageDraw


class Weave:
    Colors = {"0": "#000000",
              "1": "#ffffff",
              "r": "#DA344D",
              "g": "#169873",
              "b": "#0A369D",
              "y": "#F7EE7F",
              "o": "#F26419",
              "v": "#4F345A",
              "p": "#F15BB5",
              "i": "#284B63",
    }

    def __init__(self, formula, dim, color, save):
        self.formula = str(formula)
        self.dim = int(dim)
        self.color = str(color).lower()
        self.save = save
        self.size = 50

        self.weave_plan = list()
        self.create_weave_plan()
        self.color_weave = self.weave_plan.copy()

    def show_weave_plan(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.weave_plan[i][j], end =" ")
            print()

    def create_weave_plan(self):
        arr = []
        col = ""

        for i, f in enumerate(list(self.formula)):
            if i%2 == 0:
                col += "0"*int(f)
            else:
                col += "1"*int(f)
        length = sum([int(i) for i in self.formula])
        col = col*math.ceil(self.dim/length)
        col = col[::-1]

        arr.append(list(col))
        for i in range(len(col)-1):
            col = col[1:] + col[0]
            arr.append(list(col))

        for i in range(len(arr)):
            arr[i] = arr[i][:self.dim]
        arr = arr[len(arr)-self.dim:]

        self.weave_plan = arr

    def create_color_weave(self):
        if self.color == "":
            # print("colorless weave")
            return
        weft = self.color

        length = len(weft)
        weft = weft*math.ceil(self.dim/length)
        weft = weft[:self.dim]
        weft = weft[::-1]

        for i, row in enumerate(zip(self.weave_plan, weft)):
            for j, col in enumerate(zip(row[0], cycle(self.color))):
                if col[0] == "1":
                    self.color_weave[i][j] = col[1]
                if col[0] == "0":
                    self.color_weave[i][j] = row[1]

        # for i in range(self.dim):
        #     for j in range(self.dim):
        #         print(self.color_weave[i][j], end =" ")
        #     print()

    def create_figure(self):
        w, h = self.dim*self.size+50, self.dim*self.size+50
        self.image = Image.new("RGB", (w, h))

        for i, row in enumerate(self.weave_plan):
            for j, col in enumerate(row):
                shape = [(i*self.size+75, j*self.size+75),
                         ((i+1)*self.size-25, (j+1)*self.size-25)]
                img = ImageDraw.Draw(self.image)
                img.rectangle(shape, fill=self.Colors[col], outline="#EBE9E9")

        if self.save:
            filename = "figs/{}_{}({}x{}).jpg".format(self.formula, self.color,
                                                      self.dim, self.dim)
            with open(filename, "w") as file:
                self.image.save(file)
        else:
            self.image.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--formula", type=str, default="11",
                        help="input formula number")
    parser.add_argument("-d", "--dim", type=int, default=10,
                        help="input n-dimension")
    parser.add_argument("-c", "--color", type=str, default="",
                        help="input n-dimension")
    parser.add_argument("-s", "--save", action='store_true',
                        help="input n-dimension")
    args = parser.parse_args()

    weave = Weave(args.formula, args.dim, args.color, args.save)

    weave.show_weave_plan()
    weave.create_color_weave()
    weave.create_figure()


if __name__ == '__main__':
    main()
