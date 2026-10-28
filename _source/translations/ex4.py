EX = {}
EX['python14/02-match-phone'] = dict(
title="Check a phone number with re.match",
prompt="Write a function `is_phone(s)` that checks whether the string `s` is a valid mobile phone number in mainland China's format.\n\nRules:\n- 11 digits in total\n- The 1st digit must be `1`\n- The 2nd digit is `3` to `9`\n- The other 9 are all digits\n\nUse `re.match`. Return `True` if it matches, otherwise `False`.\n\nThen call:\n\n```python\nprint(is_phone('13812345678'))\nprint(is_phone('12345'))\nprint(is_phone('1381234567a'))\n```\n\nThe output should be:\n```\nTrue\nFalse\nFalse\n```\n\nTip: use the regex `^1[3-9]\\d{9}$`. Taking it apart: `^` pins the start of the string and `$` pins the end (without them, half a string could match too); `[3-9]` means any one digit from 3 to 9; `\\d{9}` means 9 digits in a row.",
starter="import re\n\n# Define is_phone(s): use re.match with the regex above, returning True or False\n# Then call is_phone with each of the three numbers above and print the results\n\n",
solution="import re\n\ndef is_phone(s):\n    return bool(re.match(r'^1[3-9]\\d{9}$', s))\n\nprint(is_phone('13812345678'))\nprint(is_phone('12345'))\nprint(is_phone('1381234567a'))",
hints=["re.match returns a Match object or None; bool(...) turns it into True/False", "In the regex, `^` and `$` pin the start and the end, so half a string can't pass", "Full code:\nimport re\ndef is_phone(s):\n    return bool(re.match(r'^1[3-9]\\d{9}$', s))\nprint(is_phone('13812345678'))\nprint(is_phone('12345'))\nprint(is_phone('1381234567a'))"])

EX['python14/03-groups-email'] = dict(
title="Pull out an email's username and domain with groups",
prompt="We have the string `email = 'alice@example.com'`.\n\nUse `re.match` + groups `(...)` to pull out the **username** and the **domain**, and `print` them one after the other.\n\nRequirements:\n- Group 1 matches the username (the part before `@`)\n- Group 2 matches the domain (the part after `@`)\n- Use `m.group(1)` for the username and `m.group(2)` for the domain\n\nThe output should be:\n```\nalice\nexample.com\n```\n\nTip: you can use the regex `(\\w+)@(\\w+\\.\\w+)`.",
starter="import re\n\nemail = 'alice@example.com'\n# m = re.match(...)\n# print(m.group(1))\n# print(m.group(2))\n",
solution="import re\n\nemail = 'alice@example.com'\nm = re.match(r'(\\w+)@(\\w+\\.\\w+)', email)\nprint(m.group(1))\nprint(m.group(2))",
hints=["A group is just the part you want to pull out, wrapped in ()", "`\\.` matches an actual dot; `.` without the backslash means any character", "Full code:\nimport re\nemail = 'alice@example.com'\nm = re.match(r'(\\w+)@(\\w+\\.\\w+)', email)\nprint(m.group(1))\nprint(m.group(2))"])

EX['python14/04-sub-spaces'] = dict(
title="Squash several spaces into one with re.sub",
prompt="Here's some text messed up with extra spaces:\n\n```python\ns = 'hello   world  python  is   cool'\n```\n\nUse `re.sub` to replace **each run of one or more spaces** with **one space**, assign the result to the variable `cleaned`, then `print(cleaned)`.\n\nThe output should be:\n```\nhello world python is cool\n```\n\nTip: `\\s+` matches 'one or more whitespace characters'.",
starter="import re\n\ns = 'hello   world  python  is   cool'\n# cleaned = re.sub(...)\n# print(cleaned)\n",
solution="import re\n\ns = 'hello   world  python  is   cool'\ncleaned = re.sub(r'\\s+', ' ', s)\nprint(cleaned)",
hints=["re.sub(pattern, repl, string): the second argument is what to replace with", "Use `\\s+` to match 'one or more spaces' – the + means once or more", "Full code:\nimport re\ns = 'hello   world  python  is   cool'\ncleaned = re.sub(r'\\s+', ' ', s)\nprint(cleaned)"])

