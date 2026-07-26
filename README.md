# rmcm - remove (python) comments

this is a simple script to remove comments and docstrings from python files.

I (well mainly claude) made this after I spent too much time removing coments from the code I had to turn in for my classes.

## Usage

WARNING: make sure to have a backup in case anything goes wrong. To my knowledge it should only flag docstrings as docstrings but if you have a ''' or """ on its own without a , or [ or ( or { at the end of the last non-whitespace line, it will flag it as a docstring as well however that might happen.

clone the repo:

```bash
git clone https://github.com/.thecosmomancer/rmcm.git
```

run with python:

```bash
python rmcm.py -i {input_file} -o {output_file}
```

or:

```bash
python rmcm.py -Oi {input_file}
```

to overwrite the input file
# License

[MIT.](https://choosealicense.com/licenses/mit/) I hate long licensing texts.