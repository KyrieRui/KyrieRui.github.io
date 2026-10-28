EX = {}
LOGCFG = "import logging\nimport sys\n\nlogging.basicConfig(\n    stream=sys.stdout,\n    level=logging.{lvl},\n    format='{fmt}',\n    force=True,\n)\n\n"
def cfg(lvl, fmt='%(levelname)s:%(message)s'):
    return LOGCFG.replace('{lvl}', lvl).replace('{fmt}', fmt)

EX['python19/04-raise-age'] = dict(
title="raise: raising an exception yourself",
prompt="Write a function `set_age(age)`:\n\n- If `age < 0`, `raise ValueError(f'Age cannot be negative: {age}')` yourself\n- Otherwise return `age`\n\nThen call `set_age(-5)` inside `try / except ValueError`, and when the exception is caught, print `f'Bad argument: {e}'`.\n\nThe output should be:\n```\nBad argument: Age cannot be negative: -5\n```",
starter="# Define set_age(age); when age is negative, use raise to throw a ValueError\n# Then wrap the call set_age(-5) in try/except ValueError as e and print the error message\n\n",
solution="def set_age(age):\n    if age < 0:\n        raise ValueError(f'Age cannot be negative: {age}')\n    return age\n\ntry:\n    set_age(-5)\nexcept ValueError as e:\n    print(f'Bad argument: {e}')",
hints=["raise ValueError('error message') – note the brackets", "Use except ValueError as e to get the exception object", "Full code:\ndef set_age(age):\n    if age < 0:\n        raise ValueError(f'Age cannot be negative: {age}')\n    return age\n\ntry:\n    set_age(-5)\nexcept ValueError as e:\n    print(f'Bad argument: {e}')"])

EX['python19/05-custom-exception'] = dict(
title="A custom exception: InvalidScoreError",
prompt="Define a custom exception class `InvalidScoreError` that inherits from `Exception`.\n\nThen write a function `check_score(score)`:\n\n- If `score < 0` or `score > 100`, raise `InvalidScoreError(f'Score {score} is not valid')`\n- Otherwise print `f'Score is valid: {score}'`\n\nThen run, in order:\n\n```python\ncheck_score(85)\ntry:\n    check_score(120)\nexcept InvalidScoreError as e:\n    print(f'Caught an exception: {e}')\n```\n\nThe output should be:\n```\nScore is valid: 85\nCaught an exception: Score 120 is not valid\n```",
starter="# Define an exception class InvalidScoreError that inherits from Exception\n# Write check_score(score): raise when the score is out of range, otherwise print the valid message\n# Call check_score(85) directly first, then call check_score(120) inside try/except\n\n",
solution="class InvalidScoreError(Exception):\n    pass\n\ndef check_score(score):\n    if score < 0 or score > 100:\n        raise InvalidScoreError(f'Score {score} is not valid')\n    print(f'Score is valid: {score}')\n\ncheck_score(85)\ntry:\n    check_score(120)\nexcept InvalidScoreError as e:\n    print(f'Caught an exception: {e}')",
hints=["class InvalidScoreError(Exception): pass is all you need", "In check_score, raise it with raise InvalidScoreError(...)", "Full code:\nclass InvalidScoreError(Exception):\n    pass\n\ndef check_score(score):\n    if score < 0 or score > 100:\n        raise InvalidScoreError(f'Score {score} is not valid')\n    print(f'Score is valid: {score}')\n\ncheck_score(85)\ntry:\n    check_score(120)\nexcept InvalidScoreError as e:\n    print(f'Caught an exception: {e}')"])