EX['python15/02-make-adder'] = dict(
title="An adder factory",
prompt="Define a function `make_adder(n)`:\n\n- It takes a number `n`\n- It returns an inner function `adder(x)`, which returns `x + n`\n\nThen:\n\n1. Use `make_adder(10)` to make `add10`\n2. `print(add10(5))` – should print `15`\n3. Use `make_adder(100)` to make `add100`\n4. `print(add100(5))` – should print `105`\n\nThe output should be:\n```\n15\n105\n```",
starter="# Define make_adder(n), returning an inner function adder(x) that returns the sum of x and n\n# Use make_adder to make add10 and add100\n# Call each one once (with 5) and print the result\n\n",
solution="def make_adder(n):\n    def adder(x):\n        return x + n\n    return adder\n\nadd10 = make_adder(10)\nprint(add10(5))\nadd100 = make_adder(100)\nprint(add100(5))",
hints=["The inner function only reads n and doesn't change it, so nonlocal isn't needed", "make_adder(10) and make_adder(100) are two different closures, each carrying its own n", "Full code:\ndef make_adder(n):\n    def adder(x):\n        return x + n\n    return adder\n\nadd10 = make_adder(10)\nprint(add10(5))\nadd100 = make_adder(100)\nprint(add100(5))"])

EX['python15/01-make-counter'] = dict(
title="A counter made with a closure",
prompt="Define a function `make_counter()`:\n\n- Inside, it keeps `count = 0`\n- It returns an inner function `counter()`; each time `counter()` is called, it adds 1 to `count` and returns the new value (remember to use `nonlocal`)\n\nThen:\n\n1. `c = make_counter()`\n2. Call `c()` 3 times in a row, `print`ing the return value each time\n\nThe output should be:\n```\n1\n2\n3\n```",
starter="# Define make_counter(): count = 0 inside, return the inner function counter\n# Each call to counter adds 1 to count and returns the new value (remember nonlocal)\n# Then use make_counter() to make c, call it 3 times and print each return value\n\n",
solution="def make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count = count + 1\n        return count\n    return counter\n\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())",
hints=["The outer function sets count = 0; the inner function needs nonlocal count to change it", "The outer function returns the inner function object (note: return counter, not return counter())", "Full code:\ndef make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count = count + 1\n        return count\n    return counter\n\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())"])

EX['python15/03-study-time'] = dict(
title="Add up study time with a closure",
prompt="Back to the task from the start of this chapter – adding up study time with a closure.\n\nDefine a function `study_time(time)`:\n\n- It takes a starting `time`\n- It returns an inner function `insert_time(min)`; each call adds `min` to `time` and returns the current total (remember to use `nonlocal`)\n\nThen:\n\n1. `f = study_time(0)`\n2. `print(f(2))` – studied for 2 minutes\n3. `print(f(10))` – studied another 10 minutes\n4. `print(f(5))` – studied another 5 minutes\n\nThe output should be:\n```\n2\n12\n17\n```",
starter="# Define study_time(time), returning an inner function insert_time(min)\n# Each call to insert_time adds min to time and returns the current total (remember nonlocal)\n# Use study_time(0) to make f, call it three times in the order above and print each result\n\n",
solution="def study_time(time):\n    def insert_time(min):\n        nonlocal time\n        time = time + min\n        return time\n    return insert_time\n\nf = study_time(0)\nprint(f(2))\nprint(f(10))\nprint(f(5))",
hints=["The outer study_time takes time as a parameter; the inner insert_time changes it with nonlocal time (the parameter name min comes from the original tutorial – it temporarily hides the built-in min() function; in real projects, a name like minutes that doesn't clash is better)", "The outer function returns the inner function object insert_time (no brackets)", "Full code:\ndef study_time(time):\n    def insert_time(min):\n        nonlocal time\n        time = time + min\n        return time\n    return insert_time\n\nf = study_time(0)\nprint(f(2))\nprint(f(10))\nprint(f(5))"])

