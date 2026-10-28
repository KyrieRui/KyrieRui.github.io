# 1. Quick Overview

## 1. Encoding

* Unless there is a special reason, always save files in UTF-8 encoding.
* Unless there is a special reason, put `#-*-coding:utf-8-*-` at the top of the file.

## 2. Code Layout

### 2.1 Indentation

* Always use 4 spaces for indentation.

### 2.2 Line Length

Try to keep each line under 80 characters. (In special cases it can be a bit longer than 80, but never more than 120.)

Why:

* It helps when you compare two versions of code side by side.
* It's easier to read code in a terminal window.
* A line that is too long may mean the design has a problem.

### 2.3 Quotes

Simply put: use double quotes for human language, and single quotes for machine labels. So **in code**, you should mostly use **single quotes**.

 * ***Human language*** **uses double quotes** `"..."`  
   For example, error messages. In many cases this is unicode, written as `u"Hello world"`
 * ***Machine labels*** **use single quotes** `'...'`
   For example, the keys in a dict
 * ***Regular expressions*** **use raw double quotes** `r"..."`
 * ***Documentation strings (docstrings)*** **use three double quotes** `"""......"""`

### 2.4 Blank Lines

* Leave two blank lines between top-level functions and class definitions.
* Leave one blank line between methods inside a class.

```python
class A:

    def __init__(self):
        pass

    def hello(self):
        pass


def main():
    pass   
```

* You can use several blank lines to separate groups of related functions.
* Inside a function, you can use blank lines to separate parts of the logic.


## 3. import Statements

* Write each import on its own line.

```python
# Correct
import os
import sys

# Not recommended
import sys,os

# Correct
from subprocess import Popen, PIPE
```
* Use **absolute** imports.

<!-- skip-ci -->
```python
# Correct
from foo.bar import Bar

# Not recommended
from ..bar import Bar
```

* Put imports at the top of the file, after the module description and docstring, and before global variables.
* Put imports in order, with one blank line between each group.

<!-- skip-ci -->
```python
import os
import sys

import msgpack
import zmq

import foo
```

* When you import a class from another module, you can use a relative import.

<!-- skip-ci -->
```python
from myclass import MyClass
```

* If two names clash, use the namespace (the module name) to tell them apart.

<!-- skip-ci -->
```python
import bar
import foo.bar

bar.Bar()
foo.bar.Bar()
```

## 4. Spaces

* Put one space on each side of a binary operator `[=,-,+=,==,>,in,is not, and]`:

<!-- skip-ci -->
```python
# Correct
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Not recommended
i=i+1
submitted +=1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```

* In a function's parameter list, put a space after each `,`

```python
# Correct
def complex(real, imag):
    pass

# Not recommended
def complex(real,imag):
    pass
```

* In a function's parameter list, do **not** put spaces around the `=` of a default value.

```python
# Correct
def complex(real, imag=0.0):
    pass

# Not recommended
def complex(real, imag = 0.0):
    pass
```

* Don't add extra spaces right after an opening bracket or right before a closing bracket.

<!-- skip-ci -->
```python
# Correct
spam(ham[1], {eggs: 2})

# Not recommended
spam( ham[1], { eggs : 2 } )
```

* Don't put extra spaces before the opening bracket of an index.

<!-- skip-ci -->
```python
# Correct
dict['key'] = list[index]

# Not recommended
dict ['key'] = list [index]
```

* Don't add extra spaces just to line up `=` signs.

```python
# Correct
x = 1
y = 2
long_variable = 3

# Not recommended
x             = 1
y             = 2
long_variable = 3
```

## 5. Line Breaks

Python lets you break a line inside brackets. There are two ways to do it.

1) Line the second line up with the opening bracket.

<!-- skip-ci -->
```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
```

2) Indent the second line by 4 spaces. Use this when you break the line right after the opening bracket.

```python
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```

You can also use a backslash `\` to break a line. Binary operators like `+` and `.` should go at the end of the line. Long strings can be broken this way too.

<!-- skip-ci -->
```python
session.query(MyTable).\
        filter_by(id=1).\
        one()

print 'Hello, '\
      '%s %s!' %\
      ('Harry', 'Potter')
```

Don't write compound statements – that means don't put several statements on one line:

<!-- skip-ci -->
```python
# Correct
do_first()
do_second()
do_third()

# Not recommended
do_first();do_second();do_third();
```

`if/for/while` must always start a new line for their body:

<!-- skip-ci -->
```python
# Correct
if foo == 'blah':
    do_blah_thing()

# Not recommended
if foo == 'blah': do_blash_thing()
```

## 6. docstring
The two most basic docstring rules:

1. Every public module, function, class and method should have a docstring. Private methods don't need one, but you should put a block comment after the `def` to explain them.
2. The closing `"""` of a docstring should be on its own line, unless the whole docstring fits on one line.

```python
"""Return a foobar
Optional plotz says to frobnicate the bizbaz first.
"""

"""Oneline docstring"""
```
