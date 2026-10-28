# 2. tuple #

## 1. What is a tuple? ##

In the last section we talked about an ordered list, the List. Now let's look at another kind of ordered list: the **tuple**.

A tuple is very similar to a List, but once a tuple is created, it **can't be changed**.
We say a tuple is **immutable**. So what does "immutable" mean?

It means that once you create a tuple, it can't change. It has no methods like `append()` or `insert()`. You can still get the value at an index, but you can't assign a new value to it.

So why do we need tuples?

Because tuples can't change, your code is **safer**.

So if you can use a tuple instead of a list, it's a good idea to use a tuple.



## 2. How to Create a tuple ##

Creating a tuple is easy. Just put the elements inside round brackets, separated by commas.

```python
tuple1=('Two Drops','twowter','liangdianshui',123,456)
tuple2='Two Drops','twowter','liangdianshui',123,456
```

Create an empty tuple:

```python
tuple3=()
```

If a tuple has only **one** element, you must add a comma after it:

```python
tuple4=(123,)
```

Without the comma, you don't get a tuple – you just get the number ```123```.


This is because round brackets `()` can mean a tuple, but they can also mean brackets in a maths formula. That's confusing.

So with only one element and no comma, the computer can't tell if you want to do maths with an integer or float, or if you mean a tuple.

So Python's rule is: in this case, treat them as maths brackets. The result is of course ```123```. If you want a tuple, you need to add a comma.

Look at the output of tuple4 and tuple5 below:

```python
#-*-coding:utf-8-*-
tuple1 = ('Two Drops', 'twowter', 'liangdianshui', 123, 456)
tuple2 = 'Two Drops', 'twowter', 'liangdianshui', 123, 456
tuple3 = ()
tuple4 = (123,)
tuple5 = (123)
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
```

Output:

```
('Two Drops', 'twowter', 'liangdianshui', 123, 456)
('Two Drops', 'twowter', 'liangdianshui', 123, 456)
()
(123,)
123
```







## 3. How to Get Values from a tuple ##

Tuple indexes also start from 0. You can use an index to get a value from a tuple.

```python
#-*-coding:utf-8-*-

tuple1=('Two Drops','twowter','liangdianshui',123,456)
tuple2='Two Drops','twowter','liangdianshui',123,456

print(tuple1[1])
print(tuple2[0])
```

Output:

```
twowter
Two Drops
```





## 4. "Changing" a tuple ##

When you see this heading, you might be confused. Didn't we just spend a long time saying tuples can't change?

So why are we changing a tuple now?

Because although you can't change the element values in a tuple, you **can** join tuples together. You can also change a list that is inside a tuple, which affects how the tuple looks.

Look at this example:

```python
#-*-coding:utf-8-*-
list1=[123,456]
tuple1=('Two Drops','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)
```

Output:
```
('Two Drops', 'twowater', 'liangdianshui', [123, 456])
('Two Drops', 'twowater', 'liangdianshui', [789, 100])
```


We can see the tuple printed differently the two times. Let's see how tuple1 is stored.

![A mutable object inside a tuple](../../images/diagrams/tuple-list.svg)

tuple1 has four elements. The last element is a List, and the List has two elements.

When we change the List's two elements from `123` and `456` to `789` and `100`, the printed tuple1 looks like it really changed.

But actually, what changed was **not** the tuple's elements – it was the list's elements.

The tuple still points to the same list it pointed to at the start. So when we say a tuple "doesn't change", we mean that **what each element points to never changes**. The fourth element of tuple1 still points to the original list. We only changed the elements **inside** that list.



## 5. Deleting a tuple ##

You can't delete single elements from a tuple. But you can use the `del` statement to delete the whole tuple.

```python
#-*-coding:utf-8-*-

tuple1=('Two Drops','twowter','liangdianshui',[123,456])
print(tuple1)
del tuple1
```

## 6. tuple Operators ##

Just like strings, you can use `+` and `*` with tuples. This means you can join and repeat them. The result is a new tuple.

|Python expression|Result|What it does|
|-----------|-----|-----|
|len((1, 2, 3))|3|Counts the elements|
|(1, 2, 3) + (4, 5, 6)|(1, 2, 3, 4, 5, 6)|Joins|
|('Hi!',) * 4|('Hi!', 'Hi!', 'Hi!', 'Hi!')|Repeats|
|3 in (1, 2, 3)|True|Checks if an element is there|
|for x in (1, 2, 3):  print(x)|1 2 3|Loops through it|

## 7. Built-in tuple Functions ##

|Function|What it does|
|----|----|
|len(tuple)|Counts the elements in a tuple|
|max(tuple)|Returns the biggest element|
|min(tuple)|Returns the smallest element|
|tuple(seq)|Turns a list into a tuple|


## 8. Example ##

Finally, just like with lists, here's an example. Try out all the different things you can do with tuples.

```python
name1 = ('One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops')

name2 = ('1 Drop', '2 Drops', '3 Drops', '4 Drops', '5 Drops')

list1 = [1, 2, 3, 4, 5]

# Count the elements
print(len(name1))
# Join: add two tuples together
print(name1 + name2)
# Repeat a tuple
print(name1 * 2)
# Is the element there? (Does name1 contain 'One Drop'?)
print('One Drop' in name1)
# The biggest element
print(max(name2))
# The smallest element
print(min(name2))
# Turn a list into a tuple
print(tuple(list1))
```

Output:

```
5
('One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops', '1 Drop', '2 Drops', '3 Drops', '4 Drops', '5 Drops')
('One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops', 'One Drop', 'Two Drops', 'Three Drops', 'Four Drops', 'Five Drops')
True
5 Drops
1 Drop
(1, 2, 3, 4, 5)
```
