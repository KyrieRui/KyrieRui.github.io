# 1. Conditional Statements #


## 1. What is a Conditional Statement? ##


Conditional statements in Python work basically the same as in other languages. The result of one or more checks (**True** or **False**) decides which block of code runs.

In Python, any value that is not 0 and not empty counts as **True**. 0 or empty (null) counts as **False**.

Here is the flow chart:

![if condition check](../../images/diagrams/if-flow.svg)


## 2. The Basic Form of an if Statement ##

In Python, the basic form of an `if` statement looks like this:

<!-- skip-ci -->
```python
if condition:
    do something……
else:
    do something else……
```

As we said in earlier chapters, Python is very strict about **indentation**, so be careful with it here. And don't forget the colon `:`.

In the condition of an `if` statement, you can use `>` (greater than), `<` (less than), `==` (equal to), `>=` (greater than or equal to) and `<=` (less than or equal to) to compare things.

For example:

```python
# -*-coding:utf-8-*-

results=59

if results>=60:
    print ('Pass')
else :
    print ('Fail')

```

Output:

```txt
Fail
```

As we said above, non-zero numbers, non-empty strings, non-empty lists and so on count as True. Everything else is False. So you can also write:

```python
num = 6
if num :
    print('Hello Python')
```

Output:

```
Hello Python
```

So the message was printed.

What if we change `num` to an empty string?

```python
num = ''
if num :
    print('Hello Python')
```

Nothing is printed (the program ends normally, without printing `Hello Python`).

Clearly, an empty string is False. It doesn't meet the condition, so `print('Hello Python')` never runs.

One more reminder: after the colon `:` in a condition, the next line **must** be indented. If it's not indented, you get an error.

<!-- skip-ci -->
```python
num = ''
if num :
print('Hello Python')
```

Running it gives an error:

```
  File "/Users/twowater/dev/python/test/com/twowater/test.py", line 4
    print('Hello Python')
        ^
IndentationError: expected an indented block
```

The colon and indentation are part of the syntax. They help Python see which code belongs where, and understand the logic and order of what runs.



## 3. if with Several Conditions in Turn ##

Sometimes we need more than two choices. In the example above, 60 or more is a pass. What if we also want 90+ to be "Excellent", and 80 – 90 to be "Good"?

Then we use an `if` statement with several conditions.

In pseudocode (plain-language code):

<!-- skip-ci -->
```python
if condition1:
    do thing 1……
elif condition2:
    do thing 2……
elif condition3:
    do thing 3……
else:
    do thing 4……
```

Example:

```python
# -*-coding:utf-8-*-

results = 89

if results > 90:
    print('Excellent')
elif results > 80:
    print('Good')
elif results > 60:
    print ('Pass')
else :
    print ('Fail')

```

Output:

```txt
Good
```



## 4. if Checking Several Conditions at Once ##

What do we do when there are several conditions at the same time?

For example, a student is "Excellent" only if **both** their Java and Python test scores are over 80. How do we do that?

We can use `or` and `and`.

`or` means the check succeeds if **at least one** of the two conditions is true.
 
`and` means the check succeeds only if **both** conditions are true.

For example:

```python
# -*-coding:utf-8-*-

java = 86
python = 68

if java > 80 and  python > 80:
    print('Excellent')
else :
    print('Not excellent')

if ( java >= 80  and java < 90 )  or ( python >= 80 and python < 90):
    print('Good')

```

Output:

```txt
Not excellent
Good
```

Note: when an `if` has several conditions, you can use brackets to show which to check first. Checks inside brackets happen first. Also, `and` and `or` have **lower priority** than `>`, `<` and other comparison symbols. So without brackets, greater-than and less-than are checked before and/or.

## 5. Nested if ##

What is a nested `if`?

It's just what it sounds like: an `if` statement inside another `if` statement.

The example above can also be written with a nested `if`:

