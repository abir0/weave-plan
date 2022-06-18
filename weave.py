import sys
import math
from itertools import cycle
import numpy as np
from PIL import Image, ImageDraw


class Weave:
    Colors = {"1": "#000000",   # black
              "0": "#FFFFFF",   # white
              "r": "#DA344D",   # red
              "g": "#169873",   # green
              "b": "#0A369D",   # blue
              "y": "#F7EE7F",   # yellow
              "o": "#F26419",   # orange
              "v": "#4F345A",   # violet
              "p": "#F15BB5",   # pink
              "i": "#284B63",   # indigo
    }


    def __init__(self, formula_no, color_ratio, colors, dim, show_repeat, save):
        self.formula_no = self.parse_formula_number(formula_no)
        self.color_ratio = self.parse_color_ratio(color_ratio)
        self.color_order = self.parse_color_order(colors)
        self.repeat_size = self.find_repeat_size()

        self.dim = self.parse_dim(dim, show_repeat)
        self.save = save
        self.size = 50

        self.weave_plan = self.create_weave_plan()
        self.color_weave = self.weave_plan.copy()


    def parse_formula_number(self, formula_no):
        return formula_no.split("/")


    def parse_color_ratio(self, color_ratio):
        if not color_ratio:
            return []
        return color_ratio.split(":")


    def parse_color_order(self, colors):
        c_string = "oirgbyvp"
        if not self.color_ratio:
            return ""
        if len(self.color_ratio) > len(c_string):
            print(f"Color limit exceeded. Please use color ratio smaller than \
            {len(c_string)}.")
            return sys.exit()
        if not colors:
            colors = c_string[:len(self.color_ratio)]

        func = lambda x: int(x[0]) * x[1]
        return "".join(list(map(func, zip(self.color_ratio, colors))))


    def parse_dim(self, dim, show_repeat):
        if show_repeat:
            return self.repeat_size
        try:
            return int(dim), int(dim)
        except:
            if "x" in dim:
                dims = dim.split("x")
                return int(dims[0]), int(dims[1])
            else:
                print(f"Incorrent dimension shape syntax.")
                return sys.exit()


    def find_repeat_size(self):
        f = sum([int(i) for i in self.formula_no])
        if not self.color_ratio:
            return (f, f)
        else:
            c = sum([int(i) for i in self.color_ratio])
            return (math.lcm(f, c), math.lcm(f, c))


    def create_weave_plan(self):
        weave = []
        warp = ""

        for i, num in enumerate(self.formula_no):
            if i%2 == 0:
                warp += "1"*int(num)
            else:
                warp += "0"*int(num)

        warp = warp*math.ceil(self.dim[1]/len(warp))
        warp = warp[::-1]

        weave.append(list(warp))
        for i in range(len(warp)-1):
            warp = warp[1:] + warp[0]
            weave.append(list(warp))
        weave = np.array(weave)
        weave = weave.T

        weave = np.delete(weave,
                          np.s_[self.dim[0]:weave.shape[0]],
                          axis=0)
        weave = np.delete(weave,
                          np.s_[0:weave.shape[1]-self.dim[1]],
                          axis=1)

        return weave.tolist()


    def show_weave_plan(self):
        for i in range(self.dim[1]):
            for j in range(self.dim[0]):
                print(self.weave_plan[j][i], end =" ")
            print()


    def create_color_weave(self):
        if self.color_order == "":
            return
        weft = self.color_order

        weft = weft*math.ceil(self.dim[0]/len(weft))
        weft = weft[::-1]

        for i, row in enumerate(zip(self.weave_plan, weft)):
            for j, col in enumerate(zip(row[0], cycle(self.color_order))):
                if col[0] == "0":
                    self.color_weave[i][j] = col[1]
                if col[0] == "1":
                    self.color_weave[i][j] = row[1]


    def create_figure(self, dir="figs"):
        w, h = self.dim[0]*self.size+50, self.dim[1]*self.size+50
        self.image = Image.new("RGB", (w, h))

        for i, row in enumerate(self.weave_plan):
            for j, col in enumerate(row):
                shape = [(i*self.size+75, j*self.size+75),
                         ((i+1)*self.size-25, (j+1)*self.size-25)]
                img = ImageDraw.Draw(self.image)
                img.rectangle(shape,
                              fill=self.Colors[str(col)],
                              outline="#bbb",
                              width=2)

        if self.save:
            filename = "{}/{}_{}({}x{}).jpg".format(dir,
                                                    "".join(self.formula_no),
                                                    self.color_order,
                                                    self.dim[0],
                                                    self.dim[1])
            with open(filename, "w") as file:
                self.image.save(file)
        else:
            self.image.show()
