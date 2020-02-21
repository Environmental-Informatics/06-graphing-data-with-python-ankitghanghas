""""
Created on 2020-02-21 Friday
Creator: Ankit Ghanghas

makeplots.py

This Script takes input and output file name from the command line and makes a plot with three subplots and saves the result as the output file specified by the user.
The first plot is year vs streamflow indicating mean flow with black line, max flow with red line and min flow with blue line.
the second plot is between Tqmean and year
the third subplot is a bar plot of R-B Index (ratio) across different years

"""
import numpy as np
import matplotlib.pyplot as plt
import sys

in1=str(sys.argv[1]) # converts the first system argument to str and stores it for input
out=str(sys.argv[2])# converts the second system argument to string and stores it for output
data=np.genfromtxt(in1, names=True, delimiter='\t') # this command creates np array of data while selecting column names from first row of input data and deliminates data based on tab

plt.figure() # creates an empty pyplot figure
plt.subplot(311) # accesse first pyplot of the three on x axis
plt.plot(data['Year'],data['Mean'], 'k-', data['Year'], data['Max'], 'r-', data['Year'], data['Min'], 'b-') # makes three lines with first entry as x (here data['Year']) second as y (here data['Mean'] for first line) and 'k-' specifies color of this line as black (k) and solid line (specified by '-'). Similarly 'r-' specifies solid red line
plt.ylabel('Streamflow(cfs)') # specifies the ylabel for this subplot
plt.legend(('Mean Flow','Max Flow','Min Flow'), loc = 'upper right') # creates legend in the upper right corner

plt.subplot(312)
plt.plot(data['Year'],data['Tqmean']*100)
plt.ylabel('Tqmean(%)')

plt.subplot(313)
plt.bar(data['Year'], data['RBindex'])
plt.ylabel('R-B Index(ratio)')
plt.xlabel('Year')
plt.savefig(out) # saves the figure by the specified name
plt.close() # closes the figure
