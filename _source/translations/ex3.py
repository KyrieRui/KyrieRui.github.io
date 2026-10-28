EX = {}
EX['python7/05-zip-pair'] = dict(
title="Pair up two lists with zip",
prompt="Here are two lists for you:\n\n```python\nnames = ['Alice', 'Bob', 'Cathy']\nages = [18, 19, 20]\n```\n\nUse `zip()` to pair them up, then use a `for` loop to print each pair in the format `name age` (with **one space** between).\n\nThe output should be:\n```\nAlice 18\nBob 19\nCathy 20\n```",
starter="names = ['Alice', 'Bob', 'Cathy']\nages = [18, 19, 20]\n# Use zip to pair the two lists; in the for loop, unpack into name and age and print each pair\n",
solution="names = ['Alice', 'Bob', 'Cathy']\nages = [18, 19, 20]\nfor name, age in zip(names, ages):\n    print(name, age)",
hints=["zip(names, ages) takes one item from each list at the same time, making (name, age)", "Unpack straight in the for: for name, age in zip(...)", "print(name, age) separates them with a space by default", "Full code:\nnames = ['Alice', 'Bob', 'Cathy']\nages = [18, 19, 20]\nfor name, age in zip(names, ages):\n    print(name, age)"])

EX['python8/01-class-basic'] = dict(
title="Define your first class",
prompt="Define a class `Animal` with one method, `sound`, which prints `'Some sound'`.\n\nThen:\n1. Create an instance `Animal()` and assign it to `a`\n2. Call `a.sound()`\n\nThe output should be:\n```\nSome sound\n```",
starter="# Define the class Animal, with a sound method that prints the text asked for\n# Then create an instance, assign it to a, and call a.sound()\n\n",
solution="class Animal:\n    def sound(self):\n        print('Some sound')\n\na = Animal()\na.sound()",
hints=["Define a class with class. A method is like a function, but its first parameter must be self", "Create an instance: a = Animal(); call the method: a.sound()", "Full code:\nclass Animal:\n    def sound(self):\n        print('Some sound')\n\na = Animal()\na.sound()"])

EX['python8/02-init'] = dict(
title="Pass values to an object with __init__",
prompt="Define a class `Person`:\n\n- `__init__` takes `name` and `age` and saves them to `self.name` and `self.age`\n- A method `greet` prints `f'My name is {self.name} and I am {self.age} years old'`\n\nThen create `Person('Sam', 18)`, assign it to `p`, and call `p.greet()`.\n\nThe output should be:\n```\nMy name is Sam and I am 18 years old\n```",
starter="# Define the class Person: __init__ takes name and age and saves them as instance attributes\n# Write a greet method that prints the introduction in the format asked for\n# Finally create p and call p.greet()\n\n",
solution="class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def greet(self):\n        print(f'My name is {self.name} and I am {self.age} years old')\n\np = Person('Sam', 18)\np.greet()",
hints=["__init__ has two underscores on each side", "Inside __init__, set instance attributes with self.xxx = ...", "Full code:\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def greet(self):\n        print(f'My name is {self.name} and I am {self.age} years old')\n\np = Person('Sam', 18)\np.greet()"])

EX['python8/03-inheritance'] = dict(
title="Inheritance: Student inherits from Person",
prompt="We've already defined this for you:\n```python\nclass Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'My name is {self.name}')\n```\n\nDefine a class `Student` that **inherits from `Person`**, and give it a method `study` that prints `f'{self.name} is studying'`.\n\nThen create `Student('Xiao Ming')`, assign it to `s`, and call `s.greet()` then `s.study()`.\n\nThe output should be:\n```\nMy name is Xiao Ming\nXiao Ming is studying\n```",
starter="class Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'My name is {self.name}')\n\n# Define a class Student that inherits from Person, with a study method\n# Create s, then call greet and study\n\n",
solution="class Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'My name is {self.name}')\n\nclass Student(Person):\n    def study(self):\n        print(f'{self.name} is studying')\n\ns = Student('Xiao Ming')\ns.greet()\ns.study()",
hints=["How to inherit: class Student(Person):", "It's fine that Student has no __init__ – it uses the parent class's one automatically", "Full code:\nclass Person:\n    def __init__(self, name):\n        self.name = name\n    def greet(self):\n        print(f'My name is {self.name}')\n\nclass Student(Person):\n    def study(self):\n        print(f'{self.name} is studying')\n\ns = Student('Xiao Ming')\ns.greet()\ns.study()"])

