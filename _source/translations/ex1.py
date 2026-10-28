EX = {}
EX['python1/01-hello-python'] = dict(
title="Say hello to Python",
prompt="Write one line of code that makes the program print:\n\n```\nHello, Python!\n```\n\nCopy it exactly – a capital **H** and **P**, a comma, a space and an exclamation mark.",
starter="# Use print() to print one sentence\n",
solution="print('Hello, Python!')",
hints=["Call the print() function and put the text inside single or double quotes", "Check the punctuation: a comma after Hello, then a space, and ! at the end", "Full code:\nprint('Hello, Python!')"])

EX['python2/01-hello-world'] = dict(
title="Print Hello, World!",
prompt="Use the `print` function to print `Hello, World!` (note the capital letters; there's a comma and an exclamation mark, and one space after the comma).",
starter="# Write your code here\n",
solution="print('Hello, World!')",
hints=["Use the print function", "Strings need quotes (single ' or double \" both work)", "The full code is roughly: print('Hello, World!')"])

EX['python2/09-string-basics'] = dict(
title="Strings: writing a string that contains double quotes",
prompt="Define a variable `quote` that stores this string:\n\n```\nHe said: \"Python is so much fun!\"\n```\n\nNotice the pair of **double quotes** `\"` inside it.\n\nTip: when a string contains double quotes, the easiest way is to use single quotes `'...'` or triple quotes `'''...'''` on the outside (you can still use double quotes outside, but then every double quote inside needs a backslash to escape it – a hassle).\n\nThen print it with `print(quote)`.",
starter="# The string contains double quotes, so use single or triple quotes outside\n",
solution="quote = 'He said: \"Python is so much fun!\"'\nprint(quote)",
hints=["Use single quotes '...' outside, then you can put double quotes straight inside", "Triple quotes '''...''' work too", "Full code:\nquote = 'He said: \"Python is so much fun!\"'\nprint(quote)"])

EX['python2/03-arithmetic'] = dict(
title="Basic arithmetic",
prompt="Use `print` to print the result of `48 + 56`.\n\nJust write `48 + 56` inside the brackets of `print()` – Python works it out first, then prints it.\n\nThe output should be:\n```\n104\n```",
starter="# Use print to print the result of 48 + 56\n",
solution="print(48 + 56)",
hints=["Numbers don't need quotes – just write 48 + 56", "Put the whole thing inside print(): print(48 + 56)"])

EX['python2/10-bool-logic'] = dict(
title="Booleans: and / or / not",
prompt="Use `print` to print the results of these three boolean operations, one per line:\n\n1. `True and False`\n2. `True or False`\n3. `not True`\n\nThe output should be:\n```\nFalse\nTrue\nFalse\n```",
starter="# Three print lines, one for each boolean expression\n",
solution="print(True and False)\nprint(True or False)\nprint(not True)",
hints=["True and False both start with a capital letter", "Just print(expression) – Python works out True/False first, then prints it", "Full code:\nprint(True and False)\nprint(True or False)\nprint(not True)"])

EX['python2/04-string-concat'] = dict(
title="Build a sentence with an f-string",
prompt="We've already defined `name = 'Brother Shui'` and `age = 28` for you.\n\nUse an **f-string** to build `My name is Brother Shui and I am 28 years old.`, assign it to the variable `intro`, then print it.\n\nNote:\n- You must use an f-string (not `+` to join pieces by hand)\n- `Brother Shui` and `28` must be put in with `{name}` and `{age}` – don't type them straight into the string\n- There's a full stop `.` at the end\n\nThe output should be:\n```\nMy name is Brother Shui and I am 28 years old.\n```",
starter="name = 'Brother Shui'\nage = 28\n# Use an f-string to build the sentence, assign it to intro and print it\n",
solution="name = 'Brother Shui'\nage = 28\nintro = f'My name is {name} and I am {age} years old.'\nprint(intro)",
hints=["How to write an f-string: put f in front of the string, like f'My name is {name}'", "Write the variable name inside {} and it gets replaced by the variable's value", "Full code:\nname = 'Brother Shui'\nage = 28\nintro = f'My name is {name} and I am {age} years old.'\nprint(intro)"])