EX['python20/01-basic-point'] = dict(
title="Define Point with @dataclass",
prompt="Use the `@dataclass` decorator to define a `Point` class:\n\n- Two fields: `x: int` and `y: int`\n- Then create `Point(1, 2)`, assign it to the variable `p`, and `print(p)`\n\nThe output should be:\n```\nPoint(x=1, y=2)\n```\n\n(This is exactly the `__repr__` output that `dataclass` generates for you.)",
starter="# Import dataclass from dataclasses\n# Use @dataclass to define the Point class with two int fields, x and y (remember the type hints)\n# Create Point(1, 2), assign it to p, then print p\n\n",
solution="from dataclasses import dataclass\n\n@dataclass\nclass Point:\n    x: int\n    y: int\n\np = Point(1, 2)\nprint(p)",
hints=["Remember from dataclasses import dataclass", "Fields must have type hints: x: int, y: int", "Full code:\nfrom dataclasses import dataclass\n\n@dataclass\nclass Point:\n    x: int\n    y: int\n\np = Point(1, 2)\nprint(p)"])

EX['python20/02-default-factory'] = dict(
title="Mutable defaults: default_factory",
prompt="Use `@dataclass` to define a `Team` class:\n\n- A field `name: str`\n- A field `members: list`, whose default is an empty list given by `field(default_factory=list)`\n\nThen:\n\n```python\nt1 = Team('Team A')\nt2 = Team('Team B')\nt1.members.append('Xiao Ming')\nprint(t1)\nprint(t2)\n```\n\nThe output should be:\n```\nTeam(name='Team A', members=['Xiao Ming'])\nTeam(name='Team B', members=[])\n```\n\n(This checks that the two instances each have their own `members` list and don't share one.)",
starter="# Import dataclass and field from dataclasses\n# Define the Team class: name is a str; members is a list with the default field(default_factory=list)\n# Create t1 and t2 as above, add 'Xiao Ming' to t1.members, then print t1 and t2\n\n",
solution="from dataclasses import dataclass, field\n\n@dataclass\nclass Team:\n    name: str\n    members: list = field(default_factory=list)\n\nt1 = Team('Team A')\nt2 = Team('Team B')\nt1.members.append('Xiao Ming')\nprint(t1)\nprint(t2)",
hints=["Note: you need from dataclasses import dataclass, field", "Use field(default_factory=list), not just = []", "Full code:\nfrom dataclasses import dataclass, field\n\n@dataclass\nclass Team:\n    name: str\n    members: list = field(default_factory=list)\n\nt1 = Team('Team A')\nt2 = Team('Team B')\nt1.members.append('Xiao Ming')\nprint(t1)\nprint(t2)"])

EX['python20/03-frozen-hash'] = dict(
title="frozen=True: unchangeable + hashable",
prompt="Use `@dataclass(frozen=True)` to define a `Point` class (fields `x: int` and `y: int`), so that it can't be changed and can go into a `set`.\n\nThen:\n\n```python\np1 = Point(1, 2)\np2 = Point(1, 2)\np3 = Point(3, 4)\ns = {p1, p2, p3}\nprint(len(s))\n```\n\nBecause `p1` and `p2` have the same field values, the set treats them as the same item, so the output should be:\n```\n2\n```\n\nThis is a side effect of `frozen=True` – it generates `__hash__` for you.",
starter="# Use @dataclass(frozen=True) to define the Point class with two int fields, x and y\n# Create p1, p2 and p3 as above and put them in a set\n# Print the length of the set\n\n",
solution="from dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Point:\n    x: int\n    y: int\n\np1 = Point(1, 2)\np2 = Point(1, 2)\np3 = Point(3, 4)\ns = {p1, p2, p3}\nprint(len(s))",
hints=["Write the decorator as @dataclass(frozen=True)", "frozen=True generates __hash__ automatically, so the objects can go into a set", "Full code:\nfrom dataclasses import dataclass\n\n@dataclass(frozen=True)\nclass Point:\n    x: int\n    y: int\n\np1 = Point(1, 2)\np2 = Point(1, 2)\np3 = Point(3, 4)\ns = {p1, p2, p3}\nprint(len(s))"])

