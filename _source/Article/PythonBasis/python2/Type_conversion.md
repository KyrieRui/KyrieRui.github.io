# 5. Converting Between Basic Data Types #

Here are the ways to convert between basic data types in Python.

|Function|What it does|
|-----|------|
|int(x [,base ])  |       Turns x into an integer  |
|float(x )    |           Turns x into a float  |
|complex(real [,imag ])|  Makes a complex number  |
|str(x ) |                Turns object x into a string  |
|repr(x ) |               Turns object x into an expression string  |
|eval(str )  |            Works out a valid Python expression inside a string and returns an object  |
|tuple(s )  |             Turns sequence s into a tuple  |
|list(s )   |             Turns sequence s into a list  |
|chr(x )   |              Turns an integer into a character  |
|ord(x )     |            Turns a character into its integer value  |
|hex(x )     |            Turns an integer into a hexadecimal string  |
|oct(x )     |            Turns an integer into an octal string  |

Note: Python 3 has only one integer type, `int`, which can hold very big numbers. There is no `Long` type like in Python 2.

Let's try some of these functions.

For example, the `int()` function turns a string that **looks like a whole number** into an integer.

```python
str1 = '100'
str2 = '300'

print(str1 + str2)
print(int(str1) + int(str2))
```

Output:

```
100300
400
```

Notice we said "a string that looks like a whole number". Strings made of words can't be turned into integers by `int()`.

Strings with a decimal point also can't be turned into integers by `int()`.

<!-- skip-ci -->
```python
print(int('88.88'))
```

This gives an error:

```
Traceback (most recent call last):
  File "test.py", line 2, in <module>
    print(int('88.88'))
ValueError: invalid literal for int() with base 10: '88.88'
```

But this doesn't mean floats can't become integers. It only means a **string** with a decimal point can't be forced into an integer by `int()`.

A **float** can still be converted with `int()`.

For example:

```python
print(int(88.88))
```

Output:

```
88
```

But notice the result is 88. The 0.88 after the decimal point is gone.

This is because `int()` turns data into an integer. When it turns a float into an integer, it just cuts off the decimal part and keeps the whole number part. So the output is 88.

I won't go through every function one by one. Just use them and try them, and you will slowly get to know them. If you are a beginner, play with every one of them! Write anything you like, run it, and look at the result. Don't worry – your computer won't break from this.










