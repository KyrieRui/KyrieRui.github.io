EX = {}
EX['python4/01-dict-create'] = dict(
title="Create a dict",
prompt="Create a dictionary `phone_book` that stores these three contacts:\n\n- `'Alice'` → `'13800001111'`\n- `'Bob'` → `'13800002222'`\n- `'Carol'` → `'13800003333'`\n\nThen `print(phone_book)`.\n\nThe output should be:\n```\n{'Alice': '13800001111', 'Bob': '13800002222', 'Carol': '13800003333'}\n```",
starter="# Use curly brackets {} to create a dict, written as {key: value, ...}\n",
solution="phone_book = {'Alice': '13800001111', 'Bob': '13800002222', 'Carol': '13800003333'}\nprint(phone_book)",
hints=["How to write a dict: {'key1': 'value1', 'key2': 'value2'}", "Full code:\nphone_book = {'Alice': '13800001111', 'Bob': '13800002222', 'Carol': '13800003333'}\nprint(phone_book)"])

EX['python4/02-dict-access'] = dict(
title="Get a value by its key",
prompt="We've already defined this for you:\n```python\nscores = {'English': 90, 'Maths': 85, 'Science': 78}\n```\n\nUse `print` to print the score for `Maths` (use `scores['Maths']`).\n\nThe output should be:\n```\n85\n```",
starter="scores = {'English': 90, 'Maths': 85, 'Science': 78}\n# Use scores['Maths'] to get the score and print it\n",
solution="scores = {'English': 90, 'Maths': 85, 'Science': 78}\nprint(scores['Maths'])",
hints=["Get a value with dict[key]", "Full code:\nscores = {'English': 90, 'Maths': 85, 'Science': 78}\nprint(scores['Maths'])"])

EX['python4/03-dict-modify'] = dict(
title="Add + change",
prompt="We've already defined this for you:\n```python\nscores = {'English': 90, 'Maths': 85}\n```\n\nPlease:\n\n1. Add a new item `'Science': 78`\n2. Change the `'Maths'` score to `92`\n3. `print(scores)`\n\nThe output should be:\n```\n{'English': 90, 'Maths': 92, 'Science': 78}\n```",
starter="scores = {'English': 90, 'Maths': 85}\n# First add the Science score, then change the Maths score, then print scores\n",
solution="scores = {'English': 90, 'Maths': 85}\nscores['Science'] = 78\nscores['Maths'] = 92\nprint(scores)",
hints=["Adding and changing are both dict[key] = value – if the key doesn't exist it's added, if it does it's overwritten", "Full code:\nscores = {'English': 90, 'Maths': 85}\nscores['Science'] = 78\nscores['Maths'] = 92\nprint(scores)"])

EX['python4/04-dict-merge'] = dict(
title="Merge two dicts with |",
prompt="We've already defined this for you:\n```python\nold = {'a': 1, 'b': 2}\nnew = {'b': 99, 'c': 3}\n```\n\nUse `|` to merge them into `merged` (note: the right side wins, so `'b'` should be 99), then `print(merged)`.\n\nThe output should be:\n```\n{'a': 1, 'b': 99, 'c': 3}\n```",
starter="old = {'a': 1, 'b': 2}\nnew = {'b': 99, 'c': 3}\n# Use | to merge the two dicts, assign the result to merged and print it\n",
solution="old = {'a': 1, 'b': 2}\nnew = {'b': 99, 'c': 3}\nmerged = old | new\nprint(merged)",
hints=["The | merge only exists in Python 3.9+", "'b': 99 on the right overwrites 'b': 2 on the left", "Full code:\nold = {'a': 1, 'b': 2}\nnew = {'b': 99, 'c': 3}\nmerged = old | new\nprint(merged)"])

EX['python4/05-set-dedup'] = dict(
title="Remove duplicates with a set",
prompt="We've already defined this for you:\n```python\nnums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\n```\n\nPlease:\n\n1. Turn `nums` into a `set` to remove duplicates\n2. Then use `sorted()` to sort the set into a list and assign it to `unique` (so the output order is always the same)\n3. `print(unique)`\n\nThe output should be:\n```\n[1, 2, 3, 4, 5, 6, 9]\n```",
starter="nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\n# First remove duplicates with set, then sort with sorted, assign to unique and print\n",
solution="nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nunique = sorted(set(nums))\nprint(unique)",
hints=["set(nums) removes duplicates automatically – each value is kept only once", "sorted(set) turns a set into a sorted list", "Full code:\nnums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nunique = sorted(set(nums))\nprint(unique)"])