EX['python8/04-polymorphism'] = dict(
title="Polymorphism: overriding a parent's method",
prompt="We've already defined this for you:\n```python\nclass Animal:\n    def sound(self):\n        print('Some sounds')\n```\n\nDefine two classes `Dog` and `Cat` that inherit from `Animal`, and **override** the `sound` method in each:\n\n- `Dog.sound` prints `'Woof woof'`\n- `Cat.sound` prints `'Meow meow'`\n\nThen use a `for` loop to call `Dog().sound()` and `Cat().sound()` in turn.\n\nThe output should be:\n```\nWoof woof\nMeow meow\n```",
starter="class Animal:\n    def sound(self):\n        print('Some sounds')\n\n# Define Dog and Cat inheriting from Animal, each overriding sound\n# Use a for loop over the two instances and call sound on each\n\n",
solution="class Animal:\n    def sound(self):\n        print('Some sounds')\n\nclass Dog(Animal):\n    def sound(self):\n        print('Woof woof')\n\nclass Cat(Animal):\n    def sound(self):\n        print('Meow meow')\n\nfor a in [Dog(), Cat()]:\n    a.sound()",
hints=["Defining a method with the same name in a child class replaces the parent's one", "for a in [Dog(), Cat()]: goes through the two objects", "Full code:\nclass Animal:\n    def sound(self):\n        print('Some sounds')\n\nclass Dog(Animal):\n    def sound(self):\n        print('Woof woof')\n\nclass Cat(Animal):\n    def sound(self):\n        print('Meow meow')\n\nfor a in [Dog(), Cat()]:\n    a.sound()"])

EX['python9/01-import-math'] = dict(
title="Work out a circle's circumference with the math module",
prompt="Use `import` to bring in the `math` module, then use `math.pi` to:\n\n1. Work out the circumference of a circle with radius `r = 5`, using the formula `2 * math.pi * r`\n2. Round the result to **4 decimal places** (with the built-in function `round(..., 4)`) and assign it to the variable `c`\n3. `print(c)`\n\nThe output should be:\n```\n31.4159\n```",
starter="# Import the math module and use math.pi in the formula for a circle of radius 5\n# Round to 4 decimal places with round, assign to c and print it\n\n",
solution="import math\n\nr = 5\nc = round(2 * math.pi * r, 4)\nprint(c)",
hints=["Bring the math module in with import math", "math.pi is the number π", "Full code:\nimport math\n\nr = 5\nc = round(2 * math.pi * r, 4)\nprint(c)"])

EX['python9/02-from-import'] = dict(
title="from...import: take out sqrt directly",
prompt="Use the `from...import` syntax to import the `sqrt` function **directly** from the `math` module (don't use `import math`), then:\n\n1. Work out `sqrt(16)`\n2. Assign the result to the variable `result`\n3. `print(result)`\n\nThe output should be:\n```\n4.0\n```",
starter="# Use from...import to import sqrt straight from the math module\n# Work out the square root of 16, assign it to result and print it\n\n",
solution="from math import sqrt\n\nresult = sqrt(16)\nprint(result)",
hints=["The syntax is from module_name import name", "After from math import sqrt you can write sqrt(16) directly, with no prefix", "Full code:\nfrom math import sqrt\n\nresult = sqrt(16)\nprint(result)"])

EX['python9/03-datetime'] = dict(
title="Make a date with the datetime module",
prompt="Use `from...import` to import the `date` class from the `datetime` module, then:\n\n1. Create the date `1 January 2026` and assign it to the variable `d`: `d = date(2026, 1, 1)`\n2. `print` its three attributes `year`, `month` and `day`, one per line\n\nThe output should be:\n```\n2026\n1\n1\n```",
starter="# Import the date class from the datetime module\n# Make a date object for 1 January 2026 and assign it to d\n# Print its year, month and day attributes\n\n",
solution="from datetime import date\n\nd = date(2026, 1, 1)\nprint(d.year)\nprint(d.month)\nprint(d.day)",
hints=["from datetime import date", "date(year, month, day) makes a date object; then get attributes with .year / .month / .day", "Full code:\nfrom datetime import date\n\nd = date(2026, 1, 1)\nprint(d.year)\nprint(d.month)\nprint(d.day)"])