EX['python20/04-eq'] = dict(
title="Automatic __eq__: comparing by field values",
prompt="Use `@dataclass` to define a `Book` class:\n\n- `title: str`\n- `author: str`\n- `pages: int`\n\nThen create three books:\n\n```python\nb1 = Book('Python Basics', 'Xiao Ming', 300)\nb2 = Book('Python Basics', 'Xiao Ming', 300)\nb3 = Book('Python Basics', 'Xiao Ming', 500)\nprint(b1 == b2)\nprint(b1 == b3)\nprint(b1 is b2)\n```\n\nThe output should be:\n```\nTrue\nFalse\nFalse\n```\n\nExplanation: `==` compares field values (`b1` and `b2` are exactly the same, so it's `True`), while `is` compares identity (`b1` and `b2` are two different objects, so it's `False`).",
starter="# Use @dataclass to define the Book class: title and author are str, pages is int\n# Create the three books b1, b2 and b3 as above\n# Print the results of b1 == b2, b1 == b3 and b1 is b2\n\n",
solution="from dataclasses import dataclass\n\n@dataclass\nclass Book:\n    title: str\n    author: str\n    pages: int\n\nb1 = Book('Python Basics', 'Xiao Ming', 300)\nb2 = Book('Python Basics', 'Xiao Ming', 300)\nb3 = Book('Python Basics', 'Xiao Ming', 500)\nprint(b1 == b2)\nprint(b1 == b3)\nprint(b1 is b2)",
hints=["@dataclass generates __eq__ by default, comparing field by field", "== compares field values, is compares identity – two different things", "Full code:\nfrom dataclasses import dataclass\n\n@dataclass\nclass Book:\n    title: str\n    author: str\n    pages: int\n\nb1 = Book('Python Basics', 'Xiao Ming', 300)\nb2 = Book('Python Basics', 'Xiao Ming', 300)\nb3 = Book('Python Basics', 'Xiao Ming', 500)\nprint(b1 == b2)\nprint(b1 == b3)\nprint(b1 is b2)"])

EX['python21/01-with-stringio'] = dict(
title="Use with on a StringIO",
prompt="`io.StringIO` is a 'file in memory', and it also supports the context manager protocol.\n\nUse `with` together with `io.StringIO()`:\n\n1. Inside the `with` block, `write` the string `'Hello'`\n2. Inside the `with` block, `write` the string `' World'`\n3. Assign the result of `getvalue()` (`Hello World`) to the variable `text`\n4. `print(text)`\n\nThe output should be:\n```\nHello World\n```",
starter="import io\n# Open io.StringIO() with with, and write two strings inside the block\n# Inside the block, assign the result of getvalue() to text, then print text at the end\n\n",
solution="import io\nwith io.StringIO() as buf:\n    buf.write('Hello')\n    buf.write(' World')\n    text = buf.getvalue()\nprint(text)",
hints=["io.StringIO supports the with syntax too", "Assign text **inside** the with block – after with exits, buf is closed, but text is still there", "Full code:\nimport io\nwith io.StringIO() as buf:\n    buf.write('Hello')\n    buf.write(' World')\n    text = buf.getvalue()\nprint(text)"])

EX['python21/02-custom-class'] = dict(
title="A custom context manager class",
prompt="Define a class `Section` that follows the context manager protocol:\n\n- `__enter__` prints `'>>> Start'` and does `return self`\n- `__exit__` prints `'<<< End'`\n\nThen use `with Section():` around one line, `print('Working')`.\n\nThe output should be:\n```\n>>> Start\nWorking\n<<< End\n```",
starter="# Define the Section class with __enter__ and __exit__\n# __enter__ prints the start message and returns self; __exit__ prints the end message\n# Then use with on a Section instance, printing 'Working' inside the block\n\n",
solution="class Section:\n    def __enter__(self):\n        print('>>> Start')\n        return self\n\n    def __exit__(self, exc_type, exc_val, tb):\n        print('<<< End')\n\nwith Section():\n    print('Working')",
hints=["Both __enter__ and __exit__ must be defined in the class", "__exit__ must take 4 parameters: self, exc_type, exc_val, tb", "Full code:\nclass Section:\n    def __enter__(self):\n        print('>>> Start')\n        return self\n\n    def __exit__(self, exc_type, exc_val, tb):\n        print('<<< End')\n\nwith Section():\n    print('Working')"])

