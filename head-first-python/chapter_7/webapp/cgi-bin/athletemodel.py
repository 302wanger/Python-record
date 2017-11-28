import pickle

from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print('File error: ' + str (ioerr))
        return(None)

def put_to_store(files_list):

    all_athletes = {}
    for each_file in files_list:
        # Takes each file , turn it into an AthleteList object instance, and add the athlete's
        # data to the dictionary
        ath = get_coach_data(each_file)
        # Each athlete's name is used as the "key" in the dictionary.
        # The "value" is the AthleteList object instance
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            #Save the entire dictionary of AthleteList to a pickle
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        # And don't forget a try/except to protect your file I/O code
        print("File error (put_and_store):" + str(ioerr))

    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            # Simply read the entire picke into the dictionary. What could be easier?
            all_athletes = pickle.load(athf)

    except IOError as ioerr:
        # Again... don't forget your try/except
        print("File error (get_from_store):" + str(ioerr))

    return(all_athletes)
