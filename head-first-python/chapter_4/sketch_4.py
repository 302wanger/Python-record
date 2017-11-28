man = []
other = []
# use try...excpet to think more conditon
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing!')


try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt','w')

    print(man, file=man_file) # use print to let man's content into man_file
    print(other, file=other_file)


except IOError:
    print('File error.')

# make sure to close file no matter what happened
finally:
    man_file.close()
    other_file.close()
    



    

