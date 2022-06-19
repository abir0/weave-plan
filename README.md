# Weave plan
Generate weave plan from formula no and color ratios.


### Dependencies

- [numpy](https://pypi.org/project/numpy/)
- [Pillow](https://pypi.org/project/Pillow/) (fork of PIL or Python Imaging Library)


### Features

- Construction of plain, twill, satin or any other weave plan from formula number e.g. 4 up, 3 down.
- Create color and weave effect from color ratio(s) along with formula number e.g. 1 up, 1 down and 2:2 color ratio.
- Find out the repeat unit of the specified types of weave plan.
- Create the weave plan of any desired shape.
- Save the weave plan in JPEG file format.


### Usage

This program has the following arguments:

```
usage: planner.py [-h] [-fn FORMULA_NO] [-cr COLOR_RATIO] [-c COLORS] [-d DIM] [-r] [-s]

optional arguments:
  -h, --help                                    show this help message and exit
  -fn FORMULA_NO, --formula-no FORMULA_NO       input formula number
  -cr COLOR_RATIO, --color-ratio COLOR_RATIO    input color ratio
  -c COLORS, --colors COLORS                    input color string
  -d DIM, --dim DIM                             input shape
  -r, --show-repeat                             show repeat unit
  -s, --save                                    save as image
```

#### Formula number

The formula number is the numerical description of the weave repeat unit. This program takes the formula no from the `-fn` or `--formula-no` flag. The input sequence of numbers separated by `/` represent the formula number. Numbers in odd sequence represent the warp threads up and the even sequence represent the weft threads up or warp thread down e.g. input `3/2` represents 3 up, 2 down.

#### Color ratio

The color ratio is the number and order of different colors of threads in both warp and weft direction. This program takes the color ratio from the `-cr` or `--color-ratio` flag. It is represented by the sequence of numbers separated by `:`. So `3:2` color ratio means two different colors are used and 3 threads of the first color is followed by 2 threads of the second color. This order of coloring is repeated in both warp and weft direction.

**Suported colors:**

| Symbol | Color  | Hex code |
|--------|--------|----------|
| `0`    | black  | #000000  |
| `1`    | white  | #FFFFFF  |
| `r`    | red    | #DA344D  |
| `g`    | green  | #169873  |
| `b`    | blue   | #0A369D  |
| `y`    | yellow | #F7EE7F  |
| `o`    | orange | #F26419  |
| `v`    | violet | #4F345A  |
| `p`    | pink   | #F15BB5  |
| `i`    | indigo | #284B63  |


#### Example usage

The command below produces 2 up, 2 down weave construction with 4:4 color ratio of indigo and orange colored threads in both warp and weft direction. This is known as Hound's Tooth Weave. The output is a JPEG file, generated in the [figs](./figs/) folder.

```bash
python planner.py -fn 2/2 -cr 6:6 -d 30 -s
```

Output:

<p align="center">
  <img src=".\figs\22_44.jpg" width="400px"><br>
  <i> Hound's Tooth Weave </i>
</p>
