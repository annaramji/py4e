
han = open('code3/mbox-short.txt')

# for line in han:
#     line = line.rstrip()
#     print("Line: ", line)
#     wds = line.split()
#     print('Words: ', wds)
#     if wds[0] != 'From' : 
#         print("Ignore")
#         continue
#     print(wds[2])

# returns:
# Sat
# Traceback (most recent call last):
#   File "/Users/aramji/dev/py4e/exercises/ch_08/ex_08.py", line 7, in <module>
#     if wds[0] != 'From': 
# IndexError: list index out of range

# note: printed out Sat... blew up later.

# we don't know what it was doing when it blew up
# step 1: find the line that caused the problem
# step 2: print statement above to see what word/line it was on

# now, we see a bunch of output. End is:

# Words:  ['X-DSPAM-Probability:', '0.0000']
# Words:  []
# Traceback (most recent call last):
#   File "/Users/aramji/dev/py4e/exercises/ch_08/ex_08.py", line 8, in <module>
#     if wds[0] != 'From' : 
# IndexError: list index out of range

# so, the problem is that the line is empty. We need to add a check for that.

# wds[0] is out of bounds when there are no words

# updated:

# for line in han:
#     line = line.rstrip()
#     print("Line: ", line)
#     wds = line.split()
#     print('Words: ', wds)
#     # guardian pattern
#     if len(wds) < 1 :
#         continue
#     if wds[0] != 'From' :  # could be dangerous if wds is empty
#         print("Ignore")
#         continue
#     print(wds[2])



# # alt:
# for line in han:
#     line = line.rstrip()
#     print("Line: ", line)
#     wds = line.split()
#     print('Words: ', wds)
#     # guardian pattern
#     if line == '': # if blank line (empty string), continue
#         # print("Skip blank")
#         continue
#     if wds[0] != 'From' : 
#         # print("Ignore")
#         continue
#     print(wds[2])



# # alt:
# for line in han:
#     line = line.rstrip()
#     # print("Line: ", line)
#     wds = line.split()
#     # print('Words: ', wds)
#     # guardian pattern
#     # if len(wds) < 1 : 
#     #     continue
#     # stronger:
#     if len(wds) < 3 : 
#         continue
#     if wds[0] != 'From' : 
#         # print("Ignore")
#         continue
#     print(wds[2])



# alt:
for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' : # if we flip this order, it'd fail (blow up) bc empty list has no index 0
        continue
    print(wds[2])