EX['python9/04-json'] = dict(
title="Turn a dictionary into JSON with the json module",
prompt="Use `import` to bring in the `json` module, then:\n\n1. Define the dictionary `data = {'name': 'Alice', 'age': 18}`\n2. Use `json.dumps(data)` to turn it into a JSON string and assign it to the variable `s`\n3. `print(s)`\n\nThe output should be:\n```\n{\"name\": \"Alice\", \"age\": 18}\n```\n\n> Tip: `json.dumps` puts spaces after `,` and `:` by default – don't type the string by hand.",
starter="# Import the json module and define the dictionary data as asked\n# Use json.dumps to turn it into a JSON string, assign it to s and print it\n\n",
solution="import json\n\ndata = {'name': 'Alice', 'age': 18}\ns = json.dumps(data)\nprint(s)",
hints=["import json", "json.dumps(dictionary) returns a JSON string", "Full code:\nimport json\n\ndata = {'name': 'Alice', 'age': 18}\ns = json.dumps(data)\nprint(s)"])

EX['python10/01-str'] = dict(
title="Make print friendly with __str__",
prompt="Define a class `Book`:\n\n- `__init__` takes `title` and saves it to `self.title`\n- `__str__` returns the string `f'Book: {self.title}'`\n\nThen create `Book('Python Basics')`, assign it to `b`, and `print(b)`.\n\nThe output should be:\n```\nBook: Python Basics\n```",
starter="# Define the Book class: save title in __init__, and make __str__ return a string like Book: title\n# Then create the book 'Python Basics', assign it to b, and print b\n\n",
solution="class Book:\n    def __init__(self, title):\n        self.title = title\n\n    def __str__(self):\n        return f'Book: {self.title}'\n\nb = Book('Python Basics')\nprint(b)",
hints=["__str__ must return a string – don't use print inside it", "f'Book: {self.title}' uses an f-string to put the title in", "Full code:\nclass Book:\n    def __init__(self, title):\n        self.title = title\n    def __str__(self):\n        return f'Book: {self.title}'\nb = Book('Python Basics')\nprint(b)"])

EX['python10/02-eq'] = dict(
title="Custom equality with __eq__",
prompt="Define a class `Money`:\n\n- `__init__` takes `amount` and saves it to `self.amount`\n- `__eq__` checks whether two `Money` objects have the same `amount`; if the other thing isn't `Money` (for example `Money(100) == 100`), it should return `False` instead of giving an error\n\nThen create:\n\n```python\na = Money(100)\nb = Money(100)\nc = Money(50)\n```\n\nand run:\n\n```python\nprint(a == b)\nprint(a == c)\n```\n\nThe output should be:\n```\nTrue\nFalse\n```",
starter="# Define the Money class: save amount in __init__\n# In __eq__, first use isinstance to check the other one is also Money, then compare the amounts\n# Create a, b and c, then print a == b and a == c\n\n",
solution="class Money:\n    def __init__(self, amount):\n        self.amount = amount\n\n    def __eq__(self, other):\n        return isinstance(other, Money) and self.amount == other.amount\n\na = Money(100)\nb = Money(100)\nc = Money(50)\nprint(a == b)\nprint(a == c)",
hints=["__eq__(self, other) takes a second parameter, other", "First check isinstance(other, Money), then compare amount – otherwise Money(100) == 100 would give an error", "Full code:\nclass Money:\n    def __init__(self, amount):\n        self.amount = amount\n    def __eq__(self, other):\n        return isinstance(other, Money) and self.amount == other.amount\na = Money(100)\nb = Money(100)\nc = Money(50)\nprint(a == b)\nprint(a == c)"])