EX['python21/03-contextmanager'] = dict(
title="Write a banner with @contextmanager",
prompt="Use `@contextmanager` to write a **generator-function** context manager `banner(title)`:\n\n- On entering (before yield): print `f'==== {title} ===='`\n- yield (no value)\n- On exiting (after yield): print `'================'`\n\nThen use `with banner('Start task'):` around one line, `print('Working')`.\n\nThe output should be:\n```\n==== Start task ====\nWorking\n================\n```",
starter="from contextlib import contextmanager\n\n# Decorate the generator function banner(title) with @contextmanager\n# Print the opening banner before yield, and the closing line after yield (wrap yield in try/finally)\n# Then use with on banner('Start task'), printing 'Working' inside the block\n\n",
solution="from contextlib import contextmanager\n\n@contextmanager\ndef banner(title):\n    print(f'==== {title} ====')\n    try:\n        yield\n    finally:\n        print('================')\n\nwith banner('Start task'):\n    print('Working')",
hints=["@contextmanager only decorates generator functions, so you need yield", "What's before yield runs on entering; what's after yield runs on exiting", "Remember to wrap yield in try/finally so the clean-up always runs"])

EX['python21/04-suppress'] = dict(
title="Ignore an exception with contextlib.suppress",
prompt="Use `contextlib.suppress` to ignore `ZeroDivisionError`:\n\n1. Use `with suppress(ZeroDivisionError):` around `x = 1 / 0` (this line raises an exception, but it's swallowed)\n2. After the `with`, `print('done')`\n\nThe output should be:\n```\ndone\n```\n\n(The key point: the program doesn't crash because of the divide-by-zero error.)",
starter="from contextlib import suppress\n# Use with + suppress to ignore ZeroDivisionError, dividing by zero inside the block\n# After with ends, print done\n\n",
solution="from contextlib import suppress\nwith suppress(ZeroDivisionError):\n    x = 1 / 0\nprint('done')",
hints=["suppress(exception type) quietly swallows that kind of exception; other exceptions are still raised as usual", "Full code:\nfrom contextlib import suppress\nwith suppress(ZeroDivisionError):\n    x = 1 / 0\nprint('done')"])

EX['python22/01-hello'] = dict(
title="Your first async function",
prompt="Use `async def` to define a coroutine function `hello` that prints `'hi'`.\n\nThen start it with `asyncio.run(hello())`.\n\nThe output should be:\n```\nhi\n```",
starter="import asyncio\n\n# Use async def to define the coroutine function hello, which prints 'hi'\n# Then start it with asyncio.run\n\n",
solution="import asyncio\n\nasync def hello():\n    print('hi')\n\nasyncio.run(hello())",
hints=["async def is almost the same as def – it just has the extra async keyword", "In asyncio.run(hello()), note the brackets after hello() – you pass in a coroutine object", "Full code:\nimport asyncio\n\nasync def hello():\n    print('hi')\n\nasyncio.run(hello())"])

