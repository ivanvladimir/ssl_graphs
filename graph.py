import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.lines import Line2D
df=pd.read_csv("data/SSL_analysis.csv")

def myLogFormat(y,pos):
    decimalplaces = int(np.maximum(-np.log10(y),0))     # =0 for numbers >=1
    formatstring = '{{:.{:1d}f}}'.format(decimalplaces)
    return formatstring.format(y)


markers = ['o','v','8','s','<','p','^','h','>','D']

geometry=df['Array Geometry'].unique()

cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, len(geometry))]

df1=df.groupby(['Year','Number of microphones']).size().reset_index(name='count')

volumen=[ (20*x)^2 for x in df1['count']]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df1['Year'],df1['Number of microphones'], s=volumen)
ax.set_yscale('log')
ax.set_xlim([1988,2018])
ax.set_ylim([0.9,72])
ax.set_yticks([1,2,3,4,8,16,32,64])
ax.yaxis.set_major_formatter(ticker.FuncFormatter(myLogFormat))
plt.legend(loc=2)
plt.show()

df1=df.groupby(['Year','Number of sources located in practice']).size().reset_index(name='count')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df1['Year'],df1['Number of sources located in practice'], s=volumen)
ax.set_xlim([1988,2018])
ax.set_ylim([0,8])
ax.set_yticks([0,1,2,3,4,5,6,7,8])
#ax.yaxis.set_major_formatter(ticker.FuncFormatter(myLogFormat))
plt.legend(loc=2)
plt.show()


print df['Maximum distance to source in practice'].unique()

df1=df.groupby(['Year','Maximum distance to source in practice']).size().reset_index(name='count')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df1['Year'],df1['Maximum distance to source in practice'], s=volumen)
ax.set_xlim([1988,2018])
ax.set_ylim([0,8])
ax.set_yticks([0,1,2,3,4,5,6,7,8])
#ax.yaxis.set_major_formatter(ticker.FuncFormatter(myLogFormat))
plt.legend(loc=2)
plt.show()
