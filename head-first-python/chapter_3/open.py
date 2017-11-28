import os

data = open('sketch.txt')
# print first line
print(data.readline(), end='')
# print second line
print(data.readline(), end='')

# return to first line
data.seek(0)

# print every line in the file
for each_line in data:
    print(each_line, end='')


# close the file
data.close()
