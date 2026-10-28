# 2. Early return

Look at this 'check the login' code:

```python no-run
def login(user, password):
    if user is not None:
        if user.is_active:
            if user.check_password(password):
                if not user.is_locked:
                    return 'Logged in'
                else:
                    return 'Account locked'
            else:
                return 'Wrong password'
        else:
            return 'Account not activated'
    else:
        return 'User does not exist'
```

Four levels of nesting – by the time you reach the third `if`, you've forgotten what the first condition was.

## Early return: send the unusual cases away first

"**Handle the edge cases first, so the main path can sit at the outer level**" – that's the core idea of early return.

```python no-run
def login(user, password):
    if user is None:
        return 'User does not exist'
    if not user.is_active:
        return 'Account not activated'
    if not user.check_password(password):
        return 'Wrong password'
    if user.is_locked:
        return 'Account locked'
    return 'Logged in'
```

Can you see what changed?

- No `else`
- No nesting
- Each failure condition **takes just one line**
- The last line is the "success path" – easy to find at a glance

## The general pattern

Whenever you see this shape:

```python no-run
if condition_is_true:
    # a big chunk of the main path
    ...
else:
    return error
```

you can rewrite it as:

```python no-run
if not condition_is_true:
    return error
# a big chunk of the main path (not indented)
...
```

The main path moves back from 1 level of indentation to 0. When several conditions stack up, the difference is huge.

## When not to use early return

Not every `if` should be an early return. If the two branches are **equally important** – like "return X for odd, Y for even" – just write a normal `if/else`; there's no need to force it into an early return.

```python no-run
def parity(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'
```

This is actually clearer. Early return is for **flattening error handling**, not for getting rid of every `else`.
