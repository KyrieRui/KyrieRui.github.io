# 3. Python's Basic Data Types #

## 1. Strings ##

A **string** is one of the most common data types in Python. It is easy to spot: a string is text inside **quotes**.

You can use single quotes `' '`, double quotes `" "` or triple quotes `''' '''`. For example: `'abc'`, `"123"` and so on.

Please note: the quotes `''` or `""` are only a way to show where the string starts and ends. They are **not** part of the string. So the string `'abc'` has only 3 characters: a, b and c.

If you like to think things through, you might ask:

Why do we need single quotes `' '`, double quotes `" "` **and** triple quotes `''' '''`? Why not just pick one? Why have so many rules for the same thing?

Good question. Usually, one rule for one thing is best. So if strings have three ways to be written, there must be a reason.

Let's write the same string in all three ways, print them, and see what happens.

```python
str1 = 'Sam'
str2 = "Sam"
str3 = '''Sam'''
print(str1)
print(str2)
print(str3)
```

The results are the same:

```
Sam
Sam
Sam
```

But what if our string is not `Sam`, but `Sam's book` – with a quote mark **inside** it?

Then we get an error straight away:

<!-- skip-ci -->
```python
str1 = 'Sam's book'
print(str1)
```

```
  File "test.py", line 1
    str1 = 'Sam's book'
                  ^
SyntaxError: invalid syntax
```

Notice: single quotes `' '` don't work here, but double quotes `" "` do.

```python
str2 = "Sam's book"
print(str2)
```

The result is just what we wanted:

```
Sam's book
```

Triple quotes work the same way. If your text has double quotes inside it, double quotes around it will give the same error. That is when you can use triple quotes:

```python
str3 = '''Sam said: "Hello!"'''
print(str3)
```

```
Sam said: "Hello!"
```

So, can strings made with single or double quotes **never** hold text like this?

They can! You can use **escape characters**.

For a single quote, write `\'`. For a double quote, write `\"`.

Be careful: this is a **backslash** `\`, not a forward slash `/`.

Now let's test it:

```python
str1 = 'Sam\'s book'
str2 = "Sam said: \"Hello!\""
print(str1)
print(str2)
```

The output:

```
Sam's book
Sam said: "Hello!"
```

One last thing: triple quotes `''' '''` let a string go over **several lines**.

```python
str2 = '''Sam
loves
Python'''
print(str2)
```

Output:

```
Sam
loves
Python
```






## 2. Integers ##

An **integer** in code is the same as an integer in maths: positive whole numbers, negative whole numbers and zero. Integers are numbers **without a decimal point**.

Python can handle integers of any size, for example `1`, `100`, `-8080`, `0` and so on.

```python
int1 = 1
int2 = 100
int3 = -8080
int4 = 0

print(int1)
print(int2)
print(int3)
print(int4)
```

Output:

```
1
100
-8080
0
```

Be careful: if you put a number inside quotes, it becomes a **string**, not an integer. For example, `'100'` is a string, not an integer.

In real life we do maths with whole numbers. In code it's the same: you can add, subtract, multiply and divide integers.

For example:

```python
int1 = 1 + 2
int2 = 1 - 2
int3 = 1 * 2
int4 = 1 / 2

print(int1)
print(int2)
print(int3)
print(int4)
```

Output:

```
3
-1
2
0.5
```

Now look at the example above. Do you notice anything?

Look at what `int4` prints: `0.5`. That is a decimal number.

And how did we define an integer earlier?

A number **without** a decimal point.

So `int4` is definitely **not** an integer.

We can use the `type()` function to check the type:

```python
int1 = 1 + 2
int2 = 1 - 2
int3 = 1 * 2
int4 = 1 / 2

print(int1)
print(int2)
print(int3)
print(int4)

print(type(int1))
print(type(int2))
print(type(int3))
print(type(int4))
```

Result:

```
3
-1
2
0.5
<class 'int'>
<class 'int'>
<class 'int'>
<class 'float'>
```

We can see that `int4` is a **float**, while `int1`, `int2` and `int3` are all **int** (integer).

So what is a float?

A float is a **floating-point number**. We will talk about it next.

Before that, have a quick look at Python's arithmetic operators, just to get to know them.

**Python Arithmetic Operators**

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | Add | `2 + 1` gives `3` |
| `-` | Subtract | `1 - 2` gives `-1` |
| `*` | Multiply | `1 * 2` gives `2` |
| `/` | Divide | `1 / 2` gives `0.5` |
| `%` | Modulo – gives the remainder of a division | `5 % 2` gives `1` |
| `**` | Power – gives x to the power of y | `2 ** 3` is 2 to the power of 3 |
| `//` | Floor division – gives the whole-number part of the answer | `11 // 2` gives `5`, `11.0 // 2.0` gives `5.0` |





## 3. Floats ##

A **float** is a number with a decimal point.

Floats are like integers in many ways, but floats are the trickiest. They are the hardest to fully understand.

