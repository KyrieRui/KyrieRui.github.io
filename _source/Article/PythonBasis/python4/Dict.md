# 1. Dictionary (dict) #

## 1. What is a dict? ##

In the last chapter, we learned to use lists and tuples for ordered collections.

When we talked about lists, we used a list to store people's names:

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']
```

Now, what if we want to contact these friends easily, and we need to add their phone numbers too?

With a list, we could do this:

```python
name = [['One Drop', '131456780001'], ['Two Drops', '131456780002'], ['Three Drops', '131456780003'], ['Four Drops', '131456780004'], ['Five Drops', '131456780005']]
```

But this isn't very handy. We saved the phone numbers so we can quickly contact someone when we need to.

If we store them in a list, the longer the list gets, the longer it takes to find someone.

This is when we can use a **dict** (dictionary). Python has dicts built in. If you know Java, a dict is like a `map` in Java. It stores data as **key-value** pairs, and it can find things extremely fast.

```python
name = {'One Drop': '131456780001', 'Two Drops': '131456780002', 'Three Drops': '131456780003', 'Four Drops': '131456780004', 'Five Drops': '131456780005'}
```



## 2. Creating a dict ##

A dictionary is another kind of changeable container, and it can store any type of object.

Each **key: value** pair is split by a colon (`:`). Pairs are separated by commas (`,`). The whole dictionary goes inside **curly braces** (`{}`), like this:

<!-- skip-ci -->
```python
dict = {key1 : value1, key2 : value2 }
```

Note: keys must be **unique**, but values don't have to be. Values can be any data type, but keys must be **immutable** (unchangeable).

> To be more exact, dictionary keys must be **hashable**. A tuple that contains a list is itself immutable, but it still can't be a dictionary key. So you can't decide only by "changeable or unchangeable".

Examples of creating dicts:

```python
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'Two Drops':'333333'}
dict2={'abc':1234,1234:'abc'}
```



## 3. Getting Values from a dict ##

Now we know how to create a dict. Back to our first question: why does a dictionary help us find someone's phone number so quickly?



```python
name = {'One Drop': '131456780001', 'Two Drops': '131456780002', 'Three Drops': '131456780003', 'Four Drops': '131456780004', 'Five Drops': '131456780005'}

print(name['Two Drops'])
```


Output:

```
131456780002
```

As you can see, if you know someone's name (the **key**), you can very quickly find their phone number (the **value**).

One thing to note: if the key is **not** in the dictionary, you will get an error.



## 4. Changing a dict ##

To add new content to a dictionary, add a new key/value pair. You can also change or delete existing pairs.

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'Two Drops':'333333'}
print(dict1)
# Add a new key-value pair
dict1['jack']='444444'
print(dict1)
# Change a key-value pair
dict1['liangdianshui']='555555'
print(dict1)
```

Output:

```
{'liangdianshui': '111111', 'twowater': '222222', 'Two Drops': '333333'}
{'liangdianshui': '111111', 'twowater': '222222', 'Two Drops': '333333', 'jack': '444444'}
{'liangdianshui': '555555', 'twowater': '222222', 'Two Drops': '333333', 'jack': '444444'}
```

## 5. Deleting from a dict ##

You can use `del` to delete one item from a dict, or to delete the whole dict.

You can call the `clear()` method to remove all items from a dict.

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'Two Drops':'333333'}
print(dict1)
# Delete an item using its key
del dict1['twowater']
print(dict1)
# Remove all items from the dict
dict1.clear()
print(dict1)
# Delete the dict
del dict1
```

Output:

```
{'liangdianshui': '111111', 'twowater': '222222', 'Two Drops': '333333'}
{'liangdianshui': '111111', 'Two Drops': '333333'}
{}
```

## 6. Things to Watch Out For with dicts ##

(1) A dict can't have the same key twice. If you give the same key a value twice when creating a dict, the **last** value wins.

For example:

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,'twowater':'222222' ,'Two Drops':'333333','twowater':'444444'}
print(dict1)
print(dict1['twowater'])
```

Output:

```
{'liangdianshui': '111111', 'twowater': '444444', 'Two Drops': '333333'}
444444
```


(2) dict keys must be immutable. Keys can be numbers, strings or tuples, but **not** lists.

For example:

```python
#-*-coding:utf-8-*-
dict1={'liangdianshui':'111111' ,123:'222222' ,(123,'tom'):'333333','twowater':'444444'}
print(dict1)
```

Output:

```
{'liangdianshui': '111111', 123: '222222', (123, 'tom'): '333333', 'twowater': '444444'}
```

