# 3. Your First Python Program #

OK, enough talking. Now we can write our first Python program!

When you start writing Python, I don't really suggest using a special tool, because it makes it harder to get used to the syntax. So here I will use [Sublime Text](http://www.sublimetext.com/). Later you can switch to PyCharm.

Our first Python program will, of course, print **Hello Python**.

If you have never programmed before and don't understand anything yet, that's OK. For your first program, just follow along, get a feel for it, and give it a try.

Create a new file and name it `HelloPython.py`. Notice that the file ends with `.py`.

Then open the file and type `print('Hello Python')`


```python
print('Hello Python')
```


Finally, open a command line window, go to the folder where HelloPython.py is, and you can run the program. Here is the result:


```
C:\Users\Administrator>cd C:\Users\Administrator\Desktop\Python

C:\Users\Administrator\Desktop\Python>python HelloPython.py
Hello Python

C:\Users\Administrator\Desktop\Python>
```


If you use [Sublime Text](http://www.sublimetext.com/), and you set up the environment variable when you installed Python, you can just press Ctrl + B to run it. The result looks like this:

Note: in the bottom-right corner of Sublime Text, choose `Python` as the syntax. Otherwise Ctrl + B won't run your code correctly. After running, you will see the result in the output panel at the bottom:

```
Hello Python
[Finished in 0.5s]
```




## Once your first line works, change one small thing

The program above can already print text. First, write down two lines you would like to see. Then change the text below to your own version:

```python
print('Today I start learning Python')
print('First, finish a small example that runs')
```

Output:

```text
Today I start learning Python
First, finish a small example that runs
```

This time, only change the text inside the quotes. Run it and check that you get two lines. Next, leave out a closing bracket on purpose and run it again. Look at the error. When you read an error, first find the **error type** and **where in the code** it is. Don't delete everything and start again straight away. Put the bracket back, run it again, and check the problem is gone. This is a small but complete cycle: **change, observe, fix**.

The quotes and brackets here are Python syntax, so they must be normal keyboard symbols (not fancy "curly" quotes). Inside the quotes is the text we want to show, and it can be in any language. Special punctuation in the output text won't cause a syntax error.

Running code in the browser lets us focus on the code first. When you need to work with local files or the command line, set up Python by following the installation chapter. For now, just pick one editor that can run programs. You don't need to install every editor just to write your first line of code.
