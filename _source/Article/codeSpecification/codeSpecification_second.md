# 2. Comments

## 1. Comments

### 1.1 Block Comments
Put one space after the `#`. Separate paragraphs with an empty comment line (which still needs a `#`).

```python
# Block comment
# Block comment
#
# Block comment
# Block comment
```

### 1.2 Inline Comments
Leave at least two spaces between the code and the comment. Don't write comments that say nothing useful.

<!-- skip-ci -->
```python
# Correct
x = x + 1  # Make the border one pixel thicker

# Not recommended (a useless comment)
x = x + 1 # add 1 to x
```

### 1.3 Tips

* In important parts of your code (or tricky parts), try to write comments whenever you can.

* For really important comments, put lines of `=` around them so they stand out.

<!-- skip-ci -->
```python
app = create_app(name, options)


# =====================================
# Do NOT add get/post app routes here !!!
# =====================================


if __name__ == '__main__':
    app.run()
```

## 2. Documentation Comments (Docstrings)
A docstring is usually placed at the top of a module, function or class. Python can then read it through the object's `__doc__` attribute.
Editors and IDEs can also use docstrings to show helpful hints.

* A docstring starts and ends with `"""`. Don't break the line right after the opening quotes. If it has several lines, the closing quotes must be on a new line. Here is an example in Google's docstring style:

```python
# -*- coding: utf-8 -*-
"""Example docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.
"""
```

* Don't just copy the function's signature into the docstring. Instead, describe what it does, and explain the parameters and return value.

<!-- skip-ci -->
```python
#  Not recommended (don't just repeat the signature)
def function(a, b):
    """function(a, b) -> list"""
    ... ...


#  Correct
def function(a, b):
    """Work out and return the average of the data from a to b"""
    ... ...
```

* Describe parameters and return values using the numpy style, like this:

```python
def func(arg1, arg2):
    """Write a one-sentence summary here (e.g. Calculate the average).

    Write the detailed description here.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : int
        Description of arg2

    Returns
    -------
    int
        Description of the return value

    See Also
    --------
    otherfunc : other related functions...

    Examples
    --------
    Examples use doctest format. Code after `>>>` can be run automatically
    as test cases by doc-testing tools.

    >>> a=[1,2,3]
    >>> print [x + 3 for x in a]
    [4, 5, 6]
    """
```


* Docstrings can be in any language, but don't mix two languages in one docstring.

* Longer is not better. Usually one or two sentences are enough to explain things.

* Modules, public classes and public methods should have docstrings whenever possible.


