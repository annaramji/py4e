# # lecture 10: tuples

# # immutable! 
# # don't sort, append, or reverse on a tuple

# l = list()
# print(dir(l))

# t = tuple()
# print(dir(t))

# # tuples and assignment
# (x, y) = (4, 'fred') # unpacking a tuple
# print(y)

# (a, b) = (99, 98)
# print(a)


# # tuples and dictionaries
# d = dict()
# d['csev'] = 2
# d['cwen'] = 4
# for (k, v) in d.items():
#     print(k, v)

# tups = d.items() # returns a list of tuples
# print(tups)

# # tuples are comparable
# print((0, 1, 2) < (5, 1, 2))
# print((0, 1, 200000) < (0, 3, 4)) # stops once it finds elements that differ
# print(('Jones', 'Sally') < ('Jones', 'Sam')) # compares first element, then second, then third character in second term
# print(('Jones', 'Sally') > ('Adams', 'Sam')) # stops at first element


# # using sorted()
# d = {'b': 1, 'c': 22, 'a': 10}
# print(d.items()) # returns a list of tuples in the original order
# t = sorted(d.items()) # sorts the keys
# print(t)

# print(d.items())


# c = {'a': 10, 'b': 1, 'c': 22}
# tmp = list()
# for k, v in c.items():
#     tmp.append( (v, k) ) # creates a list of tuples with value first

# print(tmp)

# tmp = sorted(tmp, reverse=True) # sorts by value, descending
# print(tmp)

# fhand = open('./unit3/romeo.txt')
# counts = dict()
# for line in fhand: 
#     words = line.split() # splits the line into words
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# # print(counts)
# # reverse tuple
# lst = list()
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)  # creates a list of tuples with value first

# lst = sorted(lst, reverse=True)  # sorts by value, descending order

# for val, key in lst[:10] : # list slicing: start at 1, go up to not including 10 # prints the first 10 items (10 most common words)
#     print(key, val)

## even shorter version
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted( [ (v, k) for k, v in c.items() ] ) )  # sorts by value!, ascending order
print(sorted( [ (v, k) for k, v in c.items() ], reverse=True ))  # sorts by value!, descending order
# extract this tuple of value, keys -- for all, create tuples (v, k), for each pair of key, value pair in c.items(). 




test_line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# extract the hour
# from the line, which is the two digits before the ':'


# print in sorted order by hour (ascending), where hour is the two digits before the ':'

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1
   
l = sorted(counts.items())

for k, v in l:
    print(k, v)