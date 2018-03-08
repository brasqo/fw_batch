import csv
import os

# set the start, middle, and end parts of the string.
netsh_begin = "netsh advfirewall firewall add rule name="
netsh_mid = " dir=in action=allow program="
netsh_end = " enable=yes"
quote = '"'
hillsfilecsv = "PATH_TO_CSV_FILE"

# create a new txt file, append the data to the created file.
NewFile = open("NEW_BATCH_FILE_NAME.bat","a" )


# change directory to path of the original file
os.chdir(r"PATH_TO_ORIGINAL_CSV_FILE")

# open the csv, read it as text, and create an object of it
with open('NAME_OF_THE_CSV.csv', 'rt') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')

   # set row counter to 0
    rownum = 0

    # loop thru the csv, label the two cols w/ their respected names (name/path)
    for row in filereader:
        name = str(row[0])
        path = str(row[1])
        # print the formatted string.
        # print(netsh_begin + '"' + name + '"' + netsh_mid + '"' + path + '"' + netsh_end)
        output = ('{}{}{}{}{}{}{}{}{}'.format(netsh_begin, quote, name, quote, netsh_mid, quote, path, quote, netsh_end))

        # write the output to the file, each line on a new line.
        NewFile.write(output + "\n")