EX['python22/02-sleep-order'] = dict(
title="The order of awaits one after another",
prompt="Define a coroutine function `step(name)`:\n\n- First `print(f'{name} start')`\n- Then `await asyncio.sleep(0)`\n- Finally `print(f'{name} end')`\n\nThen define `main`: `await step('A')`, then `await step('B')`.\n\nStart it with `asyncio.run(main())`.\n\nThe output should be:\n```\nA start\nA end\nB start\nB end\n```\n\n(Explanation: because the `await`s run one after another, B always comes after A.)",
starter="import asyncio\n\n# Define the coroutine function step(name): print 'start', await asyncio.sleep(0), then print 'end'\n# Then define main: await step('A'), then await step('B')\n# Finally start main with asyncio.run\n\n",
solution="import asyncio\n\nasync def step(name):\n    print(f'{name} start')\n    await asyncio.sleep(0)\n    print(f'{name} end')\n\nasync def main():\n    await step('A')\n    await step('B')\n\nasyncio.run(main())",
hints=["Inside step: print → await asyncio.sleep(0) → print", "In main, write two awaits one after the other: await step('A') then await step('B')", "Full code:\nimport asyncio\n\nasync def step(name):\n    print(f'{name} start')\n    await asyncio.sleep(0)\n    print(f'{name} end')\n\nasync def main():\n    await step('A')\n    await step('B')\n\nasyncio.run(main())"])

EX['python22/03-gather-two'] = dict(
title="Run two coroutines at the same time with gather",
prompt="Define a coroutine function `task(name)`:\n\n- `await asyncio.sleep(0.01)`\n- Return `f'{name} done'`\n\nIn `main`, use `asyncio.gather(task('A'), task('B'))` to run both at the same time, assign the results to `r1, r2`, then **in order**:\n\n```python\nprint(r1)\nprint(r2)\n```\n\nStart it with `asyncio.run(main())`.\n\nThe output should be:\n```\nA done\nB done\n```\n\n(Note: `gather` returns results in the same order you passed them in, so the result here is always the same.)",
starter="import asyncio\n\n# Define the coroutine function task(name): sleep for 0.01 seconds, then return the name plus ' done'\n# In main, use asyncio.gather to run task('A') and task('B') at the same time, unpacking the results into r1 and r2\n# Print r1 and r2 in order, then start main with asyncio.run\n\n",
solution="import asyncio\n\nasync def task(name):\n    await asyncio.sleep(0.01)\n    return f'{name} done'\n\nasync def main():\n    r1, r2 = await asyncio.gather(task('A'), task('B'))\n    print(r1)\n    print(r2)\n\nasyncio.run(main())",
hints=["In task, first await asyncio.sleep(0.01), then return", "gather takes several coroutine objects: asyncio.gather(task('A'), task('B'))", "gather returns a list of results, which you can unpack into r1, r2"])

EX['python22/04-gather-fetch'] = dict(
title="Fetching at the same time (simulated)",
prompt="The browser sandbox can't go online, so we'll use `asyncio.sleep` to pretend to fetch something.\n\nDefine a coroutine function `fetch(url)`:\n\n- `await asyncio.sleep(0.01)` (pretending to wait for the network)\n- Return `f'fetched {url}'`\n\nIn `main`, use `asyncio.gather` to fetch three URLs at the same time: `'a'`, `'b'` and `'c'`, and assign the returned list to `results`. Then use a `for` loop to `print` each result in order.\n\nStart it with `asyncio.run(main())`.\n\nThe output should be:\n```\nfetched a\nfetched b\nfetched c\n```",
starter="import asyncio\n\n# Define the coroutine function fetch(url): pretend to wait 0.01 seconds, then return the fetched-result string\n# In main, use asyncio.gather to fetch 'a', 'b' and 'c' at the same time, assigning the results to results\n# Use a for loop to print each result in order, then start main with asyncio.run\n\n",
solution="import asyncio\n\nasync def fetch(url):\n    await asyncio.sleep(0.01)\n    return f'fetched {url}'\n\nasync def main():\n    results = await asyncio.gather(fetch('a'), fetch('b'), fetch('c'))\n    for r in results:\n        print(r)\n\nasyncio.run(main())",
hints=["The fetch function: after await asyncio.sleep(0.01), return f'fetched {url}'", "Gather the three coroutines: asyncio.gather(fetch('a'), fetch('b'), fetch('c'))", "The list from gather is in the same order you passed things in, so for r in results: print(r) is all you need"])

