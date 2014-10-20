# Class Info
- teacher: Suneel Chakravorty, twitter: @suneelius
- chakravorty@post.harvard.edu
guest access for chatroom: https://www.hipchat.com/geDHwPme2
- class chatroom: https://suneelius.hipchat.com/chat
- wifi: GA guest, password: yellowpencil

# Python Warm Up and Diagnostic
## Objectives
- review/test/warm up knowledge of lists, for loops, logical control flow, and list comprehensions

1. Write a function that takes prints all the even numbers between 1 and 10,000.
2. Write a function that returns a list of the numbers between 1 and 10,000 that are divisible by 3.
3. The same as 2, but use Python list comprehensions
4. Write a function `get_max` that takes a list of numbers and returns the max of those numbers, don't use the builtin `max()` function. Afterward,  try using `max()`
5. Write a function `is_odd_or_div_by_7` that returns True if a number is odd or divisble by 7 and False otherwise. Then write it using a `lambda` function.
6. Use `is_odd_or_div_by_7` and list comprehensions to write a function `get_sublist_of_numbers_odd_or_div_by_7` that takes in a list and returns a sublist of those numbers that are either odd or divisible by 7.
7. Given a list of food orders, e.g. ```["burger", "fries", "burger", "tenders", "apple pie"]```, write a function `get_aggregate_order_counts` that takes the list and returns a dictionary with the different dishes as keys and the number of times they appear in the list as the values. For example, it takes ```["burger", "fries", "burger", "tenders", "apple pie"]``` and outputs ```
{
   "burger": 2,
   "fries": 1,
   "tenders": 1,
   "apple pie": 1
}```
8. Use collections.Counter to achieve the same functionality.
9. Write a function `get_most_popular_order_data` that takes a list of orders but instead of returning a dictionary with the counts, it just outputs a tuple: the dish that appears the most in the list and the number of times it appears in the list. So the output given the example would be ```("burger", 2)```

# Data Set Worksheet 1
## Objectives
- use csv library to read in data
- use pure Python techniques to extract insights about the data
- start getting acquainted with the Pandas library

1. Using csv library, read in data from rock.csv, which you can download here: https://www.dropbox.com/s/cbffxkqq0ujru58/rock.csv?dl=0
2. How many songs are from 1981?
3. How many songs are from before 1984
4. What is the earliest release year in the data? (HINT: You might have to account for/clean up dirty data)
5. What are the top 20 songs by play count (HINT: use builtin sorted() function, documentation here: https://wiki.python.org/moin/HowTo/Sorting)
6. Who are the top 10 most prolific artists in the data along with the number of their songs that appear in the data?
7. How many different artists appear in the data?
8. How songs does 'Rock' appear in the title of?

# Now let's get ready for Data Science. Install Anacondas
- Instructions for Mac: http://docs.continuum.io/anaconda/install.html#mac-install
- Instructions for Windows: http://docs.continuum.io/anaconda/install.html#windows-install
- Setting up your environment, using the `conda` command line tool:
```bash
conda create -n ga-python pandas matplotlib ipython
source activate ga-python
ipython -pylab
>>> import pandas
```

# Pandas Methods and Concepts
- read_csv
- .columns
- [:], like list slicing
- .head()/tail()
- filtering
- restricting columns
- add columns
- getting count of rows from .index
- get value_counts
- apply() functions to a column
- string methods
- .plot

# Data Science Worksheet 2
## Objectives
- practice using Pandas
- learn how to sort

Download csv from https://github.com/suneel0101/lesson-plan/blob/master/crunchbase_monthly_export.csv

1. What are the top 10 highest funded companies?
2. How many companies are from New York?
3. What are the most popular Markets?
4. Plot # of companies against region, limiting to 20 most popular regions