EX['python4/06-set-add'] = dict(
title="A set's add",
prompt="We've already defined this for you:\n```python\ntags = {'python', 'web'}\n```\n\nPlease:\n\n1. Use `add` to add `'ai'`\n2. Use `add` to add `'python'` again (it's already there, so nothing changes)\n3. Use `print(sorted(tags))` to print the items **sorted** (so the output is always the same)\n\nThe output should be:\n```\n['ai', 'python', 'web']\n```",
starter="tags = {'python', 'web'}\n# Use add to add 'ai' and then 'python', then print the sorted tags\n",
solution="tags = {'python', 'web'}\ntags.add('ai')\ntags.add('python')\nprint(sorted(tags))",
hints=["tags.add(x) adds an item; adding the same value again does nothing", "A set has no order, so print's order isn't fixed – that's why we sort before printing", "Full code:\ntags = {'python', 'web'}\ntags.add('ai')\ntags.add('python')\nprint(sorted(tags))"])

EX['python4/07-set-ops'] = dict(
title="Find the intersection",
prompt="We've already defined this for you:\n```python\na = {1, 2, 3, 4, 5}\nb = {3, 4, 5, 6, 7}\n```\n\nUse `&` to find the **intersection** of `a` and `b` (the items both have), then use `sorted()` to turn it into a sorted list, assign it to `common`, and `print(common)`.\n\nThe output should be:\n```\n[3, 4, 5]\n```",
starter="a = {1, 2, 3, 4, 5}\nb = {3, 4, 5, 6, 7}\n# Use & for the intersection, sort it with sorted, assign to common and print\n",
solution="a = {1, 2, 3, 4, 5}\nb = {3, 4, 5, 6, 7}\ncommon = sorted(a & b)\nprint(common)",
hints=["a & b gives the intersection of two sets", "sorted() turns it into a sorted list so the output is stable", "Full code:\na = {1, 2, 3, 4, 5}\nb = {3, 4, 5, 6, 7}\ncommon = sorted(a & b)\nprint(common)"])

EX['python5/01-if-basic'] = dict(
title="if / else: pass or fail",
prompt="We've already defined `score = 75` for you.\n\nUse `if / else` to decide:\n\n- If `score >= 60`: `print('Pass')`\n- Otherwise: `print('Fail')`\n\nThe output should be:\n```\nPass\n```",
starter="score = 75\n# Use if / else to decide\n",
solution="score = 75\nif score >= 60:\n    print('Pass')\nelse:\n    print('Fail')",
hints=["if needs a colon at the end, and the next line is indented by 4 spaces", "Full code:\nscore = 75\nif score >= 60:\n    print('Pass')\nelse:\n    print('Fail')"])

EX['python5/02-if-elif'] = dict(
title="elif: grade levels",
prompt="We've already defined `score = 85` for you.\n\nUse `if / elif / else` to print a grade with these rules:\n\n- `>= 90`: `'Excellent'`\n- `>= 80`: `'Good'`\n- `>= 60`: `'Pass'`\n- anything else: `'Fail'`\n\nThe output should be:\n```\nGood\n```",
starter="score = 85\n# Use if / elif / else to decide\n",
solution="score = 85\nif score >= 90:\n    print('Excellent')\nelif score >= 80:\n    print('Good')\nelif score >= 60:\n    print('Pass')\nelse:\n    print('Fail')",
hints=["elif is short for else if", "Check from strictest to loosest: >= 90 → >= 80 → >= 60 → else", "Full code:\nscore = 85\nif score >= 90:\n    print('Excellent')\nelif score >= 80:\n    print('Good')\nelif score >= 60:\n    print('Pass')\nelse:\n    print('Fail')"])

EX['python5/03-if-and-or'] = dict(
title="and / or: combined conditions",
prompt="We've already defined this for you:\n```python\nage = 22\nhas_id = True\n```\n\nUse `and` to decide: **when `age >= 18` and `has_id` is True**, print `'Come in'`, otherwise print `'Sorry, no entry'`.\n\nThe output should be:\n```\nCome in\n```",
starter="age = 22\nhas_id = True\n# Use if + and to decide\n",
solution="age = 22\nhas_id = True\nif age >= 18 and has_id:\n    print('Come in')\nelse:\n    print('Sorry, no entry')",
hints=["Both conditions must be true: join them with and", "has_id is already a bool, so just write has_id – no need for has_id == True", "Full code:\nage = 22\nhas_id = True\nif age >= 18 and has_id:\n    print('Come in')\nelse:\n    print('Sorry, no entry')"])