(3) The order things are stored inside a dict has nothing to do with the order you added the keys. *(This changed in Python 3.7 – see section 8 below.)*

Compared with a list, a dict:

* Finds and adds items extremely fast, and doesn't get slower as you add more keys

* Uses a lot of memory, and wastes quite a bit

A list is the opposite:

* Finding and adding items takes longer as the list grows

* Uses little space and wastes very little memory


## 7. dict Functions and Methods ##

|Method / Function|What it does|
|---------|--------|
|len(dict)|Counts the items in the dict|
|str(dict)|Gives a printable string version of the dict|
|type(variable)|Returns the variable's type. If it's a dict, it returns the dict type|
|dict.clear()|Removes all items from the dict|
|dict.copy()|Returns a shallow copy of the dict|
|dict.values()|Returns all the values in the dict as a list|
|popitem()|Removes and returns a key-value pair from the dict|
|dict.items()|Returns a list of (key, value) tuples you can loop through|



## 8. New in Python 3.9+: the dict merge operator ##

Hey everyone! We have covered adding, deleting, changing and finding things in a dict. Now here's a nice extra that came in Python 3.9: the dict **merge operators** `|` and `|=`.

Why talk about this specially?

Let's look at a task first. Say Brother Shui has two contact dictionaries, and needs to merge them into one:

```python
old_contacts = {'One Drop': '131456780001', 'Two Drops': '131456780002'}
new_contacts = {'Three Drops': '131456780003', 'Two Drops': '131456780099'}
```

Look carefully: the key `'Two Drops'` is in both. We want the **new** one to win.

Before Python 3.9, people usually wrote it like this:

```python
old_contacts = {'One Drop': '131456780001', 'Two Drops': '131456780002'}
new_contacts = {'Three Drops': '131456780003', 'Two Drops': '131456780099'}

merged = {**old_contacts, **new_contacts}
print(merged)
```

Output:

```
{'One Drop': '131456780001', 'Two Drops': '131456780099', 'Three Drops': '131456780003'}
```

This `**` unpacking works fine, but it's not very easy to read. From Python 3.9, you can just use `|`:

```python
old_contacts = {'One Drop': '131456780001', 'Two Drops': '131456780002'}
new_contacts = {'Three Drops': '131456780003', 'Two Drops': '131456780099'}

merged = old_contacts | new_contacts
print(merged)
```

Output:

```
{'One Drop': '131456780001', 'Two Drops': '131456780099', 'Three Drops': '131456780003'}
```

Notice anything? It looks exactly like the set union `|`. That's on purpose – it means "join the two dicts together".

If you don't want a new dictionary, and instead want to merge the new content **into the original** dictionary, use `|=`:

```python
old_contacts = {'One Drop': '131456780001', 'Two Drops': '131456780002'}
new_contacts = {'Three Drops': '131456780003', 'Two Drops': '131456780099'}

old_contacts |= new_contacts
print(old_contacts)
```

Output:

```
{'One Drop': '131456780001', 'Two Drops': '131456780099', 'Three Drops': '131456780003'}
```

Note: with `|`, the **right side overwrites the left side**, the same as `{**a, **b}`. Keep this in mind so you don't mix up which side is new and which is old.

Finally, one more point I didn't stress before: since Python 3.7, dicts **keep insertion order**. This means the earlier rule, "the order inside a dict has nothing to do with the order you added keys", is no longer true in modern Python. Look at this example:

```python
d = {}
d['c'] = 3
d['a'] = 1
d['b'] = 2

for key in d:
    print(key)
```

Output:

```
c
a
b
```

See? The loop goes in the same order the keys were added. This is guaranteed by the language in Python 3.7+ (in 3.6 it already worked this way in CPython, but it wasn't an official rule). So in most cases now, you don't need `import collections.OrderedDict` any more – a normal `dict` is enough.







## Studying the same subject again: how to update the record

We've recorded 15 minutes of Python and 10 minutes of reading. If we study Python for another 5 minutes, do we add the same key again, or change the old value?

```python
totals = {'Python': 15, 'Reading': 10}
totals['Python'] = totals['Python'] + 5
print(totals)
print(totals.get('Maths', 0))
```

Output:

```text
{'Python': 20, 'Reading': 10}
0
```

In one dictionary, each key can only have one value. Before assigning, we take out the old `15`, add `5`, and store it back. So the Python total becomes `20`. `get('Maths', 0)` means: if this subject isn't there, give back the default value `0` that we provided. It does **not** add a new key.

Try it yourself: change the right side to just `5`. What's different? Then add a new subject to the dictionary and check whether the old records are still there. After we learn loops, we'll handle lots of study records.