```python
java = 86
python = 68

if java > 80:
    if python > 80:
        print('Excellent')
    else:
        print('Not excellent')
else:
    print('Not excellent')
```

Output:

```
Not excellent
```

Of course, this is just to show that `if` statements can be nested. For this task, I don't really recommend nesting like this. It makes the code longer, and too much nesting makes code hard to read.



## 6. New in Python 3.10+: match / case ##

Hey everyone! If you're using Python 3.10 or newer, there's another, clearer tool besides `if / elif / else`: `match / case`. It's called **structural pattern matching**.

Why talk about it specially?

Let's look at a task first. Say Brother Shui wants to do different things depending on a **command string** from the server:

```python
command = 'start'

if command == 'start':
    print('Starting')
elif command == 'stop':
    print('Stopping')
elif command == 'pause':
    print('Pausing')
else:
    print('Unknown command')
```

Output:

```
Starting
```

Nothing wrong with this. But when there are lots of choices, a long chain of `elif` gets wordy. Let's rewrite it with `match / case`:

```python
command = 'start'

match command:
    case 'start':
        print('Starting')
    case 'stop':
        print('Stopping')
    case 'pause':
        print('Pausing')
    case _:
        print('Unknown command')
```

Output:

```
Starting
```

`case _` is the "catch-all" branch, like `else`. The underscore `_` is a **wildcard**. It matches anything that none of the earlier cases matched.

If you like to think, you might ask: isn't this just `switch / case` from other languages, with different syntax?

Not quite! The real power of `match / case` is that it can match **structure**, not just **values**.

Here's an example matching a sequence. Say the product team sends us a coordinate:

```python
point = [10, 20]

match point:
    case [0, 0]:
        print('Origin')
    case [x, 0]:
        print(f'On the x-axis, x = {x}')
    case [0, y]:
        print(f'On the y-axis, y = {y}')
    case [x, y]:
        print(f'Normal point, x = {x}, y = {y}')
    case _:
        print('Not a 2D coordinate')
```

Output:

```
Normal point, x = 10, y = 20
```

See? It didn't just match "this is a list of length 2" – it also **unpacked** `x` and `y` for you, ready to use in that branch.

In a sequence, you can also use `*rest` to collect the remaining elements:

```python
nums = [1, 2, 3, 4, 5]

match nums:
    case [first, *rest]:
        print(f'First: {first}, the rest: {rest}')
```

Output:

```
First: 1, the rest: [2, 3, 4, 5]
```

What about dictionaries?

`match / case` can also match the **shape** of a dictionary:

```python
response = {'status': 'ok', 'data': [1, 2, 3]}

match response:
    case {'status': 'ok', 'data': data}:
        print(f'Success, got data {data}')
    case {'status': 'error', 'message': msg}:
        print(f'Failed: {msg}')
    case _:
        print('Unknown response')
```

Output:

```
Success, got data [1, 2, 3]
```

Even cooler, `match / case` works with **classes** too. It's even better with `dataclass`:

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p = Point(0, 5)

match p:
    case Point(x=0, y=0):
        print('Origin')
    case Point(x=0, y=y):
        print(f'On the y-axis, y = {y}')
    case Point(x=x, y=0):
        print(f'On the x-axis, x = {x}')
    case Point(x=x, y=y):
        print(f'Normal point ({x}, {y})')
```

Output:

```
On the y-axis, y = 5
```

Finally, one small feature called a **guard**: you add an `if` after the `case`:

```python
score = 75

match score:
    case x if x >= 90:
        print('Excellent')
    case x if x >= 80:
        print('Good')
    case x if x >= 60:
        print('Pass')
    case _:
        print('Fail')
```

Output:

```
Pass
```

See how `match / case` makes code more structured and easier to read?

One more note: `match / case` is **not** meant to replace `if / elif`. For simple value comparisons and true/false checks, a plain `if` is actually clearer. `match / case` really shines when you choose what to do based on the **structure of data** – for example, reading JSON, working with syntax trees, or writing an interpreter.