EX['python5/04-match-case'] = dict(
title="match / case: handling commands",
prompt="We've already defined `command = 'pause'` for you.\n\nUse `match / case` to `print` with these rules:\n\n- `'start'` → `'Starting'`\n- `'stop'` → `'Stopping'`\n- `'pause'` → `'Paused'`\n- anything else → `'Unknown command'`\n\nThe output should be:\n```\nPaused\n```",
starter="command = 'pause'\n# Use match / case to match command and print the right text for each of the four cases\n# Don't forget case _ as a catch-all that prints 'Unknown command'\n",
solution="command = 'pause'\nmatch command:\n    case 'start':\n        print('Starting')\n    case 'stop':\n        print('Stopping')\n    case 'pause':\n        print('Paused')\n    case _:\n        print('Unknown command')",
hints=["After match comes the variable to match; after each case comes a value to match (match needs Python 3.10+, and this page runs 3.12, so it's fine)", "case _ is the catch-all, like else", "Full code:\ncommand = 'pause'\nmatch command:\n    case 'start':\n        print('Starting')\n    case 'stop':\n        print('Stopping')\n    case 'pause':\n        print('Paused')\n    case _:\n        print('Unknown command')"])

EX['python5/05-for-range'] = dict(
title="for + range: adding up",
prompt="Use a `for` loop with `range` to work out **the sum of 1 to 10** (including 10), assign it to the variable `total`, then `print(total)`.\n\nThe output should be:\n```\n55\n```",
starter="# First set total to 0\n# Use for + range to go through 1 to 10, adding each one to total\n# Print total after the loop\n",
solution="total = 0\nfor n in range(1, 11):\n    total = total + n\nprint(total)",
hints=["range(1, 11) gives 1 to 10 (the end isn't included, so write 11 to include 10)", "Add up inside the loop: total = total + n", "Full code:\ntotal = 0\nfor n in range(1, 11):\n    total = total + n\nprint(total)"])

EX['python5/06-while'] = dict(
title="while: countdown",
prompt="Use a `while` loop to count down from 5 to 1 (including 1), printing each number on its own line.\n\nThe output should be:\n```\n5\n4\n3\n2\n1\n```",
starter="# First make a countdown variable n, starting at 5\n# Use a while loop: each time, print n, then take 1 away from n, until 1 has been printed\n",
solution="n = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1",
hints=["Condition: while n >= 1", "Inside the loop you need n = n - 1, or the loop never ends", "Full code:\nn = 5\nwhile n >= 1:\n    print(n)\n    n = n - 1"])

EX['python5/07-break-continue'] = dict(
title="continue: sum of the odd numbers from 1 to 10",
prompt="Use `for + range` to go through 1 to 10. **Skip even numbers with `continue`**, add up the odd numbers into `total`, and finally `print(total)`.\n\nThe output should be:\n```\n25\n```\n\n(1 + 3 + 5 + 7 + 9 = 25)",
starter="# First set total to 0, then use for + range to go through 1 to 10\n# Skip even numbers with continue, add odd numbers to total\n# Finally print total\n",
solution="total = 0\nfor n in range(1, 11):\n    if n % 2 == 0:\n        continue\n    total = total + n\nprint(total)",
hints=["n % 2 == 0 means n is even (the remainder after dividing by 2 is 0)", "continue stops this round of the loop and moves on to the next one", "Full code:\ntotal = 0\nfor n in range(1, 11):\n    if n % 2 == 0:\n        continue\n    total = total + n\nprint(total)"])

EX['python6/01-define-add'] = dict(
title="Define an add function",
prompt="Define a function `add(a, b)` that returns `a + b`.\n\nThen call `add(3, 5)`, assign the result to `result`, and `print(result)`.\n\nThe output should be:\n```\n8\n```",
starter="# Use def to define the add function, returning the sum of its two parameters\n# Call it, assign the result to result, then print it\n",
solution="def add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)",
hints=["Define a function with the def keyword", "Inside the function: return a + b", "Full code:\ndef add(a, b):\n    return a + b\n\nresult = add(3, 5)\nprint(result)"])