The famous programmer Herb Sutter once joked that there are three kinds of people: people who know they don't understand floating-point maths; people who *think* they understand it; and a very small number of experts who wonder if they could *ever* fully understand it.

Why would he say that?

Look at the example below. Just like with integers, we are only adding some floats:

```python
print(0.55+0.41)
print(0.55+0.4)
print(0.55+0.411)
```

But the results might surprise a beginner:

```
0.96
0.9500000000000001
0.9610000000000001
```

The first one is fine: `0.55 + 0.41` equals 0.96, exactly right. But in the other two, where did all those zeros come from?

This is because computers cannot store floats perfectly. Computers save numbers in **binary**, and binary cannot show some numbers exactly. It can only get very, very close.

So be careful when you do maths with floats or compare them.




## 4. Booleans ##

Booleans work just like in Boolean algebra. A Boolean has only two values: `True` or `False`. It is always one or the other. In Python you can write `True` and `False` directly (watch the capital letters!), or you can get them from a Boolean calculation.

You can use `and`, `or` and `not` with Booleans.

`and`: the result is True only if **all** parts are True.

`or`: the result is True if **at least one** part is True.

`not`: it works on just one value. It turns True into False, and False into True.



## 5. None (the empty value) ##

Almost every programming language has a special "empty" value. In Python, it is called `None`.



## 6. f-strings: putting variables inside strings ##

Hey everyone! What if you want to put the value of a variable inside some text? How do you do it?

The best way in Python is called an **f-string** (added in Python 3.6). Put an `f` before the opening quote, and wrap a variable name in `{}` inside the string. Python will replace the `{}` with the variable's value.

```python
name = 'Sam'
print(f'Nickname: {name}')
```

Output:

```
Nickname: Sam
```

It's that simple: `f` at the front + `{variable_name}`. Single or double quotes both work, and you can use many `{}` in one string. This is the recommended way to build strings today.

Now that you know the basics, here are a few more advanced tricks that many people don't know about.

### (1) Self-documenting: a great debugging tool `f"{x=}"` ###

When you write code, do you often want to `print` a variable's **name and value** to help find bugs?

The old way looks like this:

```python
name = 'Sam'
age = 18

print(f'name={name}, age={age}')
```

Output:

```
name=Sam, age=18
```

You have to type each variable name twice, and if you rename a variable, it's easy to forget one. Since Python 3.8, f-strings have an `=` syntax (called **self-documenting expressions**) that does it in one step:

```python
name = 'Sam'
age = 18

print(f'{name=}, {age=}')
```

Output:

```
name='Sam', age=18
```

See? The variable name and the equals sign are added for you, and the string even gets quotes around it. This is super handy for debugging. It has been around since Python 3.8, but lots of people still don't know about it – don't miss out!

You can even put a whole expression in it:

```python
a = 3
b = 4

print(f'{a + b = }')
```

Output:

```
a + b = 7
```

Notice that the spaces around `=` are kept exactly as you typed them. If you want neat output, just control the spaces yourself.

### (2) Format specs: alignment, decimal places, thousands separators ###

Inside the curly braces of an f-string, you can add a colon `:` followed by a **format spec**. It controls how the value looks.

Keep 2 decimal places:

```python
pi = 3.1415926

print(f'{pi:.2f}')
```

Output:

```
3.14
```

Right-align in a space 10 characters wide:

```python
name = 'Sam'

print(f'[{name:>10}]')
```

Output (the gap is spaces):

```
[       Sam]
```

`>` means right-align, `<` means left-align, and `^` means centre.

Add commas to big numbers:

```python
amount = 1234567890

print(f'Order total: ${amount:,}')
```

Output:

```
Order total: $1,234,567,890
```

Show as a percentage:

```python
rate = 0.875

print(f'Success rate: {rate:.1%}')
```

Output:

```
Success rate: 87.5%
```

See? Jobs that used to need `round`, `format` or joining strings together can all be done with one f-string.

### (3) Python 3.12+: quotes inside f-strings are no longer a problem ###

One last thing: a new feature in Python 3.12 (PEP 701). Before 3.12, f-strings had an annoying rule: if you wrote a string inside the curly braces, its quotes could **not** be the same as the outer quotes.

For example, the code below is **wrong** in Python 3.11 and earlier:

<!-- skip-ci -->
```python
data = {'name': 'Sam', 'age': 18}

# Only allowed in Python 3.12+: single quotes inside and outside
print(f'The nickname is {data['name']}')
```

Output:

```
The nickname is Sam
```

In older versions, this code gives a `SyntaxError`. You would have to switch the outer quotes to double quotes, or use an extra variable. From 3.12, this rule is gone: you can mix the outer and inner quotes however you like. This is really helpful when you write complex templates.

Python 3.12 also removed other limits: f-strings can now have expressions over several lines, comments, and backslashes. So when you use Python 3.12+, you can write f-strings pretty much any way you want – no more strange rules.




