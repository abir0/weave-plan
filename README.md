# Weave plan
Generate weave plan from formula no and color ratios.

### Dependencies

- [Pillow](https://pypi.org/project/Pillow/) (PIL or Python Imaging Library fork) 

### Usage

This program has the following arguments:

```
usage: weave.py [-h] [-f FORMULA] [-d DIM] [-c COLOR] [-s]

optional arguments:
  -h, --help                       show this help message and exit
  -f FORMULA, --formula FORMULA    input formula number
  -d DIM, --dim DIM                input n-dimension
  -c COLOR, --color COLOR          input n-dimension
  -s, --save                       input n-dimension
```

#### Example usage

```bash
python weave.py -f 11 -c iioo -d 20 -s
```
Output:

The command above will generate this weave pattern in the [figs](./figs/) folder.
<p align="center">
  <img src=".\figs\11_iioo(20x20).jpg" width="400px"><br>
  <i> Crows foot weave </i>
</p>
