# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

# Enter file name: mbox-short.txt
# fn = input("Enter file name: ")
# try:
#     fh = open(fn)
# except:
#     print("File cannot be opened:", fn)
#     quit()

# for line in fh:
#     print(line.upper().rstrip())




# # 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# # X-DSPAM-Confidence:    0.8475
# # Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# # Do not use the sum() function or a variable named sum in your solution.

# # Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)

# count = 0
# total_values = 0

# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     count += 1
#     ipos = line.find(":")
#     piece = line[ipos+2:]
#     value = float(piece)
#     total_values = total_values + value

# average = total_values / count
# print("Average spam confidence:", average)

