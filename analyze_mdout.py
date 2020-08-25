import os
import argparse


#to open the file for reading
# tell argparse to handle arguments
parser = argparse.ArgumentParser(description="parsers amber mdout files to extract total energy.")
#Tell argparse what argument to expect
parser.add_argument("path", help="The filepath to the file.")
#Get arguments from the user
args = parser.parse_args()

filename = args.path
f = open(filename, 'r') # r is for open the file FOR reading

# then read data in the file
data = f.readlines()
f.close()
#once you read the data, you close the file

#open a file for writing
base_filename = filename.split('.')[0]
output_filename = F'{base_filename}_Etot.txt'

f_write = open(output_filename, 'w+') # this will create a new file with name
print(F'Writing output to {output_filename}')
f_write.write('Total Energy\n')
etot = []

# loop through lines in the file
for line in data:
    split_line = line.split()
    # get info from line
    if 'Etot' in line:
        # Write info into file
        etot.append(split_line[2])
etot = etot[:-2]
for energy in etot:
    f_write.write(F"{energy}\n")

      
f_write.close()