EX['python2/07-ascii-code'] = dict(
title="See the ASCII codes",
prompt="Above, we saw that the capital letter `A` has ASCII code **65**, and the small letter `z` has ASCII code **122**.\n\nIn Python, `ord('A')` gives you a character's ASCII code.\n\nUse one `print` to print the ASCII codes of `A` and `z` together, separated by a space.\n\nTip: `print` can take several values at once, separated by commas, like `print(a, b)` – it joins them with spaces automatically.\n\nThe output should be:\n```\n65 122\n```",
starter="# Use print to print ord('A') and ord('z') together\n",
solution="print(ord('A'), ord('z'))",
hints=["ord('A') returns 65, ord('z') returns 122", "print takes several arguments separated by commas and joins them with spaces: print(a, b)", "Full code: print(ord('A'), ord('z'))"])

EX['python2/08-type-conversion'] = dict(
title="Turn a string into an integer",
prompt="We've already defined `age_str = '28'` for you – it's a **string**, not an integer.\n\nAdding a number to a string directly gives an error, so first turn it into an integer with `int()`. Please:\n\n1. Use `int(age_str)` to turn it into an integer and assign it to the variable `age`\n2. Print `age + 2`\n\nThe output should be:\n```\n30\n```",
starter="age_str = '28'\n# 1. Use int(age_str) to make an integer and assign it to age\n# 2. Print age + 2\n",
solution="age_str = '28'\nage = int(age_str)\nprint(age + 2)",
hints=["int('28') returns the integer 28", "Assign it to a variable: age = int(age_str)", "Full code:\nage_str = '28'\nage = int(age_str)\nprint(age + 2)"])

EX['python2/02-variable-assign'] = dict(
title="Assign a variable and print it",
prompt="Create a variable `name`, assign the string `'Brother Shui'` to it, then use `print` to print `name`.\n\nThe output should be:\n```\nBrother Shui\n```",
starter="# Write your code here\n",
solution="name = 'Brother Shui'\nprint(name)",
hints=["Use = to assign the string 'Brother Shui' to the variable name", "Then print it with print(name) (note: print(name), not print('name'))", "Full code:\nname = 'Brother Shui'\nprint(name)"])

EX['python2/05-combined'] = dict(
title="Put it together: variables + maths + f-string",
prompt="We've already defined `apples = 12` and `oranges = 8` for you.\n\nPlease do two things:\n\n1. Add `apples` and `oranges` together and assign the result to the variable `total`\n2. Use an **f-string** to print `There are 20 pieces of fruit.` (the `20` must come from the `total` variable – don't type the number in)\n\nThe output should be:\n```\nThere are 20 pieces of fruit.\n```",
starter="apples = 12\noranges = 8\n# 1. Assign apples + oranges to total\n# 2. Use an f-string to print \"There are X pieces of fruit.\", with X from total\n",
solution="apples = 12\noranges = 8\ntotal = apples + oranges\nprint(f'There are {total} pieces of fruit.')",
hints=["Step 1: add apples and oranges and store the result in a new variable, total", "Step 2: print(f'There are {total} pieces of fruit.')", "Check the spaces and the full stop: one space on each side of the number, and . at the end"])

EX['python3/01-create-list'] = dict(
title="Create your first List",
prompt="Create a variable `numbers` and put the integers `1, 2, 3, 4, 5` into a List assigned to it.\n\nThen use `print` to print `numbers`.\n\nThe output should be:\n```\n[1, 2, 3, 4, 5]\n```",
starter="# Use square brackets [] to create a List, with commas between the items\n",
solution="numbers = [1, 2, 3, 4, 5]\nprint(numbers)",
hints=["A List is written as [item1, item2, ...]", "Full code:\nnumbers = [1, 2, 3, 4, 5]\nprint(numbers)"])

EX['python3/02-list-access'] = dict(
title="Indexes and slices",
prompt="We've already defined `fruits = ['apple', 'banana', 'cherry', 'date', 'fig']` for you.\n\nPlease:\n\n1. Use an index to `print` the 3rd item (that's `cherry`)\n2. Use a slice to `print` `fruits[1:4]`\n\nThe output should be:\n```\ncherry\n['banana', 'cherry', 'date']\n```",
starter="fruits = ['apple', 'banana', 'cherry', 'date', 'fig']\n# 1. print the 3rd item (indexes start at 0)\n# 2. print the slice fruits[1:4]\n",
solution="fruits = ['apple', 'banana', 'cherry', 'date', 'fig']\nprint(fruits[2])\nprint(fruits[1:4])",
hints=["Indexes start at 0, so the 3rd item is fruits[2]", "The slice [1:4] includes the start but not the end: indexes 1, 2 and 3, but not 4", "Full code:\nfruits = ['apple', 'banana', 'cherry', 'date', 'fig']\nprint(fruits[2])\nprint(fruits[1:4])"])

