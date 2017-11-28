# use this module to make data more useful
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
# use this module to deal data file
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:'+ str(ioerr))
        return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')


clean_james = set([sanitize(each_t) for each_t in james])
clean_julie = set([sanitize(each_t) for each_t in julie])
clean_mikey = set([sanitize(each_t) for each_t in mikey])
clean_sarah = set([sanitize(each_t) for each_t in sarah])



print(sorted(clean_james)[0:3])
print(sorted(clean_julie)[0:3])
print(sorted(clean_mikey)[0:3])
print(sorted(clean_sarah)[0:3])
