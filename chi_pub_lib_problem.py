
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv


def split_line(line):
    return re.findall('[A-Za-z0-9]+(?:\'[A-Za-a0-9]+)?', line)


library_list = []
file = open("chilib_vistors_2016")
reader = csv.reader(file, delimiter='\t')
for line in reader:
    library_list.append(line)

headers = library_list[0]
library_list = library_list[1:]

print(file)

for line in file:
    words = split_line(line)
    library_list.append(words)
print(library_list)



