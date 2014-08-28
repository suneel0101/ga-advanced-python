## What is this class about?
By the end of the class you should have
- learn some more advanced Python techniques
- become comfortable with the Pandas data analysis library

## Shell vs Scripting Python
### Shell:

1. Open Terminal
2. run
```bash
$ python
>>> "Hello"
Hello
>>> 2 + 2
4
>>> exit()
$
```

### Scripting
Run:
```bash
$ mkdir ~/Documents/ga-python-data-science
$ cd ~/Documents/ga-python-data-science
$ touch test.py
```

In your editor, open up test.py and write the following line:
print "Hello, world!"
Save and close the file.
Then in the terminal, run
$ python test.py
Hello, world!


## Python Exercises

1 - Write a function that prints all the even numbers between 1 and 10,000.

Solution:
```python
def print_even_numbers():
    for x in xrange(10001):
        if x % 2 == 0:
           print x
```
This reviewed FOR LOOPS, IF CONDITIONS, and PRINTING

2 - Write a function that returns a list of the numbers between 1 and 10,000 that are divisible by 3.

Solution:
```python
This reviews basic use of LISTS
def divisible_by_3():
    numbers = []
    for x in xrange(10001):
        if x % 3 == 0:
           numbers.append(x)
    return numbers
```
Note: we use `xrange` instead of `range` because `range` loads the entire list into memory, while `xrange` just creates an iterator: https://mail.python.org/pipermail/python-list/2012-November/634509.html. If you have a really big list, `xrange` is way faster.

3 - The same as #2, but use Python list comprehensions.

Solution:
```python
def divisible_by_3():
    return [x for x in xrange(10001) if x % 3 == 0]
```
Note: List comprehensions are super useful. They allow you to iterate through lists and generate new lists on the fly with very little code.

4 - Write a function that takes a list of numbers and returns the max of those numbers, don't ues the max() function.

Solution:
```python
def get_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
           max_number = number
    return max_number
```
Note: Here we just tested out our logic skills.

5 - Use the max() function to achieve the same functionality

Solution:
```python
def get_max(numbers):
    return max(numbers)
```
Note: `max` is useful, as are `sorted` and `min`, some of which we'll use later on.

6 - Write a function that returns True if a number is odd or divisble by 7 and False otherwise.

Solution:
```python
def is_odd_or_div_by_7(number):
    return (number % 2 == 1 or number % 7 == 0)
```

7 - Use the function in #6 and list comprehensions to write a function that given a list of numbers returns a sublist of numbers
that are odd or divisible by 7.

Solution:
```python
def get_sublist_of_numbers_odd_or_div_by_7(numbers):
    return [number for number in numbers if is_odd_or_div_by(number)]
```
Note: Here we are combining our knowledge of list comprehensions with some conditional logic inside the list comprehension.

8 - Given a list of food orders, e.g. ["burger", "fries", "burger", "tenders", "apple pie"], write a function that takes the list
and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example,
Takes ["burger", "fries", "burger", "tenders", "apple pie"] and turns it into
{
   "burger": 2,
   "fries": 1,
   "tenders": 1,
   "apple pie": 1
}

Solution:
```python
def aggregate_counts(order_list):
    orders_by_count = {}
    for order in order_list:
        # if we've already seen this order, increment the count
        if order in orders_by_count:
           orders_by_count[order] += 1
        # otherwise, this is the first time we're seeing it, so set its count to 1
        else:
           orders_by_count[order] = 1
    return orders_by_count
```

9 - Use collections.Counter to achieve the same functionality.

Solution:
```python
from collections import Counter

def aggregate_counts(order_list):
    return Counter(order_list)
```
Note: Good lesson here is that Python has a ton of useful libraries, so don't reinvent the wheel.

10 - Write a function that takes the same kind of input as in #9 but instead of returning a dictionary with the counts, it just returns a tuple: the dish that appears the most in the list and the number of times it appears in the list. So the output given the example would be ("burger", 2)

Solution:
```python
def get_most_popular_order_data(order_list):
    agg_counts = aggregate_counts(order_list)
    # the key is a function that tells `max` what to sort by
    # in this case, it's the second element of the tuple, e.g. 2 in ("burger", 2)
    # which is just the number of times it appears in the list of orders
    return max(agg_accounts.iteritems(), key=lambda: agg_count[1])
```
Note: for more on lambda functions, check this out http://www.diveintopython.net/power_of_introspection/lambda_functions.html