EX['python16/01-log'] = dict(
title="Write a @log decorator",
prompt="Write a decorator `log`:\n\n- It takes a function as its argument\n- Before calling the original function, it does `print('Starting')`\n- After calling the original function, it does `print('Finished')`\n\nThen decorate a function `hello()` with `@log` (inside it: `print('hello world')`), and call `hello()`.\n\nThe output should be:\n```\nStarting\nhello world\nFinished\n```",
starter="# Define the decorator log: take func, print a line before and after calling it inside wrapper, then return wrapper\n# Decorate hello() (which prints hello world) with @log, then call hello()\n\n",
solution="def log(func):\n    def wrapper():\n        print('Starting')\n        func()\n        print('Finished')\n    return wrapper\n\n@log\ndef hello():\n    print('hello world')\n\nhello()",
hints=["The three parts of a decorator: take func, define wrapper, return wrapper (note: wrapper, not wrapper())", "Inside wrapper: print('Starting') first → call func() → then print('Finished')", "Full code:\ndef log(func):\n    def wrapper():\n        print('Starting')\n        func()\n        print('Finished')\n    return wrapper\n\n@log\ndef hello():\n    print('hello world')\n\nhello()"])

EX['python16/02-uppercase'] = dict(
title="@uppercase: changing the return value",
prompt="Write a decorator `uppercase`:\n\n- It takes a function `func`\n- It calls the original function to get its result, `result`\n- It returns `result.upper()` (in capitals) from the wrapper\n\nThen decorate a function `greet(name)` with `@uppercase`; inside it: `return 'hello ' + name`.\n\nFinally:\n```python\nprint(greet('alice'))\nprint(greet('bob'))\n```\n\nThe output should be:\n```\nHELLO ALICE\nHELLO BOB\n```",
starter="# Define the decorator uppercase: in wrapper, catch the original function's return value, make it capitals and return it\n# Decorate greet(name) with @uppercase, then print the two calls as shown above\n\n",
solution="def uppercase(func):\n    def wrapper(*args, **kwargs):\n        result = func(*args, **kwargs)\n        return result.upper()\n    return wrapper\n\n@uppercase\ndef greet(name):\n    return 'hello ' + name\n\nprint(greet('alice'))\nprint(greet('bob'))",
hints=["Inside wrapper, catch the original function's return value: result = func(*args, **kwargs)", "Then return result.upper() – so print(greet(...)) gets the capital-letter result", "Full code:\ndef uppercase(func):\n    def wrapper(*args, **kwargs):\n        result = func(*args, **kwargs)\n        return result.upper()\n    return wrapper\n\n@uppercase\ndef greet(name):\n    return 'hello ' + name\n\nprint(greet('alice'))\nprint(greet('bob'))"])

EX['python16/03-count-calls'] = dict(
title="@count_calls: counting calls",
prompt="Write a decorator `count_calls`:\n\n- Keep a counter `count = 0` in the closure\n- Each time the decorated function is called, add 1 to `count`, then `print(f'Call number {count}')`, then call the original function\n- Add `@functools.wraps(func)` to `wrapper` – the good habit from the last section, don't forget it\n\nThen decorate a function `say_hi()` with `@count_calls` (inside it: `print('hi')`), and call `say_hi()` 3 times in a row.\n\nThe output should be:\n```\nCall number 1\nhi\nCall number 2\nhi\nCall number 3\nhi\n```",
starter="# Define the decorator count_calls: keep count in the closure; in wrapper, change it with nonlocal and print the message\n# Don't forget to import functools and add @functools.wraps(func) to wrapper\n# Decorate say_hi() with @count_calls and call it 3 times\n\n",
solution="import functools\n\ndef count_calls(func):\n    count = 0\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        nonlocal count\n        count = count + 1\n        print(f'Call number {count}')\n        return func(*args, **kwargs)\n    return wrapper\n\n@count_calls\ndef say_hi():\n    print('hi')\n\nsay_hi()\nsay_hi()\nsay_hi()",
hints=["Set count = 0 in the outer part of the decorator; wrapper needs nonlocal count to change it (this is closures + decorators together)", "Each time wrapper runs: add 1 to count → print the message → then func(*args, **kwargs); don't forget to import functools and add @functools.wraps(func) to wrapper", "Full code:\nimport functools\n\ndef count_calls(func):\n    count = 0\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        nonlocal count\n        count = count + 1\n        print(f'Call number {count}')\n        return func(*args, **kwargs)\n    return wrapper\n\n@count_calls\ndef say_hi():\n    print('hi')\n\nsay_hi()\nsay_hi()\nsay_hi()"])