EX['python6/02-multi-return'] = dict(
title="Returning several values",
prompt="Define a function `min_max(nums)` that takes a list and returns **the smallest and the biggest value** – two numbers (return them with a comma).\n\nThen call `min_max([3, 1, 4, 1, 5, 9, 2, 6])`, **unpack** the result into two variables `lo` and `hi`, and `print(lo)` and `print(hi)`.\n\nThe output should be:\n```\n1\n9\n```",
starter="# Define min_max and return the smallest and biggest values together, separated by a comma\n# Call it, unpack the result into lo and hi, and print each one\n",
solution="def min_max(nums):\n    return min(nums), max(nums)\n\nlo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])\nprint(lo)\nprint(hi)",
hints=["return min(nums), max(nums) returns two values at once (really a tuple)", "Unpack: lo, hi = min_max(...)", "Full code:\ndef min_max(nums):\n    return min(nums), max(nums)\n\nlo, hi = min_max([3, 1, 4, 1, 5, 9, 2, 6])\nprint(lo)\nprint(hi)"])

EX['python6/03-default-arg'] = dict(
title="Default parameters",
prompt="Define a function `greet(name, greeting='Hello')`: the first parameter `name` must be given, and the second parameter `greeting` defaults to `'Hello'`. The function prints `f'{greeting}, {name}!'`.\n\nThen:\n1. Call `greet('Alice')` (using the default greeting)\n2. Call `greet('Bob', 'Good morning')` (replacing the default)\n\nThe output should be:\n```\nHello, Alice!\nGood morning, Bob!\n```",
starter="# Define greet: name must be given, greeting defaults to 'Hello'\n# Inside the function, use an f-string to print the greeting\n# Call it twice as asked: once with the default, once replacing it\n",
solution="def greet(name, greeting='Hello'):\n    print(f'{greeting}, {name}!')\n\ngreet('Alice')\ngreet('Bob', 'Good morning')",
hints=["How to write a default parameter: def greet(name, greeting='Hello'):", "If you don't pass the second argument, the default is used", "Full code:\ndef greet(name, greeting='Hello'):\n    print(f'{greeting}, {name}!')\n\ngreet('Alice')\ngreet('Bob', 'Good morning')"])

EX['python6/04-args'] = dict(
title="*args: any number of arguments",
prompt="Define a function `total(*nums)` that adds up all the numbers passed in and returns the result.\n\nThen:\n1. Call `total(1, 2, 3)` and assign it to `a`\n2. Call `total(1, 2, 3, 4, 5, 6)` and assign it to `b`\n3. `print(a)` `print(b)`\n\nThe output should be:\n```\n6\n21\n```",
starter="# Use *nums to define total, adding up all the numbers passed in and returning the sum\n# Call it twice as asked, assign to a and b, and print each one\n",
solution="def total(*nums):\n    s = 0\n    for n in nums:\n        s = s + n\n    return s\n\na = total(1, 2, 3)\nb = total(1, 2, 3, 4, 5, 6)\nprint(a)\nprint(b)",
hints=["*nums collects any number of arguments into a tuple", "Inside the function, add them up with for n in nums, or just return sum(nums)", "Full code:\ndef total(*nums):\n    s = 0\n    for n in nums:\n        s = s + n\n    return s\n\na = total(1, 2, 3)\nb = total(1, 2, 3, 4, 5, 6)\nprint(a)\nprint(b)"])

