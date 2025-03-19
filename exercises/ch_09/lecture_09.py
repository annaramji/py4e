# Dictionaries


# context: before Python 3.7, dictionaries did not keep entries in the order of insertion
# now they do (3.7 and on)
# "insertion order" means the order in which the keys were added to the dictionary
# this is not the same as "sorted order"
# sorted order is when the keys are sorted in some way (alphabetical, numerical, etc.)


# learning how lists, dictionaries, and tuples work is really interesting CS, but not covered in this course

# Using Python collections is easy. Creating the code to support them is
# tricky and uses Computer Science concepts like dynamic memory, arrays,
# linked lists, hash maps and trees.


#  We append values to the end
# of a List and look them up by
# position
# • We insert values into a
# Dictionary using a key and
# retrieve them using a key

# indexing mechanism for lists is based on position
# indexing mechanism for dictionaries is based on key


#  We append values to the
# end of a List and look
# them up by position
# • We insert values into a
# Dictionary using a key
# and retrieve them using a
# key


cabinet = dict{}

cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75

print(cabinet)
# {'summer': 12, 'fall': 3, 'spring': 75}

print(cabinet['fall'])
# 3

cabinet['fall'] = cabinet['fall'] + 2

print(cabinet['fall'])
# 5

print(cabinet)
# {'summer': 12, 'fall': 5, 'spring': 75}


### Comparing Lists and Dictionaries

# Dictionaries are like lists except that they use keys instead of
# numbers to look up values

# think of index of list as the key

## Dictionary Literals (Constants)

# Dictionary literals use curly braces and have a list of key: value pairs
# you can make an empty dictionary using curly braces

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj)
# {'chuck': 1, 'fred': 42, 'jan': 100}

ooo = { }
print(ooo)
# {}


###### 9.2: Counting with Dictionaries

# One common use of dictionaries is counting how often we “see” something

ccc = dict()

ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
# {'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
# {'csev': 1, 'cwen': 2}

## Dictionary Tracebacks
# It is an error to reference a key which is not in the dictionary
# We can use the in operator to see if a key is in the dictionary

ccc = dict()
print(ccc['csev'])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'csev'
'csev' in ccc
# False

## When we see a new name
# When we encounter a new name, we need to add a new entry in the dictionary
# and if this the second or later time we have seen the name, we simply add
# one to the count in the dictionary under that name

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
# {'csev': 2, 'cwen': 2, 'zqian': 1}

## The get Method for Dictionaries
# The pattern of checking to see if a key is already in a dictionary 
# # and assuming a default value if the key is not there 
# is so common that there is a method called get() that does this for us


if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)
# Default value if key does not exist (and no Traceback)
# {'csev': 2, 'cwen': 2, 'zqian': 1}

## Simplified Counting with get()
# We can use get() and provide a default value of zero
#  when the key is not yet in the dictionary -- and then just add one

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1 # 0 is default (if name isn't there, it's 0, then add 1. If it is there, get count value and still add 1)
print(counts)

# every dictionary has this .get() method

# Counting is Marvelous -- Count on Sesame Street (just look it up on YouTube) :) 