# 2. `__str__` and `__repr__`: making print friendly

First, a problem. Let's write a very ordinary `Book` class:

```python
class Book:
    def __init__(self, title):
        self.title = title

b = Book('Python Basics')
print(b)
```

What's the output?

```
<__main__.Book object at 0x10a9f3d50>
```

A string of ✗ gibberish. By default, `print(obj)` calls `object`'s `__str__`, which only tells you "this is a Book object at address 0x..." – useless information for a human.

## 1. `__str__`: a string for people

Let's override it:

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'Book: {self.title}'

b = Book('Python Basics')
print(b)         # Book: Python Basics
print(str(b))    # Book: Python Basics
```

`__str__` must return a **string**. Both `print(obj)` and `str(obj)` call it.

## 2. `__repr__`: a string for programmers

`__repr__` also returns a string, but it's for something different: usually a way of writing the object that's **for developers, ideally one that could recreate the object**.

The classic cases are typing a variable's name straight into an interactive terminal, or putting objects in a list and printing it:

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f'Book: {self.title}'

    def __repr__(self):
        return f"Book(title={self.title!r})"

b = Book('Python Basics')
print(b)        # Book: Python Basics  ← uses __str__
print([b])      # [Book(title='Python Basics')]  ← inside a container, uses __repr__
```

Note:

- If you only define `__repr__` and not `__str__`, `print(obj)` **falls back** to `__repr__`
- It doesn't work the other way round – if you only define `__str__`, `[obj]` still shows the default gibberish

> Rule of thumb: **write `__repr__` first**. Then think about whether to add a friendlier `__str__`.
