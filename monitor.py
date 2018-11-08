import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv

#Set some constants
DATA_DIR = './data/'
DATA_FILE_IN = 'cch_profile.csv'
DATA_FILE_OUT = 'tratado.csv'
SEPARATOR = ';'
##################################################


df = read_csv(DATA_DIR + DATA_FILE_IN, sep=SEPARATOR)
#a = np.average(df['value'])


df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
df['day']   = pd.DatetimeIndex(df['date']).day
df['hour']   = pd.DatetimeIndex(df['date']).hour
df['dayofweek']   = pd.DatetimeIndex(df['date']).dayofweek
df['quarter']   = pd.DatetimeIndex(df['date']).quarter

conditions = [
     (df['hour'] >=0 ) & (df['hour'] <=12),
     (df['hour'] > 12) & (df['hour'] < 23),
     (df['hour'] == 23 )]
choices = ['valle', 'pico', 'valle']
#df['vallepico'] = np.where(df['hour']==0, 'valle', 'pico')
df['vallepico'] = np.select(conditions, choices, default='valle')

df.to_csv(DATA_DIR + DATA_FILE_OUT, SEPARATOR)

# 2. Agrupaciones
group_means = df.groupby('month')['value'].apply(np.sum)
group_means2 = df.groupby('vallepico')['value'].apply(np.sum)
group_means3 = df.groupby(['month', 'vallepico'])['value'].apply(np.sum)

print ("Por Mes")
print group_means
print group_means3

plt.figure()
group_means.plot()
plt.show()

plt.figure()
group_means3.plot.bar()
plt.show()

#print ("Por VallePico")

#print ("Por mes/vallepico")
#print group_means3

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# group_means2 = group_means2.reset_index()

# plt.plot(group_means['month'],group_means['value'])
# plt.plot(group_means2['vallepico'],group_means2['value'])
# plt.show()

#plt.show()
# if (df['hour'] > 0):  
# 	esvalle = 'si'
# else:
# 	esvalle = 'no'

# df['vallepico'] = esvalle

#print(group_means)

#print(df)
#print(a)

__init__

