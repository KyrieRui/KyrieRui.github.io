# 1. List #

## 1. What is a List?

A **List** is a data type built into Python. It is an **ordered collection**. You can add or remove items at any time.

So why do we need lists?

Let's use an example.

A team is going on a trip, and everyone needs to sign up first. With what we have learned so far, we would store each name in its own string variable:

```python
name1 = 'One Drop'
name2 = 'Two Drops'
name3 = 'Three Drops'
name4 = 'Four Drops'
name5 = 'Five Drops'
```

But this is too much work, and it doesn't look nice.

In programming, you should learn to be "lazy" and avoid **repetitive work**. If there were a hundred members, even copying and pasting would drive you crazy.

This is when you can use a list:

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']
```

Just like that, one line of code can hold lots and lots of names.


## 2. How to Create a List ##

From the example above, we can see what a list looks like:

![The parts of a list](../../images/diagrams/list-literal.svg)

A list is data inside **square brackets** `[]`. Each piece of data inside is called an **element** (or item). Elements are separated by commas.

Also, the elements in a list don't have to be the same data type.

For example:

```python
list1=['Two Drops','twowter','liangdianshui',123]
```

Here we have strings and an integer.

Let's print it and see what we get:

```python
list1 = ['Two Drops', 'twowter', 'liangdianshui', 123]

print(list1)
```

Result:

```
['Two Drops', 'twowter', 'liangdianshui', 123]
```


## 3. How to Get Values from a List ##

Going back to our first example: sometimes we don't want to print everyone's name. Sometimes we want to know: who signed up 3rd? Who were the first two?

How do we get them out of the list?

In other words, how do we **access** the values in a list?

We can use the list's **index** (position number) to get a value. We can also use square brackets to take a **slice** (a part) of the list.

For example:

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']

# Get a value using its index
print(name[2])
# Take a slice of the list using square brackets
print(name[0:2])
```

Output:

```
Three Drops
['One Drop', 'Two Drops']
```

So, to find out who signed up third in the `name` list, we just use `name[2]`.

You might ask: why 2 and not 3?

Because in the programming world, counting starts from **0**, not from 1 like in everyday life.

So to find the third person,

we use `name[2]`.

In the example, we also printed `name[0:2]`.

Looking at the output, it only printed the first and second elements.

You might be confused here.

Why didn't it print the first three? Didn't we just say 2 means the 3rd one?

That's because a slice **includes the start but excludes the end**.

So `name[0:2]` means: start at position 0 and go up to position 2, but **don't include** position 2.

As always, the best way to understand is to try things and play with code.

Try all of these:

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']

print(name[0:2])
print(name[:2])
print(name[:])
print(name[1:2])
print(name[0:3])
```

Look at the output:

```
['One Drop', 'Two Drops']
['One Drop', 'Two Drops']
['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']
['Two Drops']
['One Drop', 'Two Drops', 'Three Drops']
```

With these results and what we just learned, these uses are easy to understand.




## 4. How to Update a List ##

Back to our example again. We stored the names of everyone who signed up. Later, new people might join, or we might find we spelled a name wrong and want to fix it.

What do we do then?

We can use an index to change (update) an item in the list. We can also use the `append()` method to add a new item.

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']


# Use an index to change or update an item
name[1]='2 Drops'
print(name)

# Use the append() method to add an item
name.append('Six Drops')
print(name)
```

Output:

```
['One Drop', '2 Drops', 'Three Drops', 'Four Drops', 'Five Drops']
['One Drop', '2 Drops', 'Three Drops', 'Four Drops', 'Five Drops', 'Six Drops']
```





## 5. How to Delete Items from a List ##

Of course, someone might drop out halfway.

Then we need to remove their name from the list.

We use the `del` statement to delete an item from a list:

```python
name = ['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']

print(name)

# Use the del statement to delete an item
del name[3]
print(name)
```

Output:

```
['One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops']
['One Drop', 'Two Drops', 'Three Drops', 'Five Drops']
```

Look at the output: `Four Drops` is no longer in the list. So it was deleted successfully.






## 6. List Operators ##

Lists work with `+` and `*` just like strings do. `+` joins lists together, and `*` repeats a list.

|Python expression|Result|What it does|
|-----------|-----|-----|
|len([1, 2, 3])|3|Counts the elements|
|[1, 2, 3] + [4, 5, 6]|	[1, 2, 3, 4, 5, 6]|	Joins|
|['Hi!'] * 4|['Hi!', 'Hi!', 'Hi!', 'Hi!']|Repeats|
|3 in [1, 2, 3]|True|Checks if an element is in the list|
|for x in [1, 2, 3]: print x,|1 2 3|Loops through it|


