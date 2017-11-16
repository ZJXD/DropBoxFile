'''
# Make a pie chart
# This script is written by Vamei, http://www.cnblogs.com/vamei
# you may freely use it.

import matplotlib.pyplot as plt
# quants: GDP
# labels: country name
labels   = []
quants   = []
# Read data
for line in open('./data/major_country_gdp.txt'):
    info = line.split()
    labels.append(info[0])
    quants.append(float(info[1]))

# make a square figure
plt.figure(1, figsize=(6,6))


# For China, make the piece explode a bit
def explode(label, target='China'):
    if label == target: return 0.1
    else: return 0
expl = list(map(explode,labels))
# Colors used. Recycle if not enough.
colors  = ["pink","coral","yellow","orange"]
# Pie Plot
# autopct: format of "percent" string;
plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
plt.title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})

plt.show()
'''

'''
Make a pie chart
This script is written by Vamei, http://www.cnblogs.com/vamei
you may freely use it.
'''

import matplotlib.pyplot as plt
import numpy as np
# quants: GDP
# labels: country name
labels   = []
quants   = []
# Read data
for line in open('./data/major_country_gdp.txt'):
    info = line.split()
    labels.append(info[0])
    quants.append(float(info[1]))

width = 0.4
ind = np.linspace(0.5,9.5,10)
# make a square figure
fig = plt.figure(1, figsize=(12,6))
ax  = fig.add_subplot(111)
# Bar Plot
ax.bar(ind-width/2,quants,width,color='coral')

# Set the ticks on x-axis
ax.set_xticks(ind)
ax.set_xticklabels(labels)
# labels
ax.set_xlabel('Country')
ax.set_ylabel('GDP (Billion US dollar)')
# title
ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
plt.show()