EX['python10/03-len'] = dict(
title="Make len() work with __len__",
prompt="Define a class `Playlist`:\n\n- `__init__` takes `songs` (a list) and saves it to `self.songs`\n- `__len__` returns the length of `self.songs`\n\nThen create `p = Playlist(['Song 1', 'Song 2', 'Song 3'])` and call `print(len(p))`.\n\nThe output should be:\n```\n3\n```",
starter="# Define the Playlist class: save the songs list in __init__\n# __len__ returns the number of songs\n# After creating p, print len(p)\n\n",
solution="class Playlist:\n    def __init__(self, songs):\n        self.songs = songs\n\n    def __len__(self):\n        return len(self.songs)\n\np = Playlist(['Song 1', 'Song 2', 'Song 3'])\nprint(len(p))",
hints=["__len__ must return a whole number that isn't negative", "Just return the length of the list inside: return len(self.songs)", "Full code:\nclass Playlist:\n    def __init__(self, songs):\n        self.songs = songs\n    def __len__(self):\n        return len(self.songs)\np = Playlist(['Song 1', 'Song 2', 'Song 3'])\nprint(len(p))"])

EX['python10/05-getitem'] = dict(
title="Let an object use [index] with __getitem__",
prompt="Define a class `Stack`:\n\n- `__init__` takes `items` (a list) and saves it to `self.items`\n- `__getitem__(self, i)` returns `self.items[i]`\n\nThen run:\n\n```python\ns = Stack(['a', 'b', 'c'])\nprint(s[0])\nprint(s[-1])\n```\n\nThe output should be:\n```\na\nc\n```",
starter="# Define the Stack class: save the items list in __init__\n# __getitem__ passes the index on to the list inside\n# After creating s, print s[0] and s[-1]\n\n",
solution="class Stack:\n    def __init__(self, items):\n        self.items = items\n\n    def __getitem__(self, i):\n        return self.items[i]\n\ns = Stack(['a', 'b', 'c'])\nprint(s[0])\nprint(s[-1])",
hints=["In __getitem__(self, i), i is the value inside the square brackets", "Just pass it on to the list inside: return self.items[i]", "Full code:\nclass Stack:\n    def __init__(self, items):\n        self.items = items\n    def __getitem__(self, i):\n        return self.items[i]\ns = Stack(['a', 'b', 'c'])\nprint(s[0])\nprint(s[-1])"])

EX['python10/04-add'] = dict(
title="Let objects use + with __add__",
prompt="Define a 2D vector class `Vec2`:\n\n- `__init__` takes `x` and `y` and saves them to `self.x` / `self.y`\n- `__add__(self, other)` returns a new `Vec2(self.x + other.x, self.y + other.y)`\n- `__repr__` returns the string `f'Vec2({self.x}, {self.y})'`\n\nThen run:\n\n```python\nv1 = Vec2(1, 2)\nv2 = Vec2(3, 4)\nv3 = v1 + v2\nprint(v3)\n```\n\nThe output should be:\n```\nVec2(4, 6)\n```",
starter="# Define the Vec2 class: save x and y in __init__\n# __add__ returns a new Vec2 with the coordinates added; __repr__ returns a string like Vec2(x, y)\n# Create v1 and v2, add them to get v3, and print it\n\n",
solution="class Vec2:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __add__(self, other):\n        return Vec2(self.x + other.x, self.y + other.y)\n\n    def __repr__(self):\n        return f'Vec2({self.x}, {self.y})'\n\nv1 = Vec2(1, 2)\nv2 = Vec2(3, 4)\nv3 = v1 + v2\nprint(v3)",
hints=["__add__ usually returns a new object – don't change self", "Add x and y separately, then wrap them in a new Vec2", "Full code:\nclass Vec2:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vec2(self.x + other.x, self.y + other.y)\n    def __repr__(self):\n        return f'Vec2({self.x}, {self.y})'\nv1 = Vec2(1, 2)\nv2 = Vec2(3, 4)\nv3 = v1 + v2\nprint(v3)"])

