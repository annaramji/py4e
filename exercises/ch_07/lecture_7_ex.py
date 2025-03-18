# fhand = open('code3/mbox.txt')
# print(fhand)


# stuff = 'Hello\nWorld!'
# print(stuff)


# stuff = 'X\nY'
# print(stuff)
# print(len(stuff))


# xfile = open('code3/mbox.txt')
# for cheese in xfile:
#     print(cheese)

# fhand = open('code3/mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)

# fhand = open('code3/mbox-short.txt')
# inp = fhand.read() # doesn't split the lines (one big blob of text), turns all characters into a string
# print(len(inp)) # n characters
# print(inp[:20]) # first 20 characters


# fhand = open('code3/mbox-short.txt')
# for line in fhand: # for each line in the file
#     if line.startswith('From:'): # if the line starts with 'From:'
#         print(line) # adds an extra line between each line
#         ## two new lines (1 from text from file, print statement adds another)

# # updated:
# fhand = open('code3/mbox-short.txt')
# for line in fhand: # for each line in the file
#     line = line.rstrip() # removes the extra whitespace at the end of the line
#     if line.startswith('From:'): # if the line starts with 'From:'
#         print(line) # adds an extra line between each line
#         ## two new lines (1 from text from file, print statement adds another)


# # skipping with continue
# fhand = open('code3/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue # skips the rest of the loop and goes to the next iteration
#     print(line)


# # # example: using "in" to Select Lines
# fhand = open('code3/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not '@uct.ac.za' in line:
#         continue
#     print(line)


# # prompt for file name
# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# # updated: deal with Bad File Names
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     quit() # stop continuing (don't go into for loop if fhand isn't properly defined)

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

# test for assignment
fname = input("Enter file name: ")
fh = open(fname)

# print the contents of the file in uppercase
for line in fh:
    print(line.upper().rstrip())