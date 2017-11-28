def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


# inherit a lot of way from list module
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temple = data.strip().split(',')
        return(AthleteList(temple.pop(0),temple.pop(0),temple))
    except IOError as ioerr:
        print('File errror: '+ str(ioerr))
        return(None)


sarah = get_coach_data('coach2.txt')

print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