## Python Data Science Worksheet 1
## Objectives
- use csv library to read in data
- use pure Python techniques to extract insights about the data
- start getting acquainted with the Pandas library

### Exercises

1 - Using csv library, read in data from https://raw.githubusercontent.com/suneel0101/data/master/classic-rock/classic-rock-song-list.csv.
NOTE: Make sure to open the file on the browser, highlight and copy the contents into your text editor and save. Otherwise, you'll get some errors when trying to read the file through the `csv` library.
HINT: Here's the relevant documentation on csv: https://docs.python.org/2/library/csv.html, use `DictReader`
```
$ python
>>> import csv
>>> csvfile = open('rock.csv', 'rb')
>>> reader = csv.DictReader(csvfile)
>>> dir(reader)
>>> reader.filenames
```

2 - How many songs are from 1981?

Solution:
```
>>> rows = [row for row in reader]
>>> len([row for row in rows if row['Release Year'] == '1981'])
61
```

3 - What is the earliest release year in the data?
HINT: You might have to account for/clean up dirty data

#### First pass
```
>>> min([int(row['Release Year']) for row in rows if row['Release Year']])
ValueError: invalid literal for int() with base 10: 'SONGFACTS.COM'
```
SONGFACTS.com is not a valid year, so we'll have to clean up Release Year by ensuring we are dealing with integers.

#### Second pass
```
>>> def is_valid_year(value):
...     try:
...         val = int(value)
...     except ValueError:
...         pass
        else:
            return val
...

>>> release_years = [int(row['Release Year']) for row in rows if is_valid_year(row['Release Year'])]
>>> min(release_years)
1071
```

This doesn't make any sense! Exclude that!

#### Third pass
```
>>> def is_valid_year(value):
...     try:
...         val = int(value)
...     except ValueError:
...         pass
        else:
           if val > 1900:
              return val
>>> release_years = [int(row['Release Year']) for row in rows if is_valid_year(row['Release Year'])]
>>> min(release_years)
1955
```

That makes much more sense!

4 - How many songs are from before 1984
```
>>> before_1984 = [
    row for row in rows
    if is_valid_year(row['Release Year']) and is_valid_year(row['Release Year']) < 1984
]
>>> print len(before_1984)
```

5 - What are the top 20 songs by play count
HINT: use builtin sorted() function
```
>>> top_20_rows_by_play_count = sorted(rows, key=lambda row: row['PlayCount'], reverse=True)[:20]
>>> top_20_play_count_song_names = [row['Song Clean'] for row in top_20_rows_by_play_count]
["(Don't Fear) The Reaper", 'Layla', 'Back In Black', 'All Right Now', 'Refugee', 'Bad Company', 'Gimme Shelter', "Runnin' Down a Dream", "Jamie's Cryin'", 'Sweet Home Alabama', 'Foreplay (Long Time)', 'Over the Hills and Far Away', 'Who Are You', 'Lights', 'In the Air Tonight', 'Come Sail Away', 'Highway To Hell', 'Rock and Roll', 'Comfortably Numb', "Rock 'n' Roll Fantasy"]
```
6 - Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?
```
>>> artists = [row['ARTIST CLEAN'] for row in rows]
>>> from collections import Counter
>>> artists_by_play_count = Counter(artists)
>>> artists_ordered_by_play_count = sorted(artists_by_play_count.items(), key=lambda artist_and_count: artist_and_count[1], reverse=True)
>>> artists_ordered_by_play_count[:10]
[('The Beatles', 100), ('Led Zeppelin', 69), ('Rolling Stones', 55), ('Van Halen', 44), ('Pink Floyd', 39), ('Aerosmith', 31), ('The Who', 31), ('Tom Petty & The Heartbreakers', 29), ('AC/DC', 29), ('Bob Seger', 24)]
```
7 - How many different artists appear in the data?
```
>>> artists = [row['ARTIST CLEAN'] for row in rows]
>>> len(set(artists))
475
```
NOTE: How is a Python set different from a list?

8 - How many songs does 'Rock'/'rock' appear in the title of?
```
>>> with_rock_in_title = [row for row in rows if 'rock' in row['Song Clean'].lower()]
>>> len(with_rock_in_title)
60
```

## Now let's get ready for Data Science. Install Anacondas
### Instructions for Mac: http://docs.continuum.io/anaconda/install.html#mac-install
### Instructions for Windows: http://docs.continuum.io/anaconda/install.html#windows-install
### Setting up your environment: `conda` command line tool:
```bash
conda create -n ga-python pandas matplotlib ipython
source activate ga-python
python
>>> import pandas
```