EX['python3/03-list-update'] = dict(
title="Change + append",
prompt="We've already defined `colors = ['red', 'green', 'blue']` for you.\n\nPlease:\n\n1. Change the item at index 1 (`green`) to capital `GREEN`\n2. Use `append` to add `'yellow'` to the end\n3. `print(colors)`\n\nThe output should be:\n```\n['red', 'GREEN', 'blue', 'yellow']\n```",
starter="colors = ['red', 'green', 'blue']\n# 1. Change the item at index 1 to capital 'GREEN'\n# 2. Use append to add 'yellow' to the end\n# 3. Print colors\n",
solution="colors = ['red', 'green', 'blue']\ncolors[1] = 'GREEN'\ncolors.append('yellow')\nprint(colors)",
hints=["Change one position: colors[1] = 'GREEN'", "Add to the end: colors.append('yellow')", "Full code:\ncolors = ['red', 'green', 'blue']\ncolors[1] = 'GREEN'\ncolors.append('yellow')\nprint(colors)"])

EX['python3/04-list-ops'] = dict(
title="Joining and length",
prompt="We've already defined `a = [1, 2, 3]` and `b = [4, 5, 6]` for you.\n\nPlease:\n\n1. Use `+` to join them into a new list `c`\n2. `print(c)`\n3. Use `len()` to print how many items `c` has\n\nThe output should be:\n```\n[1, 2, 3, 4, 5, 6]\n6\n```",
starter="a = [1, 2, 3]\nb = [4, 5, 6]\n# 1. Use + to join a and b into a new list c\n# 2. Print c\n# 3. Use len to print how many items c has\n",
solution="a = [1, 2, 3]\nb = [4, 5, 6]\nc = a + b\nprint(c)\nprint(len(c))",
hints=["Lists can be joined with +: c = a + b", "len(c) returns how many items the list has", "Full code:\na = [1, 2, 3]\nb = [4, 5, 6]\nc = a + b\nprint(c)\nprint(len(c))"])

EX['python3/05-tuple-create'] = dict(
title="The comma trap of a one-item tuple",
prompt="Create a tuple `t` with **only one item**, `42`, then `print(t)`.\n\nNote: a one-item tuple **must** have a comma after the item – `(42,)` is a tuple, but `(42)` is just the number 42.\n\nThe output should be:\n```\n(42,)\n```",
starter="# A one-item tuple needs a comma\n",
solution="t = (42,)\nprint(t)",
hints=["(42) is a number expression, not a tuple", "(42,) is a tuple – notice the comma", "Full code:\nt = (42,)\nprint(t)"])

EX['python3/06-tuple-access'] = dict(
title="Getting values and slices from a tuple",
prompt="We've already defined `days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')` for you.\n\nPlease:\n\n1. `print` the 4th item (that's `Thu`)\n2. `print` the slice `days[2:4]`\n\nThe output should be:\n```\nThu\n('Wed', 'Thu')\n```",
starter="days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')\n# 1. Use an index to print the 4th item\n# 2. print the slice days[2:4]\n",
solution="days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')\nprint(days[3])\nprint(days[2:4])",
hints=["Indexes start at 0, so the 4th item is days[3]", "Slices work just like with a List: days[2:4]", "Full code:\ndays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri')\nprint(days[3])\nprint(days[2:4])"])

EX['python3/07-tuple-ops'] = dict(
title="List to tuple + max",
prompt="We've already defined `nums = [3, 1, 4, 1, 5, 9, 2, 6]` for you.\n\nPlease:\n\n1. Use `tuple()` to turn it into a tuple and assign it to `t`\n2. `print` how many items the tuple has (`len`)\n3. `print` the biggest value in the tuple (`max`)\n\nThe output should be:\n```\n8\n9\n```",
starter="nums = [3, 1, 4, 1, 5, 9, 2, 6]\n# 1. Use tuple() to turn nums into a tuple and assign it to t\n# 2. Use len to print how many items it has\n# 3. Use max to print the biggest value\n",
solution="nums = [3, 1, 4, 1, 5, 9, 2, 6]\nt = tuple(nums)\nprint(len(t))\nprint(max(t))",
hints=["tuple(nums) turns a list into a tuple", "len counts the items, max finds the biggest value", "Full code:\nnums = [3, 1, 4, 1, 5, 9, 2, 6]\nt = tuple(nums)\nprint(len(t))\nprint(max(t))"])
