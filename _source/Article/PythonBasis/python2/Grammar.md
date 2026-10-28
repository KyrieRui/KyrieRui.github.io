# 1. A Quick Look at Python Syntax #

Every language has its own grammar (syntax) – both human languages (like English and Chinese) and computer programming languages.

Python is no different. It has its own syntax rules. The interpreter takes code that follows these rules, turns it into machine code that the CPU can run, and then runs it.

Python's syntax is fairly simple. It uses **indentation** (spaces at the start of a line).

```python
# Check whether a number is positive (or zero)
a = 88
if a >= 0:
    print('yes')
else:
    print('NO')
```

Output:

```
yes
```

In the code above, a line starting with `#` is a **comment**. Every other line is a **statement**. When a statement ends with a colon `:`, the indented lines below it form a **code block**.

Note that Python is **case-sensitive**. If you use the wrong capital or small letter, the program will give an error.

For more details, see the earlier article: [Quick Overview of Python Code Style](../../codeSpecification/codeSpecification_first.md)

