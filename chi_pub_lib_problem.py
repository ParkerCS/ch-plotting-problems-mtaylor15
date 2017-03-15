
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



file = open("chilib_vistors_2016")
reader = csv.reader(file, delimiter='\t')

library_list = []
places = []
for line in reader:
    library_list.append(line)

headers = library_list[0][1]
library_list = library_list[1:]
for i in range(len(library_list)):
    library_list[i].remove(library_list[i][0])

print(library_list)


months = []
for month in range(len(library_list[0])):
    total = 0
    for location in range(len(library_list)):
        total += int(library_list[location][month])
    months.append(total)

months.remove(months[12])

print(file)


three_most = []

file.close()

