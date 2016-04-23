#In the following code cell, we configure the histograms so that they're displayed vertically on top of each other 
#(instead of on the same horizontal area) and hide the grid so the graphs are cleaner.

import matplotlib.pyplot as plt
columns = ['Median','Sample_size']
# Set the `layout` parameter as `(2,1)` so the graphs are displayed as 2 rows & 1 column 
# Then set `grid` parameter to `False`.
recent_grads.hist(column=columns, layout=(2,1), grid=False)


#Generate a histogram of just the Sample_size column using 50 bins instead of the default 10 and with the original grid preserved : .hist() 
recent_grads.hist(column="Sample_size", bins=50, grid=False)


#Generate a box plot for the values in the Total column, grouped by Major_category to match how we grouped the majors in our box plot for the Sample_size column.
recent_grads[['Total', 'Major_category']].boxplot(by='Major_category')
plt.xticks(rotation=90)

#To accomplish this, we can actually generate multiple plots on the same chart and look for any indication of correlation. 
#In the following code cell, we generate 2 scatter plots using the same y-axis but different x-axes and then use plt.show() afterwards to display 
#the 2 plots on the same chart. We then use the color parameter to plot each scatter plot using a different color so we can easily see the difference.
# Plot Unemployment_rate on x-axis, Median salary on y-axis, in red
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['Median'], color='red')
# Plot ShareWomen (Female % in major) on x-axis, Median salary on y-axis, in blue
plt.scatter(recent_grads['ShareWomen'], recent_grads['Median'], color='blue')
plt.show()


#Generate 2 scatter plots on the same chart, one for the Unemployment_rate and one for ShareWomen, both compared against the y-axis of the 25th percentile 
#salary ('P25th' column). The Unemployment_rate scatter plot should be in red while the ShareWomen plot should be in blue
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['P25th'], color='red')
plt.scatter(recent_grads['ShareWomen'], recent_grads['P25th'], color='blue')
plt.show()