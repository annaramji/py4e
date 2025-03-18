################ 8.1: Lists ####################

# strings are immutable
## when using something like .lower(), it makes a copy of the string (new string) then performs the operation

# lists are mutable
## can change the value of an element in a list (using index operator)


# string length
## len() on string returns the number of characters in the string

# list length
## len() function tells you how many elements are in a list (not base 0)

# range() function
## returns a *list* of numbers that range from 0 to one less than the parameter
## range(4) returns [0, 1, 2, 3]

# print(list(range(4)))
## note: range and other functional-style methods, such as map, reduce, and filter, return iterators in Python 3. In Python 2 they returned lists.

# friends = ['Joey', 'Chandler', 'Phoebe', 'Ross', 'Monica', 'Rachel']
# print(list(range(len(friends))))


# we can construct an index loop using "for" and an integer iterator

# going through each element
# for friend in friends:
#     print('Happy New Year:', friend)


# going through numbers (index)  (will know what i (index position) is)
# for i in range(len(friends)):
#     friend = friends[i]
#     print('Happy New Year:', friend)
#     # print(i)

############# 8.2: Manipulating Lists #################

# concatenating lists using the "+" operator
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# adding a and b to make c DOES NOT change a or b

# lists can be sliced using the colon operator
# t = [9, 41, 12, 3, 74, 15]
# print(t[1:3])  # [41, 12]
# print(t[:4])  # [9, 41, 12, 3]
# print(t[3:])  # [3, 74, 15]
# print(t[:])  # [9, 41, 12, 3, 74, 15]

## remember: second number is "Up to but not including"

# list methods
# x = list()
# print(type(x))
# print(dir(x))
# [append, count, extend, index, insert, pop, remove, reverse, sort] # etc.


# building a list from scratch
# we can create an empty list and then add elements using the append method
# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)

# stuff.append('cookie')
# print(stuff)

# the list stays in order and new elements are added at the end of the list
## by appending, we're actually changing the list in place (mutable)

# DO NOT want to do: x = x.append. 

# is something in a list?
## Python provides two operators that let you check if an item is in a list

# these are logical operators that return True or False

## they do not modify the list

# some = [1, 9, 21, 10, 16]
# print(9 in some)  # True
# print(15 in some)  # False
# print(20 not in some)  # True


# Lists are in Order
# A list can hold many items and keeps those items in the order until we do something to change the order
# A list can be sorted (i.e., change its order)
# The sort method (unlike in strings) means “sort yourself”

# friends.sort()
# print(friends)
# print(friends[0])


# Built-in Functions and Lists

## there are a number of functions build into Python that take lists as parameters

# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))  # 6
# print(max(nums))  # 74
# print(min(nums))  # 3
# print(sum(nums))  # 154
# print(sum(nums) / len(nums))  # 25.666666666666668


# if you have a list, and these are lists of numbers, the functions above are better than writing your own loops

# manually constructed loop, counter, sum
# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average:', average)


# alternative (data structure, algorithm constructed to produce count and sum):

# numlist = list() # empty list
# while True: # same while loop
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value) # new: remember that, put it in list. not doing any calculation here yet.

# # using sum() to calculate total here, instead of doing that manually in the loop
# average = sum(numlist) / len(numlist)
# print('Average:', average)


# difference: numlist has to have all of the numbers in memory before it can do calculation. if under 100k, second is better. 
# If larger, memory usage is better in first option (2 numbers in memory, not all of them)

############# 8.3: Lists and Strings #################

# Best friends: lists and strings

# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# # ['With', 'three', 'words']

# print(len(stuff))
# # 3

# print(stuff[0])
# # With

# for w in stuff:
#     print(w)
# # With
# three
# words


# Split breaks a string into parts and produces a list of strings. 
# We think of these as words. We can access a particular word or loop through all the words.



# split()

# when you do not specify a delimiter, multiple spaces are treated like one delimiter
# you can specify what delimiter character to use in the splitting

# line = 'A lot       of spaces'
# etc = line.split()
# print(etc)

# line = 'first;second;third'
# thing = line.split()
# print(thing)
# # ['first;second;third']

# thing = line.split(';')
# print(thing)
# # ['first', 'second', 'third']

# print(len(thing))
# # 3


# example: parsing mail data

## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# fhand = open('code3/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip() # strip whitespace on right hand side
#     if not line.startswith('From '): # if line does not start with 'From ', continue (only read the "from" lines)
#         continue
#     words = line.split() # split the line into words based on spaces
#     print(words[2]) # always going to be the day of the week



# line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# words = line.split()
# print(words)
# ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']


# The Double Split Pattern

# Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again

# line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# #line = ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']
# words = line.split()
# print(words)
# print(list(range(len(words))))

# email = words[1]
# print(email)

# pieces = email.split('@')
# print(pieces)
# # ['stephen.marquard', 'uct.ac.za']

# print(pieces[1])
# # uct.ac.za



#### List Summary ####
## concept of a collection
## lists and definite loops
## indexing and lookup
## list mutability
## functions: len, min, max, sum
## slicing lists
## list methods: append, sort, split
## sorting lists
## splitting strings into lists of words
## using split to parse strings

# fruit = 'Banana'
# fruit[0] = 'b' # error
# TypeError: 'str' object does not support item assignment
# print(fruit)



# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output

# fname = 'code3/romeo.txt'
# fn = open(fname)
# lst = list()
# for line in fn:
#     words = line.split()
#     for word in words:
#         if word not in lst:
#             lst.append(word)

# lst.sort()
# print(lst)

# output: ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