## Pandas Makes Life Easier
What are we going to learn?
- how to read in data from a csv
- how to filter and slice DataFrames
- how to get aggregate counts
- how to apply functions to entire columns
- string methods
- some data cleaning using `apply`

### How to read in csvs
```python
$ ipython -pylab
>>> from pandas import read_csv
>>> rock_data = read_csv('rock.csv')
```
`rock_data` is a DataFrame, super powerful data structure that has some of the traits of lists but with a lot more functionality, as we'll find out.
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. You can think of it like a spreadsheet or SQL table, or a dict of Series objects.

I can see the columns of the DataFrame like this:
```python
>>> rock_data.columns
```

I can slice the DataFrame like a list and just see the first twenty rows like this:
```python
>>> rock_data[:20]
```

I can limit the columns to just look at the Song Clean and Release Year columns:
```python
>>> rock_data[['Song Clean', 'Release Year']]
```
I can both limit the columns and slice at the same time, doesn't matter in what order:
```python
>>> rock_data[['Song Clean', 'Release Year']][:20]
>>> rock_data[:20][['Song Clean', 'Release Year']]
```

I can just take a look at one column DataFrame like this:
```python
>>> rock_data[['Song Clean']]
```

Or I can turn it into a Series, like this:
```python
>>> rock_data['Song Clean']
```
 Series is a one-dimensional labeled array capable of holding any data type

I can filter my table based on some logic. Let's answer the question from above:
How many songs were released in 1981?
```python
>>> from_1981 = rock_data[rock_data['Release Year']=='1981']
# Think about the [] brackets like a WHERE clause
```
This says, get me the part of the table where Release Year is '1981'

I can get the count of the rows like this:
```python
>>> len(from_1981.index)
```

I can find the number of times each value appears. Let's try it out with the same question from above:
Who are the 10 most prolific artists?
```python
# Get all the artist names along with the number of times they appear in the list
>>> rock_data['ARTIST CLEAN'].value_counts()
# Just get the top 10
>>> rock_data['ARTIST CLEAN'].values_counts()[:10]
# .head() just gives us a sample from the beginning of the DataFrame
# .tail() gives us a sample from the end of the DataFrame
>>> rock_data['ARTIST CLEAN'].values_counts().head()
```

How many songs contain the word 'Rock'/'rock'/'ROCK' (and any other upper/lower case combination) in it?

```python
# I can create a new column in the DataFrame the same way we add keys to dictionaries
# Here I'm creating a column 'has rock in title' with True if rock is in the lowercase version of the title and False if not.
>>> rock_data["has rock in title"] = rock_data['Song Clean'].apply(lambda title: "rock" in title.lower())
# filter down to just where contains_rock is True
# Here is the explicit way to do it
>>> rock_data[rock_data["has rock in title"] == True]
# Here is the implicit way to do it, do you see why they are the same?
>>> rock_data[rock_data["has rock in title"]]
```

What is the earliest release year in the data?

We need to clean the data. Let's use apply. Let's change any nonstring or below 1900 to None, same as we did above.

```python
>>> def is_number(year):
...     try:
...         int(year)
...     except ValueError:
...         return False
...     else:
...         return True
...
>>> def is_before_1900(year):
...     return int(year) < 1900
# removes string outliers and year outliers like 1071 and turns year into an int
>>> clean_year = lambda year: None if not is_number(year) or is_before_1900(year) else int(year)
>>> rock_data["Release Year Clean"] = rock_data["Release Year"].apply(clean_year)
# Use .min() function of dataframes, very useful!
>>> rock_data["Release Year Clean"].min()
1955
```

Plot year against number of songs released in that year
```python
# to do this, make sure you started the shell with ipython -pylab
>>> series = rock_data['Release Year Clean'].value_counts()
>>> series.plot(color='blue', kind='bar')
# this should launch a graph
# if nothing is showing, try the following two lines:
>>> import pylab
>>> pylab.show()
```
## We Learned A Lot!

### Python
- list comprehensions
- list comprehensions with conditional logic
- sets
- lambda functions
- Counter


### Pandas
- DataFrames
- Series
- the .head() and .tail() functions
- the .apply() function
- the .min() function
- string methods
- filtering DataFrames
- slicing DataFrames
- adding new columns to DataFrames
- selecting specific columns from DataFrames
- plotting Series
- cleaning data
- the .value_counts() function