EX['python17/01-early-return'] = dict(
title="Rewrite nested ifs with early returns",
prompt="The old version of the function `check(score)` used three levels of nesting. Rewrite `check(score)` using **early returns**, keeping the same logic:\n\n- `score < 0` or `score > 100`: return `'Invalid score'`\n- `score >= 90`: return `'Excellent'`\n- `score >= 60`: return `'Pass'`\n- anything else: return `'Fail'`\n\nThen call `print(check(95))`, `print(check(72))`, `print(check(40))` and `print(check(150))` in turn.\n\nThe output should be:\n```\nExcellent\nPass\nFail\nInvalid score\n```\n\nTip: an 'early return' means you return the unusual cases first, leaving the main path at the outer level – no else, no nesting.",
starter="# The old nested version looked like this (three levels of nesting, structure only – don't hand this in):\n# def check(score):\n#     if 0 <= score <= 100:\n#         if score >= 90:\n#             ... (left out: two more levels of if/else nested here)\n#     else:\n#         return 'Invalid score'\n\n# Rewrite check with early returns here: return the invalid-score case first, then check each level from high to low\n# Finally print the four calls asked for above\n\n",
solution="def check(score):\n    if score < 0 or score > 100:\n        return 'Invalid score'\n    if score >= 90:\n        return 'Excellent'\n    if score >= 60:\n        return 'Pass'\n    return 'Fail'\n\nprint(check(95))\nprint(check(72))\nprint(check(40))\nprint(check(150))",
hints=["First return the 'Invalid score' case – after that, every score left is valid", "Then if score >= 90: return 'Excellent', if score >= 60: return 'Pass', and finally return 'Fail'", "Full code:\ndef check(score):\n    if score < 0 or score > 100:\n        return 'Invalid score'\n    if score >= 90:\n        return 'Excellent'\n    if score >= 60:\n        return 'Pass'\n    return 'Fail'\n\nprint(check(95))\nprint(check(72))\nprint(check(40))\nprint(check(150))"])

EX['python17/02-list-comp'] = dict(
title="List comprehension: pick the positive numbers and square them",
prompt="Here's a list for you: `nums = [-2, 1, -3, 4, 0, -5, 6]`.\n\nUse a **list comprehension** to make a new list `result` containing 'the square of every positive number' in `nums` (note: `0` isn't positive).\n\nThen `print(result)`.\n\nThe output should be:\n```\n[1, 16, 36]\n```",
starter="nums = [-2, 1, -3, 4, 0, -5, 6]\n\n# Make result with one line of list comprehension\n# result = [...]\n\n# print(result)\n",
solution="nums = [-2, 1, -3, 4, 0, -5, 6]\nresult = [x * x for x in nums if x > 0]\nprint(result)",
hints=["The shape is: [expression for variable in sequence if condition]", "The expression is x * x, and the filter is x > 0", "Full code:\nnums = [-2, 1, -3, 4, 0, -5, 6]\nresult = [x * x for x in nums if x > 0]\nprint(result)"])

EX['python17/03-dict-comp'] = dict(
title="Dict comprehension: double every price",
prompt="Here's a price list for you: `prices = {'apple': 5, 'banana': 3, 'cherry': 10}`.\n\nUse a **dict comprehension** to make a new dictionary `doubled` – same keys, but every value doubled.\n\nThen `print(doubled)`.\n\nThe output should be:\n```\n{'apple': 10, 'banana': 6, 'cherry': 20}\n```",
starter="prices = {'apple': 5, 'banana': 3, 'cherry': 10}\n\n# Make doubled with a dict comprehension\n# doubled = {...}\n\n# print(doubled)\n",
solution="prices = {'apple': 5, 'banana': 3, 'cherry': 10}\ndoubled = {k: v * 2 for k, v in prices.items()}\nprint(doubled)",
hints=["The shape is: {key: value for variable in iterable}", "Use prices.items() to get the key k and the value v together", "Full code:\nprices = {'apple': 5, 'banana': 3, 'cherry': 10}\ndoubled = {k: v * 2 for k, v in prices.items()}\nprint(doubled)"])

