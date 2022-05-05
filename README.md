# Weave plan
Generate weave plan from formula no and color ratios.


### Dependencies

- [Pillow](https://pypi.org/project/Pillow/) (fork of PIL or Python Imaging Library)


### Features

- Construction of  plain, twill, satin or any other weave plan from formula number e.g. 4 up, 3 down.
- Create color weave plan from color ratio along with formula number e.g. 1 up, 1 down and 2:2 color ratio.
- Make the weave plan of any desired shape.
- Save the weave plan in JPEG file format.


### Usage

This program has the following arguments:

```
usage: planner.py [-h] [-f FORMULA] [-d DIM] [-c COLOR] [-s]

optional arguments:
  -h, --help                       show this help message and exit
  -f FORMULA, --formula FORMULA    input formula number
  -d DIM, --dim DIM                input shape
  -c COLOR, --color COLOR          input color ratio
  -s, --save                       save as image
```

#### Formula number

The formula number is the numerical description of the weave repeat unit. This program takes the formula no as input from the `-f` or `--formula` flag. The input sequence of numbers (1 to 9) represent the formula no. Odd sequence of numbers represent the warp threads up and the even sequence represent the warp threads down e.g. input `3112` will represent 3 up, 1 down, 1 up, 2 down.

#### Color ratio

The color ratio is the number of different colors of threads in both warp and weft direction. This program takes the color ratio as input from the `-c` or `--color` flag. It is represented as the sequence of alphabets, each of which corresponds to a hex color code. This can be given as a sequence of alphabets e.g. `rrbb` where _r_ and _b_ corresponds to red and blue respectively and the sequence of these represent the color ratio, so in this case it represents 2:2 color ratio of red and blue in both warp and weft direction. Another way to do this is to put the number in front or back of the alphabet to represent the number of time they repeat e.g. `3r4b` is equivalent to `rrrbbbb`.

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

The command below produces 1 up, 1 down weave construction with 2:2 color ratio of indigo and orange colored threads in both warp and weft direction. This is also known as Crows Foot Weave. The output is generated in the [figs](./figs/) folder as a JPEG image file.

```bash
python planner.py -f 11 -c 2i2o -d 20 -s
```

Output:

<p align="center">
  <img src=".\figs\11_iioo(20x20).jpg" width="400px"><br>
  <i> Crows Foot Weave </i>
</p>
