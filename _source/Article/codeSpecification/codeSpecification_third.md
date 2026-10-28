# 3. Naming Rules

##  1. Modules
* Module names should be lowercase, starting with a lowercase letter. Try not to use underscores (unless the name has a few words).

<!-- skip-ci -->
```python
# Good module names
import decoder
import html_parser

# Not recommended
import Decoder
```

## 2. Class Names
* Class names use **CamelCase**: start each word with a capital letter. Private classes can start with one underscore.

```Python
class Farm():
    pass

class AnimalFarm(Farm):
    pass

class _PrivateFarm(Farm):
    pass
```

* Put related classes and top-level functions in the same module. Unlike Java, you don't need one module per class.

## 3. Functions

* Function names are always lowercase. If there are several words, join them with underscores.

```python
def run():
    pass

def run_with_env():
    pass
```

* Put one underscore `_` in front of private function names.

```python
class Person():

    def _private_func():
        pass
```

## 4. Variable Names

* Variable names should be lowercase. If there are several words, join them with underscores.

```python
if __name__ == '__main__':
    count = 0
    school_name = ''
```

* Constants are ALL CAPITALS. If there are several words, join them with underscores.

```python
MAX_CLIENT = 100
MAX_CONNECTION = 1000
CONNECTION_TIMEOUT = 600
```

## 5. Constants ##

* Constants use capital letters, with words separated by underscores.

```python
MAX_OVERFLOW = 100

class FooBar:

    def foo_bar(self, print_):
        print(print_)

```