EX['python17/04-type-hints'] = dict(
title="Write a function with type hints",
prompt="Define a function `greet` **with full type hints**:\n\n- Parameter `name`, of type `str`\n- Return type `str`\n- Body: return `f'Hello, {name}'`\n\nThen call `print(greet('World'))`.\n\nThe output should be:\n```\nHello, World\n```\n\nNote: a colon after the parameter, an arrow for the return type.\n\n(The checker only looks at the output – it can't tell whether you wrote the hints. But the hints are the point of this exercise, so please add them.)",
starter="# Define greet with type hints here\n# def greet(name: ...) -> ...:\n#     return ...\n\n# print(greet('World'))\n",
solution="def greet(name: str) -> str:\n    return f'Hello, {name}'\n\nprint(greet('World'))",
hints=["The parameter hint goes after the parameter: name: str", "The return hint goes after ): -> str", "Full code:\ndef greet(name: str) -> str:\n    return f'Hello, {name}'\n\nprint(greet('World'))"])

EX['python18/01-name-suffix-stem'] = dict(
title="Get a path's name / suffix / stem",
prompt="Please:\n\n1. Import `Path` from `pathlib`\n2. Create a path object `p = Path('/tmp/data/foo.txt')`\n3. Print its `.name`, `.suffix` and `.stem` in turn\n\nThe output should be:\n```\nfoo.txt\n.txt\nfoo\n```\n\nNote: `print(p.name)` prints `foo.txt`, **not** `'foo.txt'` – printing directly shows no quotes.",
starter="# Import Path from pathlib and create a path object pointing to /tmp/data/foo.txt\n# Print its .name, .suffix and .stem in turn\n\n",
solution="from pathlib import Path\n\np = Path('/tmp/data/foo.txt')\nprint(p.name)\nprint(p.suffix)\nprint(p.stem)",
hints=["Import the Path class with from pathlib import Path", ".name is the full file name with its extension, .suffix is the extension with its dot, .stem is the name without the extension", "Full code:\nfrom pathlib import Path\np = Path('/tmp/data/foo.txt')\nprint(p.name)\nprint(p.suffix)\nprint(p.stem)"])

EX['python18/02-joining'] = dict(
title="Join paths with the / operator",
prompt="Use the `/` operator to join three parts into one full path:\n\n1. Import `Path` from `pathlib`\n2. Build the path with `Path('/home/user') / 'docs' / 'report.pdf'` and assign it to `p`\n3. `print(str(p))`\n\nThe output should be:\n```\n/home/user/docs/report.pdf\n```\n\nGoodbye `os.path.join`!",
starter="# Import Path from pathlib\n# Use the / operator to join /home/user, docs and report.pdf into the path p, then print it\n\n",
solution="from pathlib import Path\n\np = Path('/home/user') / 'docs' / 'report.pdf'\nprint(str(p))",
hints=["Path gives the / operator a new meaning, so you can write Path('/home/user') / 'docs' / 'report.pdf' directly", "str(p) turns a Path object into a string – print(p) directly works the same way", "Full code:\nfrom pathlib import Path\np = Path('/home/user') / 'docs' / 'report.pdf'\nprint(str(p))"])

EX['python18/03-parents'] = dict(
title="Get the parent and ancestor folders",
prompt="Here's `p = Path('/a/b/c/d.txt')` for you.\n\nPlease:\n\n1. `print(p.parent)` – the parent folder, one level up\n2. `print(p.parents[1])` – the ancestor two levels up\n\nThe output should be:\n```\n/a/b/c\n/a/b\n```\n\nNote: `.parent` is an attribute (no brackets), and `.parents[i]` is an index into a sequence – `[0]` is the direct parent, `[1]` is one level higher.",
starter="from pathlib import Path\n\np = Path('/a/b/c/d.txt')\n\n# Use .parent and .parents[1] to print the parent folder and the ancestor two levels up\n\n",
solution="from pathlib import Path\n\np = Path('/a/b/c/d.txt')\nprint(p.parent)\nprint(p.parents[1])",
hints=[".parent is the same as .parents[0] – both are the direct parent folder", ".parents[1] is .parent.parent, one more level up", "Full code:\nfrom pathlib import Path\np = Path('/a/b/c/d.txt')\nprint(p.parent)\nprint(p.parents[1])"])

