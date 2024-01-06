import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
import seaborn as sns

files = glob.glob("states*.csv")

files_list = []

for file in files: 
  data = pd.read_csv(file)
  files_list.append(data)

us_census = pd.concat(files_list)

print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)

us_census['Income'] = us_census['Income'].replace('[\$,]', '', regex=True)
us_census['Income'] = pd.to_numeric(us_census['Income'])

genderpop_split = us_census['GenderPop'].str.split('_')
print(genderpop_split)
us_census['Men'] = genderpop_split.str.get(0)
us_census['Women'] = genderpop_split.str.get(1)
us_census['Men'] = us_census['Men'].str[:-1]
us_census['Women'] = us_census['Women'].str[:-1]
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])


plt.scatter(us_census['Men'], us_census['Women'])
plt.show()

us_census = us_census.fillna(value={'Women': us_census['TotalPop'] - us_census['Men']})
print(us_census['Women'])


duplicates = us_census.duplicated()
print(duplicates)
print(duplicates.value_counts())
us_census = us_census.drop_duplicates()


plt.scatter(us_census['Men'], us_census['Women'])
plt.show()

print(us_census.head())

print(us_census.columns)
us_census['Hispanic'] = pd.to_numeric(us_census['Hispanic'].str[:-1])
us_census['White'] = pd.to_numeric(us_census['White'].str[:-1])
us_census['Black'] = pd.to_numeric(us_census['Black'].str[:-1])
us_census['Native'] = pd.to_numeric(us_census['Native'].str[:-1])
us_census['Asian'] = pd.to_numeric(us_census['Asian'].str[:-1])
us_census['Pacific'] = pd.to_numeric(us_census['Pacific'].str[:-1])
print(us_census.dtypes)
print(us_census.head())

us_census = us_census.fillna(value={'Hispanic': us_census['Hispanic'].mean(), 'White': us_census['White'].mean(), 'Black': us_census['Black'].mean(), 'Native': us_census['Native'].mean(), 'Asian': us_census['Asian'].mean(), 'Pacific': us_census['Pacific'].mean()})

plt.hist(us_census['Hispanic'])
plt.show()
plt.clf()

plt.hist(us_census['White'])
plt.show()
plt.clf()

plt.hist(us_census['Black'])
plt.show()
plt.clf()

plt.hist(us_census['Native'])
plt.show()
plt.clf()

plt.hist(us_census['Asian'])
plt.show()
plt.clf()

plt.hist(us_census['Pacific'])
plt.show()
plt.clf()

sns.scatterplot(data=us_census, x='Asian', y='TotalPop')
plt.show()
plt.clf()




