# 4. String Encoding #

We all know computers can only work with numbers. To work with text, the computer must first turn the text into numbers. Early computers used 8 **bits** as one **byte**, so the biggest number one byte can hold is 255 (binary 11111111 = decimal 255). The numbers 0 – 255 were used for capital and small English letters, digits and some symbols. This table is called **ASCII** encoding. For example, capital `A` is 65, and small `z` is 122.

To show Chinese, one byte is clearly not enough. You need at least two bytes, and it must not clash with ASCII. So China created the **GB2312** encoding for Chinese characters.

Japanese, Korean and other languages had the same problem. To put all the world's writing into one system, **Unicode** was created. Unicode puts every language into one set of codes, so there are no more garbled characters.

Unicode usually uses two bytes for one character. To turn an old English (ASCII) code into Unicode, you just fill the extra byte with 0.

Python was born before the Unicode standard was published, so the earliest Python only supported ASCII. A normal string like `'ABC'` was stored as ASCII inside Python.

Python added Unicode support later. Unicode strings were written as `u'...'`.

But in modern Python 3, strings are Unicode. This means Python strings support many languages. That's why in the examples above, I didn't need to add `u'...'` and everything still showed correctly.

However, Python source code is itself a text file. So when your code contains non-English text (for example Chinese), you must save the file in **UTF-8** encoding. To make sure the Python interpreter reads the file as UTF-8, we usually put these two lines at the top:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

The first comment tells Linux/OS X that this is a Python program that can be run. Windows ignores it.

The second comment tells the Python interpreter to read the source code as UTF-8. Otherwise, non-English text in your code might come out as garbled characters.

Declaring UTF-8 does **not** mean your `.py` file really is UTF-8. You must also make sure your text editor is saving with **UTF-8 without BOM**.


