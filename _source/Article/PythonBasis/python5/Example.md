# 3. Examples Using Conditions and Loops Together #

## 1. Print the Times Tables ##

```python
# -*- coding: UTF-8 -*-

# Print the 1–9 times tables
for i in range(1, 10):
        for j in range(1, i+1):
            # f-string: put f before the string, and any expression inside {} is worked out and put into the string
            print(f'{i}x{j}={i*j}\t', end='')
        print()
```

Output:

```txt
1x1=1   
2x1=2   2x2=4   
3x1=3   3x2=6   3x3=9   
4x1=4   4x2=8   4x3=12  4x4=16  
5x1=5   5x2=10  5x3=15  5x4=20  5x5=25  
6x1=6   6x2=12  6x3=18  6x4=24  6x5=30  6x6=36  
7x1=7   7x2=14  7x3=21  7x4=28  7x5=35  7x6=42  7x7=49  
8x1=8   8x2=16  8x3=24  8x4=32  8x5=40  8x6=48  8x7=56  8x8=64  
9x1=9   9x2=18  9x3=27  9x4=36  9x5=45  9x6=54  9x7=63  9x8=72  9x9=81 
```


## 2. Check for a Leap Year ##

<!-- skip-ci -->
```python

# Check whether a year is a leap year

year = int(input("Enter a year: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print(f'{year} is a leap year')
else:
     print(f'{year} is not a leap year')

```





## First, write down how you'd count by hand

We're going to add up study time. The records might include `0`, and might include negative numbers typed by mistake. Let's agree on a rule first: zero minutes is allowed and kept, but negative numbers are skipped for now. How would you do this by hand? Start from zero, look at each record one by one, and only add the ones that follow the rule.

```python
records = [15, 0, 10, -3]
total = 0
valid_count = 0
for minutes in records:
    if minutes < 0:
        continue
    total = total + minutes
    valid_count = valid_count + 1
print(total)
print(valid_count)
```

Output:

```text
25
3
```

Don't just look at the total. Follow the loop step by step and write down `minutes`, `total` and `valid_count` each time. Zero minutes doesn't add to the total, but it's still a valid record, so the count of valid records is `3`.

Try two edge cases yourself: an empty list should give `0` and `0`. A list of only negative numbers should too. If you change the check to `minutes <= 0`, the total might stay the same, but the count changes. This shows that **one** correct number in the output doesn't mean the whole program does what it should.

Skipping negative numbers is just the rule for this exercise. Not every program should quietly skip mistakes. When we learn about exception handling, we'll change it to tell the caller what was wrong.
