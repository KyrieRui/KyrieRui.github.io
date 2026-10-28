
#

# Common Regular Expressions

## Expressions for checking numbers

```
1.  Digits: ^[0-9]*$
2.  Exactly n digits: ^\d{n}$
3.  At least n digits: ^\d{n,}$
4.  m to n digits: ^\d{m,n}$
5.  Zero, or a number not starting with zero: ^(0|[1-9][0-9]*)$
6.  A number not starting with zero, with up to two decimal places: ^([1-9][0-9]*)+(.[0-9]{1,2})?$
7.  A positive or negative number with 1–2 decimal places: ^(\-)?\d+(\.\d{1,2})?$
8.  Positive numbers, negative numbers and decimals: ^(\-|\+)?\d+(\.\d+)?$
9.  A positive real number with two decimal places: ^[0-9]+(.[0-9]{2})?$
10. A positive real number with 1–3 decimal places: ^[0-9]+(.[0-9]{1,3})?$
11. A non-zero positive integer: ^[1-9]\d*$ or ^([1-9][0-9]*){1,3}$ or ^\+?[1-9][0-9]*$
12. A non-zero negative integer: ^\-[1-9][]0-9"*$ or ^-[1-9]\d*$
13. A non-negative integer: ^\d+$ or ^[1-9]\d*|0$
14. A non-positive integer: ^-[1-9]\d*|0$ or ^((-\d+)|(0+))$
15. A non-negative float: ^\d+(\.\d+)?$ or ^[1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0$
16. A non-positive float: ^((-\d+(\.\d+)?)|(0+(\.0+)?))$ or ^(-([1-9]\d*\.\d*|0\.\d*[1-9]\d*))|0?\.0+|0$
17. A positive float: ^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$ or ^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$
18. A negative float: ^-([1-9]\d*\.\d*|0\.\d*[1-9]\d*)$ or ^(-(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*)))$
19. A float: ^(-?\d+)(\.\d+)?$ or ^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$
```


## Expressions for checking characters

```
1.  Chinese characters: ^[一-龥]{0,}$
2.  English letters and digits: ^[A-Za-z0-9]+$ or ^[A-Za-z0-9]{4,40}$
3.  Any characters, length 3–20: ^.{3,20}$
4.  A string of the 26 English letters: ^[A-Za-z]+$
5.  A string of the 26 capital English letters: ^[A-Z]+$
6.  A string of the 26 lowercase English letters: ^[a-z]+$
7.  A string of digits and the 26 English letters: ^[A-Za-z0-9]+$
8.  A string of digits, the 26 English letters or underscores: ^\w+$ or ^\w{3,20}$
9.  Chinese, English, digits and underscores: ^[一-龥A-Za-z0-9_]+$
10. Chinese, English and digits, but no underscores or other symbols: ^[一-龥A-Za-z0-9]+$ or ^[一-龥A-Za-z0-9]{2,20}$
11. Input that does not contain ^%&',;=?$\" and similar characters: [^%&',;=?$\x22]+
12. Input that does not contain ~: [^~\x22]+
```

## Expressions for special needs

```
1.  Email address: ^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
2.  Domain name: [a-zA-Z0-9][-a-zA-Z0-9]{0,62}(/.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+/.?
3.  Internet URL: [a-zA-z]+://[^\s]* or ^http://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$
4.  Mobile number (mainland China): ^(13[0-9]|14[0-9]|15[0-9]|166|17[0-9]|18[0-9]|19[8|9])\d{8}$
5.  Phone number ("XXX-XXXXXXX", "XXXX-XXXXXXXX", "XXX-XXXXXXX", "XXX-XXXXXXXX", "XXXXXXX" and "XXXXXXXX"): ^(\(\d{3,4}-)|\d{3.4}-)?\d{7,8}$
6.  Landline number in China (0511-4405222, 021-87888822): \d{3}-\d{8}|\d{4}-\d{7}
7.  18-digit Chinese ID number (digits, may end in x): ^((\d{18})|([0-9x]{18})|([0-9X]{18}))$
8.  Valid username (starts with a letter, 5–16 characters, letters, digits and underscores allowed): ^[a-zA-Z][a-zA-Z0-9_]{4,15}$
9.  Password (starts with a letter, 6–18 long, only letters, digits and underscores): ^[a-zA-Z]\w{5,17}$
10. Strong password (must mix capital letters, lowercase letters and digits, no special characters, 8–10 long): ^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$  
11. Date format: ^\d{4}-\d{1,2}-\d{1,2}
12. The 12 months of a year (01–09 and 1–12): ^(0?[1-9]|1[0-2])$
13. The 31 days of a month (01–09 and 1–31): ^((0?[1-9])|((1|2)[0-9])|30|31)$
14. Money input formats:
      a. We accept four ways of writing money: "10000.00", "10,000.00", and without cents, "10000" and "10,000": ^[1-9][0-9]*$
      b. That means any number not starting with 0. But it also means the single character "0" fails, so we use this instead: ^(0|[1-9][0-9]*)$
      c. Either a 0, or a number not starting with 0. We could also allow a minus sign at the start: ^(0|-?[1-9][0-9]*)$
      d. That means a 0, or a possibly negative number not starting with 0. Let's allow users to start with 0, and remove the minus sign, since money can't be negative. Next, let's allow an optional decimal part: ^[0-9]+(.[0-9]+)?$
      e. Note that there must be at least 1 digit after the decimal point, so "10." fails, but "10" and "10.2" pass: ^[0-9]+(.[0-9]{2})?$
      f. This requires exactly two digits after the decimal point. If you think that's too strict, use this: ^[0-9]+(.[0-9]{1,2})?$
      g. This lets users write just one decimal place. Next, let's think about commas in the number: ^[0-9]{1,3}(,[0-9]{3})*(.[0-9]{1,2})?$
      h. 1 to 3 digits, followed by any number of (comma + 3 digits), with commas optional instead of required: ^([0-9]+|[0-9]{1,3}(,[0-9]{3})*)(.[0-9]{1,2})?$
15. XML file: ^([a-zA-Z]+-?)+[a-zA-Z0-9]+\\.[x|X][m|M][l|L]$
16. Regex for Chinese characters: [一-龥]
17. Double-byte characters: [^\x00-\xff]    (includes Chinese characters; can be used to work out string length, counting a double-byte character as 2 and an ASCII character as 1)
18. Regex for blank lines: \n\s*\r    (can be used to delete blank lines)
19. Regex for HTML tags: <(\S*?)[^>]*>.*?</\1>|<.*? />    (the versions shared online are terrible; this one only partly works and still can't handle complex nested tags)
20. Regex for whitespace at the start and end: ^\s*|\s*$ or (^\s*)|(\s*$)    (can be used to remove whitespace – spaces, tabs, form feeds and so on – at the start and end of a line; very useful)
21. Tencent QQ number: [1-9][0-9]{4,}    (QQ numbers start from 10000)
22. Chinese postcode: [1-9]\d{5}(?!\d)    (Chinese postcodes are 6 digits)
23. IP address: \d+\.\d+\.\d+\.\d+    (useful for extracting IP addresses)
24. IP address: ((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))  
25. IPv6 address: (([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))
26. URL link: ((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?

```
