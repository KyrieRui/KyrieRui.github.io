# 6. Variables in Python #

## 1. Creating and Assigning Variables ##

In a Python program, a **variable** has a name, and it can hold any type of data. A variable name can only use English letters (capital or small), digits and underscores (`_`), and it can't start with a digit. For example:

```python
a=88
```

Here, `a` is a variable that holds an integer. Notice that in Python you **don't** have to say what type of data a variable holds. In Python, `=` is the **assignment** statement, just like in other languages. Because you don't need to declare the type, you can give a variable any type of data. You can also change the same variable again and again, even to a different type.

```python
a = 'Hello Python'
print(a)
a = 123
print(a)
```

Output:

```
Hello Python
123
```

A language where a variable's type isn't fixed is called a **dynamic language**. The opposite is a **static language**. In a static language, you must give each variable a type when you create it, and if you assign the wrong type, you get an error. Java is a static language, for example.


## 2. What a Variable Points To ##

Look at this code. The variable `b` prints `Hello Python` at the end.

```python
a = 'Hello Python'
b = a
a = 123
print(b)
```

Output:

```
Hello Python
```

Here's why: at first, variable `a` points to the string `Hello Python`. Then `b = a` creates variable `b`, and `b` points to the **same** string that `a` points to, `Hello Python`. Finally, `a = 123` makes `a` point to `123` instead. So when we print `b`, we still get `Hello Python`.

You can think of it like this:

![Two names and two objects](../../images/diagrams/variable-alias.svg)

- ① Variable `a` points to the string `'Hello Python'`
- ② `b = a`: variable `b` also points to `'Hello Python'`
- ③ `a = 123`: variable `a` now points to the integer `123`, but `b` still points to `'Hello Python'`

 

## 3. Assigning Several Variables at Once ##

Python lets you assign values to several variables at the same time. For example:

```python
a = b = c = 1
```

In this example, one integer object with the value 1 is created, and all three variables point to the same place in memory.

You can also give several variables different values at once. For example:

```python
a, b, c = 1, 2, "liangdianshui"
```

Here, the integers 1 and 2 go to variables `a` and `b`, and the string `"liangdianshui"` goes to variable `c`.




## Guess the output first, then explain what the variables point to

We've covered assigning variables. Now, **don't run it yet**. Guess what the last two lines print:

```python
minutes = 15
recorded = minutes
minutes = minutes + 5
print(minutes)
print(recorded)
```

Output:

```text
20
15
```

`recorded = minutes` makes both names point to the same integer object at first. But it does **not** make them "change together forever". `minutes = minutes + 5` works out a new result and points `minutes` to it. `recorded` still points to the old integer.

Now change the starting value to `0` and work it out yourself. You should get `5` and `0`. If your guess was wrong, look back at "What a Variable Points To" and check, after each assignment, where each name is pointing.

One more thing that's easy to mix up: `'15'` is text, and `15` is an integer. When you need to do maths, convert it as needed. Just because they look the same on screen doesn't mean they work the same way. Try `int('15') + 5`, then try `'15' + '5'`, and explain why you get `20` and `'155'`.

When you're starting out, name your variables with English letters, digits and underscores. Python actually allows some non-ASCII characters in names too, as long as they follow the rules for identifiers – it's not limited to English letters. But while learning, keep using clear English names, and remember that **keywords** (like `if` or `for`) can't be used as normal variable names.