EX['python6/05-lambda'] = dict(
title="lambda: sorting with an anonymous function",
prompt="We've already defined this for you:\n```python\nusers = [\n    {'name': 'Alice', 'age': 30},\n    {'name': 'Bob', 'age': 25},\n    {'name': 'Carol', 'age': 28},\n]\n```\n\nUse `sorted` with a **lambda** to sort `users` by `age` from youngest to oldest, assign it to `sorted_users`, then use a `for` loop to `print` each person's `name` and `age` (separated by a space).\n\nThe output should be:\n```\nBob 25\nCarol 28\nAlice 30\n```",
starter="users = [\n    {'name': 'Alice', 'age': 30},\n    {'name': 'Bob', 'age': 25},\n    {'name': 'Carol', 'age': 28},\n]\n# Use sorted with a lambda to sort by age (smallest first), assign to sorted_users\n# Then use a for loop to print each person's name and age\n",
solution="users = [\n    {'name': 'Alice', 'age': 30},\n    {'name': 'Bob', 'age': 25},\n    {'name': 'Carol', 'age': 28},\n]\nsorted_users = sorted(users, key=lambda u: u['age'])\nfor u in sorted_users:\n    print(u['name'], u['age'])",
hints=["sorted's key parameter takes a function: it's used on each item to make the 'thing to sort by'", "lambda u: u['age'] is the same as def f(u): return u['age']", "Full code:\nusers = [\n    {'name': 'Alice', 'age': 30},\n    {'name': 'Bob', 'age': 25},\n    {'name': 'Carol', 'age': 28},\n]\nsorted_users = sorted(users, key=lambda u: u['age'])\nfor u in sorted_users:\n    print(u['name'], u['age'])"])

EX['python7/01-for-iterate'] = dict(
title="Add up a list with for",
prompt="Here's a list for you:\n\n```python\nnumbers = [1, 2, 3, 4, 5]\n```\n\nUse a `for` loop to add up all the items in `numbers`, put the result in the variable `total`, then `print(total)`.\n\nThe output should be:\n```\n15\n```",
starter="numbers = [1, 2, 3, 4, 5]\n# First set total to 0, then use a for loop to add each item to it\n# Print total after the loop\n",
solution="numbers = [1, 2, 3, 4, 5]\ntotal = 0\nfor n in numbers:\n    total = total + n\nprint(total)",
hints=["Inside the for loop, add each n to total", "Remember to print(total) after the loop, not inside it", "Full code:\nnumbers = [1, 2, 3, 4, 5]\ntotal = 0\nfor n in numbers:\n    total = total + n\nprint(total)"])

EX['python7/02-iter-next'] = dict(
title="Take items one by one with iter and next",
prompt="Here's a list for you:\n\n```python\nnums = [10, 20, 30]\n```\n\nPlease:\n\n1. Use `iter()` to turn `nums` into an iterator and assign it to the variable `it`.\n2. Use `next(it)` three times in a row, printing each one.\n\nThe output should be:\n```\n10\n20\n30\n```",
starter="nums = [10, 20, 30]\n# Use iter() to turn nums into an iterator, assign it to it\n# Then use next(it) three times, printing each one\n",
solution="nums = [10, 20, 30]\nit = iter(nums)\nprint(next(it))\nprint(next(it))\nprint(next(it))",
hints=["iter(nums) turns a list into an iterator object", "Each call to next(it) gives you the next item", "Full code:\nnums = [10, 20, 30]\nit = iter(nums)\nprint(next(it))\nprint(next(it))\nprint(next(it))"])

EX['python7/03-list-comp'] = dict(
title="List comprehension: squares of even numbers",
prompt="Use **one line** of list comprehension to make the **squares of all the even numbers** from 1 to 10 (including 10), assign it to the variable `result`, then `print(result)`.\n\nThe output should be:\n```\n[4, 16, 36, 64, 100]\n```",
starter="# result = [... for ... in range(...) if ...]\n# print(result)\n",
solution="result = [x * x for x in range(1, 11) if x % 2 == 0]\nprint(result)",
hints=["1 to 10 (including 10) is range(1, 11)", "Checking for even: x % 2 == 0", "Full code:\nresult = [x * x for x in range(1, 11) if x % 2 == 0]\nprint(result)"])

EX['python7/04-generator'] = dict(
title="Write a generator function",
prompt="Define a **generator function** `count_up(n)` that `yield`s `1, 2, ..., n` in turn.\n\nThen use a `for` loop to go through `count_up(5)`, printing each value (one number per line).\n\nThe output should be:\n```\n1\n2\n3\n4\n5\n```",
starter="# Define a generator function count_up(n) that yields 1 to n in turn\n# Then use a for loop over count_up(5), printing each one\n",
solution="def count_up(n):\n    for i in range(1, n + 1):\n        yield i\n\nfor x in count_up(5):\n    print(x)",
hints=["Change print(i) in a normal function to yield i, and it becomes a generator function", "Use range(1, n + 1) so that n itself is included", "Full code:\ndef count_up(n):\n    for i in range(1, n + 1):\n        yield i\n\nfor x in count_up(5):\n    print(x)"])