## 7. List Functions & Methods ##

|Function / Method|What it does|
|----|----|
|len(list)|Number of elements in the list|
|max(list)|Returns the biggest element|
|min(list)|Returns the smallest element|
|list(seq)|Turns a tuple into a list|
|list.append(obj)|Adds a new object to the end of the list|
|list.count(obj)|Counts how many times an element appears|
|list.extend(seq)|Adds all the values from another sequence to the end (extends the list with a new list)|
|list.index(obj)|Finds the index of the first matching value|
|list.insert(index, obj)|Inserts an object into the list|
|list.pop(obj=list[-1])|Removes one element (the last one by default) and returns its value|
|list.remove(obj)|Removes one element (you give the element itself), and returns nothing|
|list.reverse()|Reverses the order of the elements|
|list.sort([func])|Sorts the list|


## 8. Example ##


Finally, let's use an example to get to know List operations.

Example:

```python
#-*-coding:utf-8-*-
#-----------------------Using a list----------------------------------

# 1. A product needs to list its users. We can use a list for this
user=['liangdianshui','twowater','Two Drops']
print('1. Product users')
print(user)

# 2. To count how many users there are, len() gives the number of elements in a list
len(user)
print('\n2. Count the users')
print(len(user))

# 3. What if we need to know each user? Use an index to get the element at each position. Indexes start from 0
print('\n3. Look at each user')
print(user[0]+','+user[1]+','+user[2])

# 4. Suddenly a new user arrives. We add them to the end of the list
user.append('Yinyin')
print('\n4. Add a new user at the end')
print(user)

# 5. Another user joins, but this one is a VIP student and must go first. Use insert to put them at a chosen position
# Note: when inserting, be careful not to go out of range
user.insert(0,'VIP user')
print('\n5. Add a user at a chosen position')
print(user)

# 6. Oops, we made a mistake: "Yinyin" IS the 'VIP user', so we need to delete "Yinyin". pop() deletes the last element
user.pop()
print('\n6. Delete the last user')
print(user)

# 7. After a while, the user "liangdianshui" stopped using the product and deleted their account
# So we need to delete the element at a certain position, using pop(i), where i is the index
user.pop(1)
print('\n7. Delete the list element at a chosen position')
print(user)

# 8. The user "Two Drops" wants to change their nickname
user[2]='Three Drops'
print('\n8. Replace an element with a different one')
print(user)

# 9. Saving only nicknames isn't great. It's better to save the account number too
# The account number is an integer, not a string like the nickname, but list elements can be different types
# A list element can even be another list
newUser=[['VIP user',11111],['twowater',22222],['Three Drops',33333]]
print('\n9. A list with different types of elements')
print(newUser)

```

Output:

```
1. Product users
['liangdianshui', 'twowater', 'Two Drops']

2. Count the users
3

3. Look at each user
liangdianshui,twowater,Two Drops

4. Add a new user at the end
['liangdianshui', 'twowater', 'Two Drops', 'Yinyin']

5. Add a user at a chosen position
['VIP user', 'liangdianshui', 'twowater', 'Two Drops', 'Yinyin']

6. Delete the last user
['VIP user', 'liangdianshui', 'twowater', 'Two Drops']

7. Delete the list element at a chosen position
['VIP user', 'twowater', 'Two Drops']

8. Replace an element with a different one
['VIP user', 'twowater', 'Three Drops']

9. A list with different types of elements
[['VIP user', 11111], ['twowater', 22222], ['Three Drops', 33333]]
```





## You copied the list – so why do both change?

Let's use the sign-up list again. We want to keep a copy of the original list, then add one more person to the current list. Look carefully: do the two assignments below do the same thing?

```python
names = ['One Drop', 'Two Drops']
another_name = names
saved_names = names.copy()
another_name.append('Three Drops')
print(names)
print(saved_names)
```

Output:

```text
['One Drop', 'Two Drops', 'Three Drops']
['One Drop', 'Two Drops']
```

`another_name = names` just gives the **same** list a second name. `names.copy()` makes a **new** list. Changing the original list's items won't change this new list.

Now try it yourself: change `names` to an empty list, append a name, and look at both results. Then think: if the items in the list were lists themselves, would `copy()` make a new copy of each inner list too? **No.** A normal list copy is a **shallow copy**. When you have objects inside objects, you need to check whether the inner objects are shared.

Lists are good for storing a group of things that can change and have an order. In a tuple, you can't reassign any position. But if a tuple holds a list, the contents of that list **can** still change. Keep "the outer positions can't change" and "the objects inside can't change" separate in your head, and similar-looking code won't trick you.