EX['python11/01-define-color'] = dict(
title="Define a Color enum class",
prompt="Use `from ... import` to import `Enum` from the `enum` module, then:\n\n1. Define a class `Color` that inherits from `Enum`, with three members:\n   - `RED = 1`\n   - `GREEN = 2`\n   - `BLUE = 3`\n2. `print(Color.RED)`\n\nThe output should be:\n```\nColor.RED\n```\n\n> Tip: printing an Enum member directly shows it as `ClassName.MemberName` by default.",
starter="# Import Enum from the enum module\n# Define the Color enum class with three members: RED, GREEN and BLUE\n# Print Color.RED\n\n",
solution="from enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nprint(Color.RED)",
hints=["from enum import Enum", "class Color(Enum): then write members like RED = 1 inside the class", "Full code:\nfrom enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nprint(Color.RED)"])

EX['python11/02-name-value'] = dict(
title="Get .name and .value",
prompt="Carry on with the `Color` enum from the last exercise (with `RED=1` / `GREEN=2` / `BLUE=3`). This time:\n\n1. `print(Color.GREEN.name)` – print the member's name\n2. `print(Color.GREEN.value)` – print the member's value\n\nThe output should be:\n```\nGREEN\n2\n```",
starter="# Define the Color enum with three members: RED, GREEN and BLUE\n# Print the name and the value of Color.GREEN\n\n",
solution="from enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nprint(Color.GREEN.name)\nprint(Color.GREEN.value)",
hints=[".name is the member's name as a string", ".value is the value you gave it when defining it", "Full code:\nfrom enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nprint(Color.GREEN.name)\nprint(Color.GREEN.value)"])

EX['python11/03-iterate'] = dict(
title="Go through all the members of an Enum",
prompt="Define the same `Color` enum (`RED=1` / `GREEN=2` / `BLUE=3`), then use a `for` loop to go through it and print each member's `.name` **in the order they were defined**.\n\nThe output should be:\n```\nRED\nGREEN\nBLUE\n```\n\n> Tip: `for c in Color:` gives you each member, then `c.name` gets its name.",
starter="# Define the same Color enum\n# Use a for loop over Color and print each member's name in the order they were defined\n\n",
solution="from enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nfor c in Color:\n    print(c.name)",
hints=["An Enum class can be looped over itself: for member in Color", "Use c.name to get the member's name as a string", "Full code:\nfrom enum import Enum\n\nclass Color(Enum):\n    RED = 1\n    GREEN = 2\n    BLUE = 3\n\nfor c in Color:\n    print(c.name)"])

EX['python11/04-auto'] = dict(
title="Assign values automatically with auto()",
prompt="Use `from ... import` to import both `Enum` and `auto` from the `enum` module, then:\n\n1. Define a class `Weekday` that inherits from `Enum`, with three members all given values by `auto()`:\n   - `MON = auto()`\n   - `TUE = auto()`\n   - `WED = auto()`\n2. `print(Weekday.MON.value)`\n3. `print(Weekday.WED.value)`\n\nThe output should be:\n```\n1\n3\n```\n\n> Tip: `auto()` starts at 1 by default and counts up in the order members are defined.",
starter="# Import both Enum and auto from the enum module\n# Define the Weekday enum, with MON, TUE and WED all given values by auto()\n# Print the value of MON and of WED\n\n",
solution="from enum import Enum, auto\n\nclass Weekday(Enum):\n    MON = auto()\n    TUE = auto()\n    WED = auto()\n\nprint(Weekday.MON.value)\nprint(Weekday.WED.value)",
hints=["from enum import Enum, auto imports two names at once", "Inside the class, just write MON = auto()", "Full code:\nfrom enum import Enum, auto\n\nclass Weekday(Enum):\n    MON = auto()\n    TUE = auto()\n    WED = auto()\n\nprint(Weekday.MON.value)\nprint(Weekday.WED.value)"])

