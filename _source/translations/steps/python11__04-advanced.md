# 3. Custom types, @unique, auto()

## 1. Values can be any type

An `Enum` member's value doesn't have to be a number – strings, tuples and objects all work:

```python
from enum import Enum

class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    # ...
    Dec = 'December'

print(Month.Jan)         # Month.Jan
print(Month.Jan.name)    # 'Jan'
print(Month.Jan.value)   # 'January'
```

## 2. @unique: no repeated values

By default, an Enum **allows** several members to have the same value – the later one becomes another name (an alias) for the earlier one.

```python
from enum import Enum

class Color(Enum):
    RED = 1
    SCARLET = 1   # no error – SCARLET becomes another name for RED

print(Color.SCARLET is Color.RED)   # True
```

If you don't want that, add the `@unique` decorator. It forces every value to be unique and raises an error straight away if one repeats:

```python no-run
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # SCARLET = 1   ← adding this line gives a ValueError
```

## 3. auto(): let Python choose the values

Lots of members, and you don't care what the actual values are? Use `auto()` to let Python assign them:

```python
from enum import Enum, auto

class Weekday(Enum):
    MON = auto()
    TUE = auto()
    WED = auto()
    THU = auto()
    FRI = auto()
    SAT = auto()
    SUN = auto()

print(Weekday.MON.value)   # 1
print(Weekday.SUN.value)   # 7
```

`auto()` starts at 1 and counts up by default. To change the starting value or the step, you can override the `_generate_next_value_` method (an advanced trick – skip it for now).

## 4. IntEnum / StrEnum

If you want Enum members to **also be ints** (so they can do arithmetic and be compared with ints), use `IntEnum`:

```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MID = 5
    HIGH = 10

print(Priority.LOW < Priority.HIGH)   # True
print(Priority.MID + 1)               # 6
```

`StrEnum` (Python 3.11+) is the same idea for strings.
