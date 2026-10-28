# 2. Installing Python #

> The screenshots and commands below use Python 3.6 / 3.7 as an example. The installer you see today may look different. For the exercises, download a Python 3 version that is still supported from the [official Python download page](https://www.python.org/downloads/), and check the minimum version each chapter asks for. After installing, run `python3 --version` (on Windows you can also use `py --version`) to check which version is really running. Use your own install location for any paths.

Python is cross-platform. It runs on Windows, Mac and all kinds of Linux/Unix systems. Python has had two main versions: 2.x and 3.x. They do not work with each other. I installed version 3.6.1.

Where should you download it? I suggest the official website, so you always get the newest version. The official website is: [https://www.python.org/](https://www.python.org/)

## 1. Installing on Windows ##

On Windows, after downloading, just run the installer. Remember to tick **Add Python 3.6 to PATH**, then click **Install Now** to finish.

Pay attention here: make sure you tick "Add Python 3.6 to Path". If you tick it, you don't need to set up the environment variable yourself. If you don't, you will have to do it by hand.

In the "Install Python 3.6.1 (64-bit)" setup window, you will see two choices:

- **Install Now**: install with the default settings. The default path is `C:\Users\Administrator\AppData\Local\Programs\Python\Python36`. It includes IDLE, pip and the documentation, and creates shortcuts and file links.
- **Customize installation**: choose your own install path and features.

Whichever you choose, there are two tick boxes at the bottom: "Install launcher for all users (recommended)" and "Add Python 3.6 to PATH". **Tick the second one and you won't need to set up the environment variable yourself.** Don't forget this step!

If you clicked too fast and forgot to tick "Add Python 3.6 to Path", don't worry. You just need to set the environment variable by hand.

In the command prompt (cmd), type:

```
path=%path%;C:\Python 
```

Very important: `C:\Python` is the folder where Python is installed. If you installed it somewhere else, type your own folder instead.

After installing, open a command prompt window and type `python`. If you see something like this, Python is installed:

```
C:\Users\Administrator>python
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

When you see the `>>>` prompt, you are in Python's **interactive mode**. You can type any Python code, press Enter, and see the result right away.


## 2. Installing on Mac ##

Macs often came with Python 2.x already installed, but nobody uses 2.x now. So I suggest downloading the newest version from https://www.python.org/downloads/mac-osx/ and installing it.

After installing, how do you set the environment variable?

First, check the current PATH:

``` 
echo $PATH
```

Then open ``` ~/.bash_profile (create it if it doesn't exist) ```

``` 
vi ~/.bash_profile
``` 

I installed Python 3.7, so the Python path is `/Library/Frameworks/Python. Framework/Versions/3.7/bin`. So I add this line:

```
export PATH="/Library/Frameworks/Python. Framework/Versions/3.7/bin:$PATH"
```

After that, `~/.bash_profile` looks roughly like this (this is from my own computer):

```bash
# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
export PATH
```

Finally, save and quit, then load the file:

```
source ~/.bash_profile
```
 





