# Study-time tracker

This is the complete reference version of the extra practice in "What to do after you finish". It brings together variables, containers, loops, functions, files, exceptions and tests. The input is a subject and a number of minutes (a whole number, not negative); the output is a list of records and totals. The data is saved in a local JSON file that you choose. It only uses the Python 3.10+ standard library – no account or third-party service needed.

Open a terminal in this folder, run the help first, then practise with a fresh records file:

```bash
python3 tracker.py --help
python3 tracker.py --file practice-records.json add Python 15
python3 tracker.py --file practice-records.json add Reading 10
python3 tracker.py --file practice-records.json add Python 5
python3 tracker.py --file practice-records.json list
python3 tracker.py --file practice-records.json total
python3 tracker.py --file practice-records.json total --subject Python
python3 -m unittest -v
```

The total should be 30 minutes, and the Python total should be 20 minutes. Adding more keeps adding to the existing records, so don't add the same set again and again just to compare with the example. Zero minutes is allowed; negative numbers, empty subjects, damaged JSON and content with the wrong fields all give an error. If the file doesn't exist, it starts with an empty list; if an existing file is damaged, its content is kept and not overwritten with empty data.

You can try building it yourself first without looking at `tracker.py`, in this order:

1. Write three records using a list and dictionaries, and print them.
2. Use a loop to total all the minutes, and the minutes for one subject.
3. Write `make_record(subject, minutes)` and `total_minutes(records, subject=None)`.
4. Save and load with UTF-8 and JSON, then start the program again to check.
5. Handle invalid input and damaged files.
6. Read `test_tracker.py` and make your own version pass the tests. If you already have pytest, you can also run `python3 -m pytest -q`.

First explain each function's inputs, outputs and when it fails, then compare with the reference version. The test data lives in a separate system temporary folder, so the tests never read your real study records.

The browser practice page is good for running pure Python calculations. Files in the browser belong to a virtual file system inside the page – they aren't files on your computer's disk, and they might not be kept after a refresh. Do the terminal, argument and saving-between-runs practice on your own computer.

This tool is for teaching. It writes JSON directly when saving, with no transactions, no handling for several people writing at once, and no automatic backups. Use practice data to check it – don't use it as a real data store.
