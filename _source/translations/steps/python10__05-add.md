# 5. `__add__`: letting objects use `+`

Python's `+` means different things for different types:

- `1 + 2` → `3` (adding numbers)
- `'a' + 'b'` → `'ab'` (joining strings)
- `[1] + [2]` → `[1, 2]` (joining lists)

None of this is "hard-wired" into Python – each of these classes has its own `__add__`. We can make our own classes support `+` too.

## 2D vector addition with `__add__`

```python
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vec2({self.x}, {self.y})'

v1 = Vec2(1, 2)
v2 = Vec2(3, 4)
v3 = v1 + v2     # triggers v1.__add__(v2)
print(v3)        # Vec2(4, 6)
```

Note: `__add__` usually **returns a new object** instead of changing `self`. It's the same reason `1 + 2` doesn't change `1`.

## The whole family of arithmetic operators

| You write | Magic method |
|---|---|
| `a + b` | `__add__` |
| `a - b` | `__sub__` |
| `a * b` | `__mul__` |
| `a / b` | `__truediv__` |
| `a // b` | `__floordiv__` |
| `a % b` | `__mod__` |
| `a ** b` | `__pow__` |
| `-a` | `__neg__` |
| `abs(a)` | `__abs__` |

## And there's more

There are lots of magic methods – this section only covers the most common ones to get you started. Look these up when you need them later:

| Magic method | When it's triggered |
|---|---|
| `__call__` | Lets an object be called **like a function**: `obj()` |
| `__iter__` / `__next__` | Custom iterators |
| `__enter__` / `__exit__` | Context managers for the `with` statement |
| `__getattr__` / `__setattr__` | Intercepting attribute access |
| `__new__` | Controlling how an object is **created** (before `__init__`) |

## Summary of this section

- Magic methods are special methods named like `__name__`, called by Python automatically
- `__str__` / `__repr__`: decide how an object becomes a string
- `__eq__` and friends: decide how comparisons work
- `__len__` / `__getitem__`: make an object behave like a container
- `__add__` and friends: let an object do arithmetic

Next, do the exercises and write these magic methods yourself.