EX['python12/01-detect-meta'] = dict(
title="What is the class of a class?",
prompt="Define the simplest possible class, `Foo` (just write `pass` inside).\n\nThen use `type()` to check the type of `Foo`, and use `is` to check whether it is `type`. Print two lines in this format:\n\n```\n<class 'type'>\nTrue\n```\n\nTip: the first line is `print(type(Foo))`, the second is `print(type(Foo) is type)`.",
starter="# Define the simplest class Foo (write pass inside)\n# Use type() to print the type of Foo\n# Then print the result of type(Foo) is type\n\n",
solution="class Foo:\n    pass\n\nprint(type(Foo))\nprint(type(Foo) is type)",
hints=["Define the simplest class with class Foo: pass", "type(Foo) returns <class 'type'>", "Full code:\nclass Foo:\n    pass\n\nprint(type(Foo))\nprint(type(Foo) is type)"])

EX['python12/02-build-greeter'] = dict(
title="Make a class on the fly with three-argument type()",
prompt="**Without using the `class` keyword**, use the three-argument `type()` syntax to create a class `Greeter`:\n\n- Parent classes: `(object,)`\n- One method, `greet(self)`, which prints `'hi'` – first define an ordinary function `greet(self)` with `def`, then put it in the attribute dictionary `{'greet': greet}`\n\nAfter creating it, make an instance and call `g.greet()`, then `print(type(Greeter))` to show it's an instance of `type`.\n\nThe output should be:\n```\nhi\n<class 'type'>\n```",
starter="# First use def to define an ordinary function greet(self) that prints 'hi'\n# Use three-argument type() to create Greeter, putting greet in the attribute dictionary\n# Create an instance and call greet, then print type(Greeter)\n\n",
solution="def greet(self):\n    print('hi')\n\nGreeter = type('Greeter', (object,), {'greet': greet})\n\ng = Greeter()\ng.greet()\nprint(type(Greeter))",
hints=["Three-argument type(): type(class name string, tuple of parent classes, attribute dictionary)", "First def an ordinary function greet(self), then put it in the dictionary {'greet': greet}", "Full code:\ndef greet(self):\n    print('hi')\n\nGreeter = type('Greeter', (object,), {'greet': greet})\ng = Greeter()\ng.greet()\nprint(type(Greeter))"])

EX['python12/03-custom-meta'] = dict(
title="A custom metaclass that adds an attribute automatically",
prompt="Define a metaclass `AnimalMeta` that **inherits from `type`**:\n\n- Override `__new__(mcs, name, bases, attrs)`\n- Put `species = 'animal'` into `attrs`\n- Return the class with `super().__new__(mcs, name, bases, attrs)`\n\nThen define an empty class `Dog(metaclass=AnimalMeta)` with `pass` inside.\n\nFinally print `Dog.species`.\n\nThe output should be:\n```\nanimal\n```",
starter="# Define a metaclass AnimalMeta that inherits from type and overrides __new__\n# Put species into attrs, then return the class with super().__new__\n# Define an empty class Dog with the metaclass set, then print Dog.species\n\n",
solution="class AnimalMeta(type):\n    def __new__(mcs, name, bases, attrs):\n        attrs['species'] = 'animal'\n        return super().__new__(mcs, name, bases, attrs)\n\nclass Dog(metaclass=AnimalMeta):\n    pass\n\nprint(Dog.species)",
hints=["A metaclass must inherit from type: class AnimalMeta(type):", "In __new__, add a key-value pair to the attrs dictionary, then return super().__new__", "To use a metaclass, write class Dog(metaclass=AnimalMeta):"])

EX['python14/01-findall-digits'] = dict(
title="Grab all the numbers with re.findall",
prompt="The string `'abc123def456ghi789'` has some **runs of digits** mixed in.\n\nUse `re.findall` to grab every run of digits, assign the result to the variable `nums`, then `print(nums)`.\n\nThe output should be:\n```\n['123', '456', '789']\n```\n\nTip: a run of digits can be matched with `\\d+`.",
starter="import re\n\ns = 'abc123def456ghi789'\n# nums = re.findall(...)\n# print(nums)\n",
solution="import re\n\ns = 'abc123def456ghi789'\nnums = re.findall(r'\\d+', s)\nprint(nums)",
hints=["Remember to import re", "Write the regex as a raw string r'...' so backslashes don't need escaping", "Full code:\nimport re\ns = 'abc123def456ghi789'\nnums = re.findall(r'\\d+', s)\nprint(nums)"])
