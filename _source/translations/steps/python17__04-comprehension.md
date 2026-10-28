# 3. Comprehensions

Python has a special, elegant way to write "make one collection of data from another" – **comprehensions**.

## 1. List comprehensions

Here's a task: "pick out all the positive numbers in `nums`". The old way:

```python
nums = [-2, 1, -3, 4, 0, -5, 6]
positives = []
for x in nums:
    if x > 0:
        positives.append(x)
print(positives)
```

Output:

```
[1, 4, 6]
```

Four lines – to say one sentence: "collect every x in nums where x > 0 into a list".

A list comprehension turns that sentence straight into code:

```python
nums = [-2, 1, -3, 4, 0, -5, 6]
positives = [x for x in nums if x > 0]
print(positives)
```

Same output:

```
[1, 4, 6]
```

How to read it: "**collect `x`, for each `x` from `nums`, where `x > 0`**".

## 2. The general shape of a comprehension

```
[expression for variable in iterable if condition]
```

- **expression**: what to do to each item before collecting it (if nothing, just write the variable name)
- **for ... in**: which sequence to go through
- **if**: an optional filter – leave it out if you don't need it

A few examples:

```python no-run
# square every number
[x * x for x in [1, 2, 3, 4]]   # [1, 4, 9, 16]

# make everything capitals
[s.upper() for s in ['ab', 'cd']]  # ['AB', 'CD']

# squares of the even numbers
[x * x for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
```

## 3. Dict comprehensions

Doubling every value in a dictionary, the old way:

```python
prices = {'apple': 5, 'banana': 3, 'cherry': 10}
doubled = {}
for k, v in prices.items():
    doubled[k] = v * 2
print(doubled)
```

With a dict comprehension:

```python
prices = {'apple': 5, 'banana': 3, 'cherry': 10}
doubled = {k: v * 2 for k, v in prices.items()}
print(doubled)
```

The shape: `{key: value for variable in iterable}`.

## 4. When not to use a comprehension

Comprehensions feel great, but **shorter isn't always better**. If one comprehension is stuffed with:

- several `for` loops
- complicated conditions
- complicated expressions

then stop – go back to a plain `for` loop. A comprehension that doesn't fit on one line and takes three twists is much harder to read than a four-line for loop.

Remember this test: **if you can read it at a glance – use a comprehension; if you have to stop and translate it – use a for loop**.
