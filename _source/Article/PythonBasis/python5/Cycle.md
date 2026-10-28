# 2. Loops #



## 1. What is a Loop? ##

Almost every programming language has loops. Why?

Ask yourself: why do we write programs?

To make our work easier and help us work more efficiently, of course!

Computers are different from humans. Computers don't get tired, don't complain, and don't need a rest. They can keep going forever.

And remember: what computers are **best** at is doing the same thing again and again.

That's why we need loops. A loop lets us run a statement, or a group of statements, many times.

Here's the general shape of a loop:

![The basic flow of a loop](../../images/diagrams/while-flow.svg)


Python has `for` loops and `while` loops.

Now here's another question: what if I want the loop to stop after 100 times? How do I do that?

We use some **loop control statements**:

|Loop control statement|What it does|
|------|------|
|break|Stops the loop while it's running, and jumps out of the whole loop|
|continue|Stops the current round of the loop, skips the rest of it, and goes to the next round|
|pass|`pass` is an empty statement. It's there to keep the program's structure complete|

These control statements let us tell the program **when to stop**, and **when to skip this round**.




## 2. The for Loop ##

Let's look at the `for` loop first.

Its flow chart looks like this:


![A for loop going through a sequence](../../images/diagrams/for-flow.svg)


The basic syntax:

<!-- skip-ci -->
```python
for iterating_var in sequence:
   statements(s)
```

Using this basic syntax, let's write a quick test:


```python
for letter in 'Hello Shui':
    print(letter)
```

Output:

```txt
H
e
l
l
o
 
S
h
u
i
```

From the output, we can see it prints the string `Hello Shui` one character at a time.

What if we use a dictionary instead of a string?

```python
dict = {'One Drop': 'Primary student', 'Two Drops': 'Middle school student', 'Three Drops': 'High school student'}

for i in dict:
    print(i)
```

Output:

```
One Drop
Two Drops
Three Drops
```

You'll see it only prints each **key** in the dictionary.

I often tell everyone: whenever you learn something new, try it out lots of ways.

A conclusion you find yourself by trying once is better than hearing someone else say it ten times.

Don't know what to try?

Use our examples to think of new ones. For the `for` loop above, we tried a string and a dictionary. What other basic data types have we learned?

If you don't remember, go back and look. Try all the basic types.

For example, if you try, you'll find that integers and floats **can't** be put directly into a `for` loop:

<!-- skip-ci -->
```python
a = 100

b = 0.01

for i in a:
    print(i)

for i in b:
    print(i)
```

Running it gives an error:

```
Traceback (most recent call last):
  File "/Users/twowater/dev/python/test/com/twowater/test.py", line 5, in <module>
    for i in a:
TypeError: 'int' object is not iterable
```






## 3. The range() Function ##

`for` loops are often used together with the `range()` function.

If you don't know `range()`, let's understand it with some code:

```python
for i in range(3):
    print(i)
```

Output:

```
0
1
2
```

So it prints 0 up to (but not including) 3.

`range(x)` makes a sequence of whole numbers from 0 to x-1.

`range(a,b)` makes a sequence of whole numbers that **includes a but not b**.

In fact, `range(3)` in the example can be written as `range(0,3)` – the result is the same.

Most of the time, we use `range()` to run some code **n times**.

Here's a question: look closely at `range()`. Whether it has 1 argument or 2, what do they have in common?

Did you notice? They always go up by **1** each time.

`range(3)` is 0, 1, 2 – going up by 1 each time.

`range(3,6)` is 3, 4, 5 – also going up by 1 each time.

Can we go up by something other than 1?

What if I want to go up by 2?

When you write programs, you'll definitely need this. And of course Python's `range` can do it.

So `range` can also take **three** arguments.

For example, `range(0,10,2)` means: count from 0 to 10 (not including 10), going up by 2 each time.

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```
0
2
4
6
8
```


 
 
 

## 4. The while Loop ##

A `while` loop does the same job as a `for` loop.

Let's see what a `while` loop looks like:

```python
count = 1
sum1 = 0

while count <= 100:    # The condition
    sum1 = sum1 + count    # The body of the while loop
    count = count + 1

print(sum1)
```

Output:

```txt
5050
```

This example adds up all the whole numbers from 1 to 100.



## 5. The Difference Between for and while Loops ##

As we said before, if one piece of syntax can do a job, there's no need for two.

Since both are loops, `for` and `while` must be different in some way.

So when should you use a `for` loop, and when a `while` loop?

* A `for` loop is mainly for going through an **iterable** (something you can loop over).

* A `while` loop is mainly for repeating something **as long as a condition is true**.
(For example, an endless loop that exits with `break`.)

* In some cases, `for` and `while` can be swapped.

For example:

```python
for i in range(0, 10):
    print(i)


i = 0
while i < 10:
    print(i)
    i = i + 1
```

The output is the same, but if you think carefully, you'll see they run in a different way and need different information.



## 6. Nested Loops ##

Like conditional statements, loops can be **nested**.

Here's the syntax:

**Nested for loop syntax**

<!-- skip-ci -->
```python
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```

**Nested while loop syntax**

<!-- skip-ci -->
```python
while expression:
   while expression:
      statement(s)
   statement(s)
```

You can also put a different kind of loop inside: a `for` loop inside a `while` loop, or a `while` loop inside a `for` loop.

For example:

If we want to stop adding once `sum` is over 1000, we can use `break` to exit the whole loop.

```python
count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if ( sum > 1000):  # Exit the loop when sum is over 1000
        break
    count = count + 1
print(sum)
```

Output:

```txt
1035
```

Sometimes we only want to add up the **odd** numbers between 1 and 100. That means when `count` is even, we want to skip this round and not add it. We can use `continue` for this:

```python
count = 1
sum = 0
while (count <= 100):
    if ( count % 2 == 0):  # Skip even numbers
        count = count + 1
        continue
    sum = sum + count
    count = count + 1
print(sum)
```

Output:

```txt
2500
```

And another one:

```python
for num in range(10,20):  # Go through the numbers from 10 to 20
   for i in range(2,num): # Go through possible factors
      if num%i == 0:      # Found the first factor
         j=num/i          # Work out the second factor
         print (f'{num} is a composite number')
         break            # Jump out of the current loop
   else:                  # The else part of the loop
      print (f'{num} is a prime number')
```

Output:

```txt
10 is a composite number
11 is a prime number
12 is a composite number
13 is a prime number
14 is a composite number
15 is a composite number
16 is a composite number
17 is a prime number
18 is a composite number
19 is a prime number
```


This example also uses a `for … else` statement.

The statements in the `for` loop work as normal. The statements in `else` run only if the loop **finishes normally** – that is, if the `for` loop was **not** stopped by `break`.

And just like `for … else`, there is also `while … else`. They mean the same thing.