EX['python26/01-first-log'] = dict(
title="Your first log",
prompt="Use `logging.basicConfig` to set the log level to `INFO`, then use `logging.info` to log `'My first log'`.\n\nNote: the starter code already sets up logging to print to stdout with the simplified format `format='%(levelname)s:%(message)s'` – you only need to write the last line, `logging.info(...)`.\n\nThe output should be:\n```\nINFO:My first log\n```",
starter=cfg('INFO') + "# TODO: use logging.info to log 'My first log'\n",
solution=cfg('INFO') + "logging.info('My first log')",
hints=["logging.info('text') uses the root logger to log at INFO level", "The format is controlled by basicConfig's format – we've already set it to 'LEVEL:text'", "Full code:\n" + cfg('INFO') + "logging.info('My first log')"])

EX['python26/02-five-levels'] = dict(
title="The 5 log levels",
prompt="The starter code already sets the log level to `DEBUG` (the lowest level, so every log is shown).\n\nCall the 5 levels in this order:\n\n1. `logging.debug('Debug')`\n2. `logging.info('Info')`\n3. `logging.warning('Warning')`\n4. `logging.error('Error')`\n5. `logging.critical('Critical')`\n\nThe output should be:\n```\nDEBUG:Debug\nINFO:Info\nWARNING:Warning\nERROR:Error\nCRITICAL:Critical\n```",
starter=cfg('DEBUG') + "# TODO: log in the order debug → info → warning → error → critical\n",
solution=cfg('DEBUG') + "logging.debug('Debug')\nlogging.info('Info')\nlogging.warning('Warning')\nlogging.error('Error')\nlogging.critical('Critical')",
hints=["level=logging.DEBUG makes every level show up", "The order: debug → info → warning → error → critical", "Full code:\n" + cfg('DEBUG') + "logging.debug('Debug')\nlogging.info('Info')\nlogging.warning('Warning')\nlogging.error('Error')\nlogging.critical('Critical')"])

EX['python26/04-warning-only'] = dict(
title="Only WARNING and above",
prompt="The starter code already sets the log level to `logging.WARNING`. You only need to call, in order:\n\n```python\nlogging.info('info you cannot see')\nlogging.warning('warning you can see')\nlogging.error('error you can see')\n```\n\nBecause the level = WARNING, **INFO is filtered out**, leaving only WARNING / ERROR / CRITICAL.\n\nThe output should be:\n```\nWARNING:warning you can see\nERROR:error you can see\n```",
starter=cfg('WARNING') + "# TODO: three logging calls: info / warning / error\n",
solution=cfg('WARNING') + "logging.info('info you cannot see')\nlogging.warning('warning you can see')\nlogging.error('error you can see')",
hints=["level=logging.WARNING filters out INFO and DEBUG", "The three calls in order: info → warning → error", "Full code:\n" + cfg('WARNING') + "logging.info('info you cannot see')\nlogging.warning('warning you can see')\nlogging.error('error you can see')"])

EX['python26/03-named-logger'] = dict(
title="Name a logger with getLogger",
prompt="Use `logging.getLogger('app.punch')` to create a named logger, assign it to the variable `logger`, then use it to log `'User started check-in'`.\n\nThe starter code already changes the format to `'%(name)s:%(levelname)s:%(message)s'` – `%(name)s` prints the logger's name.\n\nThe output should be:\n```\napp.punch:INFO:User started check-in\n```",
starter=cfg('INFO', '%(name)s:%(levelname)s:%(message)s') + "# Use logging.getLogger to create a logger named 'app.punch' and assign it to the variable logger\n# Then use this logger to log 'User started check-in' at INFO level\n",
solution=cfg('INFO', '%(name)s:%(levelname)s:%(message)s') + "logger = logging.getLogger('app.punch')\nlogger.info('User started check-in')",
hints=["logging.getLogger('name') gets a named logger", "Log with that logger: logger.info(...)", "Full code:\n" + cfg('INFO', '%(name)s:%(levelname)s:%(message)s') + "logger = logging.getLogger('app.punch')\nlogger.info('User started check-in')"])
