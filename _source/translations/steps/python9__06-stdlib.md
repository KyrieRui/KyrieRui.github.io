# 5. A few commonly used standard library modules

These standard library modules come up **all the time** in everyday programming. Let's meet them first – the exercises below use them too.

## 1. math – maths functions

```python
import math

print(math.pi)          # pi, 3.141592653589793
print(math.e)           # the constant e
print(math.sqrt(16))    # square root → 4.0
print(math.floor(3.7))  # round down → 3
print(math.ceil(3.2))   # round up → 4
```

## 2. random – random numbers

```python
import random

random.seed(42)              # fix the random seed so the results repeat
print(random.randint(1, 10)) # a random whole number from 1 to 10 (both included)
print(random.choice(['A', 'B', 'C']))  # pick one at random
```

> In the exercises we use `random.seed(...)` to fix the results – that way the output is stable when it's checked.

## 3. datetime – dates and times

```python
from datetime import date, datetime

d = date(2026, 1, 1)
print(d.year, d.month, d.day)  # 2026 1 1

now = datetime(2026, 1, 1, 12, 30, 0)
print(now)                     # 2026-01-01 12:30:00
```

## 4. json – turning data into JSON

Turn a Python dictionary / list into a JSON string:

```python
import json

data = {'name': 'Alice', 'age': 18}
print(json.dumps(data))
```

Output:

```
{"name": "Alice", "age": 18}
```

And the other way round – parse a JSON string back into a Python object:

```python
import json

s = '{"name": "Alice", "age": 18}'
obj = json.loads(s)
print(obj['name'])   # Alice
```

---

Now let's practise. Every exercise needs you to **use an import statement** to bring in the right standard library module.
