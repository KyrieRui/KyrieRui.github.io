# 2. The print() Function #

Let's start with the `print()` function. If you are new, you may not know much about functions yet. That's fine. For now, you only need to know its parts and what it does. We will explain functions in detail later.

The `print()` function has two parts:

1. The command: `print`
2. What the command works on: the stuff inside the brackets after `print`

It looks like this:

![The parts of print()](../../images/diagrams/print-call.svg)

The job of `print()` is to make the computer show a result on the screen (in the terminal). What it shows is whatever you put inside `print()`.

For example, in the last chapter, our first Python program was `print('Hello Python')`

```python
print('Hello Python')
```

Output:

```
Hello Python
```

Here is what happens step by step:

1. You give the interpreter a command: print 'Hello Python'
2. The interpreter turns your code into machine language the computer can understand
3. The computer runs it and prints the result

Here is a picture of the process:

![From the call to the output](../../images/diagrams/print-execution.svg)

Some of you may ask: why do we need the single quotes? Can't we just write `print(Hello Python)`?

When you have a question like this while coding, the best thing to do is write the code and test it yourself.

<!-- skip-ci -->
```python
print(Hello Python)
```

Result:

```
  File "test.py", line 1
    print(Hello Python)
                    ^
SyntaxError: invalid syntax
```

Clearly, without the quotes, the result turns red (an error). So this doesn't work.

This is because it breaks Python's syntax rules. Without the quotes, the Python interpreter can't understand what you wrote.

So it shows the error `SyntaxError: invalid syntax`, which means: **syntax error**. Your statement doesn't follow the rules.
