EX['python18/04-suffixes'] = dict(
title="Files with several extensions: .suffixes",
prompt="For a file name with 'several extensions', like `foo.tar.gz`:\n\n- `.suffix` only gives the **last** extension (`.gz`)\n- `.suffixes` gives a **list** with all of them\n\nPlease:\n\n1. Import `Path` from `pathlib`\n2. Create `p = Path('test.tar.gz')`\n3. `print(p.suffixes)`\n\nThe output should be:\n```\n['.tar', '.gz']\n```",
starter="# Import Path from pathlib and create a path object pointing to test.tar.gz\n# Use .suffixes to print all its extensions\n\n",
solution="from pathlib import Path\n\np = Path('test.tar.gz')\nprint(p.suffixes)",
hints=[".suffix (singular) gives only the last one; .suffixes (plural) gives them all", "They're in order from left to right – ['.tar', '.gz']", "Full code:\nfrom pathlib import Path\np = Path('test.tar.gz')\nprint(p.suffixes)"])

EX['python19/01-safe-divide'] = dict(
title="safe_divide: handle dividing by zero with try/except",
prompt="Write a function `safe_divide(a, b)`:\n\n- Normally it returns `a / b`\n- If `b` is 0, it catches `ZeroDivisionError`, prints `'You cannot divide by zero'`, and returns `None`\n\nThen call:\n\n```python\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))\n```\n\nThe output should be:\n```\n5.0\nYou cannot divide by zero\nNone\n```\n\nNote: because `safe_divide(10, 0)` returns `None`, the outer `print` prints `None`.",
starter="# Define safe_divide(a, b), catching ZeroDivisionError with try/except\n# When dividing by zero, print the message first, then return None\n# Finally call it twice as asked and print the results\n\n",
solution="def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        print('You cannot divide by zero')\n        return None\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))",
hints=["Wrap a / b in try / except ZeroDivisionError", "In the except branch, print first, then return None", "Full code:\ndef safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        print('You cannot divide by zero')\n        return None\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))"])

EX['python19/02-parse-int'] = dict(
title="Catch ValueError",
prompt="Write a function `parse_int(s)`:\n\n- Try to turn `s` into an `int` and return it\n- If `int(s)` raises `ValueError`, catch it, print `f'Cannot convert: {s}'`, and return `0`\n\nThen call:\n\n```python\nprint(parse_int('42'))\nprint(parse_int('abc'))\nprint(parse_int('100'))\n```\n\nThe output should be:\n```\n42\nCannot convert: abc\n0\n100\n```",
starter="# Define parse_int(s), catching ValueError with try/except\n# If converting fails, print the message first, then return 0\n# Finally call it three times as asked and print the results\n\n",
solution="def parse_int(s):\n    try:\n        return int(s)\n    except ValueError:\n        print(f'Cannot convert: {s}')\n        return 0\n\nprint(parse_int('42'))\nprint(parse_int('abc'))\nprint(parse_int('100'))",
hints=["Wrap int(s) in try / except ValueError", "In the except branch, print first, then return 0", "Full code:\ndef parse_int(s):\n    try:\n        return int(s)\n    except ValueError:\n        print(f'Cannot convert: {s}')\n        return 0\n\nprint(parse_int('42'))\nprint(parse_int('abc'))\nprint(parse_int('100'))"])

EX['python19/03-finally'] = dict(
title="finally: clean-up always runs",
prompt="Write a function `do_work(x)`:\n\n- In `try`, print `'Starting work'`, then run `10 / x`\n- Use `except ZeroDivisionError` to catch dividing by zero, printing `'Divided by zero'`\n- Use `finally` to print `'Clean-up done'`\n\nThen call, in order:\n\n```python\ndo_work(2)\nprint('---')\ndo_work(0)\n```\n\nThe output should be:\n```\nStarting work\nClean-up done\n---\nStarting work\nDivided by zero\nClean-up done\n```\n\nNote: `do_work(2)` doesn't trigger `except`, but `finally` always runs.",
starter="# Define do_work(x), using try/except/finally for the three prints\n# The print in finally runs whether it worked or not\n# Finally call do_work(2), print the divider line, then do_work(0), as asked\n\n",
solution="def do_work(x):\n    try:\n        print('Starting work')\n        10 / x\n    except ZeroDivisionError:\n        print('Divided by zero')\n    finally:\n        print('Clean-up done')\n\ndo_work(2)\nprint('---')\ndo_work(0)",
hints=["The order is: try → except → finally", "finally runs whether it worked or failed", "Full code:\ndef do_work(x):\n    try:\n        print('Starting work')\n        10 / x\n    except ZeroDivisionError:\n        print('Divided by zero')\n    finally:\n        print('Clean-up done')\n\ndo_work(2)\nprint('---')\ndo_work(0)"])
