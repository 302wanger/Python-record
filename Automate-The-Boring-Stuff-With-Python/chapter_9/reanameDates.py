#1 python3
# reanameDates.py  -Rename filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the american date format.
datePattern = re.compile(r"""^(.*?)           # all text before the date
    ((0|1)?\d) -                              # one or two digits for the month
    ((0|1|2|3)?\d) -                          # one or two digits for the day
    ((19|20)\d\d)                             # four digits for the year
    (.*?)$
    """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

# TODO: Skip files without a date.
    if mo == None:
        continue
# TODO: Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
# TODO: Form the European-style filename.

# TODO: Get the full, absoulte file paths.

# TODO: Rename the files.
