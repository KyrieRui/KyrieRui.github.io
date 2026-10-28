# 2. set #

A Python **set** is like sets in other languages: an **unordered** collection with **no duplicate** elements. Its main jobs are testing relationships between groups and removing duplicates.

A set is like a dict, but a set doesn't store values – only keys.


## 1. Creating a set ##

To create a set, you can give it a list:

```python
set1=set([123,456,789])
print(set1)
```

Output:

```
{456, 123, 789}
```

The argument `[123,456,789]` is a list. The output `{456, 123, 789}` just tells you the set holds the 3 elements 456, 123 and 789. The order shown is different from the order in your list. This shows that a set has **no order**.

Also, notice the output is inside curly braces. From what we've learned: a tuple uses round brackets, a list uses square brackets, and a dict uses curly braces. A dict stores key-value pairs, while you can think of a set as storing only keys.

> Note the version difference here: since Python 3.7, a normal dict keeps the order keys were added. A set still does **not** keep insertion order. And a dict keeping order is not the same as sorting the keys.

Remember: when creating a dict, a repeated key gets overwritten by the later key-value pair. In a set, repeated elements are **automatically filtered out**.


```python
set1=set([123,456,789,123,123])
print(set1)
```

Output:

```
{456, 123, 789}
```

## 2. Adding Elements to a set ##

Use the `add(key)` method to add an element to a set. You can add the same thing again, but it has no effect.

```python
set1=set([123,456,789])
print(set1)
set1.add(100)
print(set1)
set1.add(100)
print(set1)
```

Output:
```
{456, 123, 789}
{456, 123, 100, 789}
{456, 123, 100, 789}
```

## 3. Removing Elements from a set ##

Use the `remove(key)` method to remove an element from a set.

```python
set1=set([123,456,789])
print(set1)
set1.remove(456)
print(set1)
```

Output:

```
{456, 123, 789}
{123, 789}
```


## 4. Using sets ##

Because a set is an unordered collection with no duplicates, two sets can do maths operations like **union**, **intersection** and **difference**.

Think of them with a Venn diagram:

- **Union**: both circles are fully coloured in – all the elements from both sets together
- **Intersection**: only the middle part where the circles overlap is coloured – elements that are in **both** sets
- **Difference**: only the first circle, minus the part that overlaps the second – elements in the first set but **not** in the second

Example:

```python
set1=set('hello')
set2=set(['p','y','y','h','o','n'])
print(set1)
print(set2)

# Intersection (the elements both sets have)
set3=set1 & set2
print('\nIntersection set3:')
print(set3)
# Union (join both sets and remove duplicates)
set4=set1 | set2
print('\nUnion set4:')
print(set4)
# Difference
set5=set1 - set2
set6=set2 - set1
print('\nDifference set5:')
print(set5)
print('\nDifference set6:')
print( set6)


# To remove duplicates from a huge list, you could use hashing, but it's not very fast. A set does this nicely
list1 = [111,222,333,444,111,222,333,444,555,666]  
set7=set(list1)
print('\nRemove duplicates from a list, set7:')
print(set7)

```

Output:

```
{'h', 'l', 'e', 'o'}
{'h', 'n', 'o', 'y', 'p'}

Intersection set3:
{'h', 'o'}

Union set4:
{'h', 'p', 'n', 'e', 'o', 'y', 'l'}

Difference set5:
{'l', 'e'}

Difference set6:
{'p', 'y', 'n'}

Remove duplicates from a list, set7:
{555, 333, 111, 666, 444, 222}
```


## 5. A Few Extras about Modern sets ##

Hey everyone! Everything above works in all versions of Python. Here are three more things that are common in modern code, to make your coding smoother.

### (1) Set comprehensions ###

When we learn about lists, we use list comprehensions like `[x * x for x in range(5)]`. Sets have their own **set comprehensions**. They look almost the same – just swap the square brackets for curly braces:

```python
# The squares of all even numbers from 1 to 10
squares = {x * x for x in range(1, 11) if x % 2 == 0}
print(squares)
```

Output:

```
{64, 4, 36, 100, 16}
```

Notice the result is automatically unordered with no duplicates. You don't need to call `set()` yourself.

Here's a more real-world example. Say Brother Shui wants to get the **unique** customers from a pile of orders:

```python
orders = [
    {'user': 'One Drop', 'amount': 100},
    {'user': 'Two Drops', 'amount': 200},
    {'user': 'One Drop', 'amount': 50},
    {'user': 'Three Drops', 'amount': 300},
]

users = {order['user'] for order in orders}
print(users)
```

Output (the order may be different):

```
{'Two Drops', 'One Drop', 'Three Drops'}
```

Done in one line – much cleaner than making an empty set and using `add`.

### (2) frozenset: a set that can't change ###

A normal set can change: you can `add` and `remove`. But sometimes we want a set that **can't** be changed – for example, to use it as a dict key, or to put it inside another set.

That's when you use `frozenset`:

```python
fs = frozenset([1, 2, 3])
print(fs)

# You can do set operations with it
print(fs & frozenset([2, 3, 4]))

# You can use it as a dict key
config = {frozenset(['admin', 'editor']): 'Admin panel access'}
print(config[frozenset(['editor', 'admin'])])
```

Output:

```
frozenset({1, 2, 3})
frozenset({2, 3})
Admin panel access
```

Look at the last part: `frozenset(['admin', 'editor'])` and `frozenset(['editor', 'admin'])` are **equal** – because sets have no order – so both lookups find the same key.

### (3) When to use a set instead of a list ###

This last point isn't new syntax, but it's very important. When we check if something is **in** a group, like `x in collection`:

* If `collection` is a list, the time is O(n). The more elements, the slower it is.
* If `collection` is a set (or dict), the time is close to O(1). It hardly depends on how many elements there are.

So if your code checks "is this thing in that pile?" a lot, changing the pile from a list to a set can make it much, much faster:

```python
# We have 100,000 usernames and want to check if a name is there
names_list = [f'user_{i}' for i in range(100000)]
names_set = set(names_list)

# Both give the same answer, but the second one is much faster
print('user_99999' in names_list)
print('user_99999' in names_set)
```

Output:

```
True
True
```

So a set isn't only useful for removing duplicates – even more important, it's great for **fast lookups**. When your code does lots of `in` checks, think about switching to a set.
