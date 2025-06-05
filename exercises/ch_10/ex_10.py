# worked exercise: tuples and sorting

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = 'exercises/ch_09/clown.txt'

fhand = open(fname)

many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1
# find the top 5 words by frequency
print(many)

print(sorted(many)) # only sorts the keys (lost the numbers)
print(sorted(many.items()))  # sorts by key, ascending order
print(sorted(many.items(), reverse=True))  # sorts by key, desc order


# sort by value, descending order

# long way:

tmp = dict()
newlist = list()
for k, v in many.items():
    tup = (v, k)
    newlist.append(tup)  # creates a list of tuples with value first

    # print(v, k)
    
print(newlist)
print("\n")
print(sorted(newlist))
print("\n")
print(sorted(newlist, reverse=True))  # sorts by value, descending order
print("\n")


# use this sorting by value, but print the key before the value
for v, k in sorted(newlist, reverse=True):
    print(k, v)  # prints the key first, then the value
# shorter way:
print("\n")
print(sorted( [ (v, k) for k, v in many.items() ], reverse=True ))  # sorts by value!, descending order


cool = sorted(newlist, reverse=True)  # sorts by value!, descending order
# print(cool)
print("\n")

for v,k in cool[0:5]: # first 5 items
    print(k, v)  # prints the key first, then the value



