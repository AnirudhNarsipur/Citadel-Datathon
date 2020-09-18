import pandas as pd
import statistics as stat
import math
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as stat

def calcRatio(value, gross):
    try: 
        return int(value) / int(gross)
    except:
        return np.nan

def subtract(us, gross):
    try: 
        return int(gross) - int(us)
    except:
        return np.nan

df = pd.read_csv('grossesbyregion.csv', engine = 'python')
df = df.replace('no data', np.nan)

# splitting up the dataset by year
def yearsplit(dataset):
    byYearData = dataset.groupby('year')
    years = dataset.year.unique()

    filmsByYear = []

    for year in years:
        data = byYearData.get_group(year)
        filmsByYear.append(data.reset_index())

    return filmsByYear

# splitting up the dataset by decade, removing years 1977-1979 and 2020 since they don't fit
def decadesplit(dataset):
    yearSplit = yearsplit(dataset)

    eighties = pd.DataFrame()
    nineties = pd.DataFrame()
    thousands = pd.DataFrame()
    tens = pd.DataFrame()

    for yeardata in yearSplit:
        year = int(yeardata['year'][0])
        if year >= 1980 and year <= 1989:
            eighties = pd.concat([yeardata, eighties])
        if year >= 1990 and year <= 1999:
            nineties = pd.concat([yeardata, nineties])
        if year >= 2000 and year <= 2009:
            thousands = pd.concat([yeardata, thousands])
        if year >= 2010 and year <= 2019:
            tens = pd.concat([yeardata, tens])
    
    return eighties, nineties, thousands, tens

# correlation matrix of regions
def correlation(dataset):
    countriesOnly = dataset.loc[:, 'USA' : 'China']
    countriesOnly = countriesOnly.apply(pd.to_numeric)

    correlation = countriesOnly.corr()
    sns.heatmap(correlation, xticklabels=correlation.columns,yticklabels=correlation.columns, annot=True)
    plt.show()
    print(correlation)
    return correlation

# convert dataframe to give percentage of total revenue by region 
def addPercentages(dataset):
    dataset['USA%'] = dataset.apply(lambda row: calcRatio(row['USA'], row['Total Gross']), axis =1)
    dataset['Europe, Middle East, and Africa%'] = dataset.apply(lambda row: calcRatio(row['Europe, Middle East, and Africa'], row['Total Gross']), axis =1)
    dataset['Latin America%'] = dataset.apply(lambda row: calcRatio(row['Latin America'], row['Total Gross']), axis =1)
    dataset['Asia Pacific%'] = dataset.apply(lambda row: calcRatio(row['Asia Pacific'], row['Total Gross']), axis =1)
    dataset['China%'] = dataset.apply(lambda row: calcRatio(row['China'], row['Total Gross']), axis =1)
    dataset['International%'] = dataset.apply(lambda row: 1- row['USA%'], axis = 1)
    return dataset

def sumsByYear(yeardataset):
    outputData = {}
    for (colname, coldata) in yeardataset[0].iteritems():
        if colname != 'index' and colname != 'title':
            outputData[colname] = []
    for yeardata in yeardataset:
        yeardata = yeardata.replace(np.nan, 0)
        yeardata = yeardata.loc[:, 'year' :]
        yeardata = yeardata.apply(pd.to_numeric)
        for (colname, coldata) in yeardata.iteritems():
            if colname == 'year':
                outputData[colname].append(stat.mean(coldata))
            elif colname != 'index' and colname != 'title':
                outputData[colname].append(sum(coldata))
    dataframe = pd.DataFrame(outputData)

    return dataframe

def sumsByDecade(decadedata):
    outputData = {}
    outputData['decade'] = ['1980s', '1990s', '2000s', '2010s']
    for (colname, coldata) in decadedata[0].iteritems():
        if colname != 'index' and colname != 'title' and colname != 'year':
            outputData[colname] = []
    for decade in decadedata:
        decade = decade.replace(np.nan, 0)
        decade = decade.drop('title', axis=1)
        decade = decade.apply(pd.to_numeric)
        for (colname, coldata) in decade.iteritems():
            if colname != 'index' and colname != 'title' and colname != 'year':
                outputData[colname].append(sum(coldata))
    dataframe = pd.DataFrame(outputData)
    return dataframe

# measure correlation between regions
correlation(df).to_csv("correlation-all.csv")

# look at the evolution of globalization
dfbyyear = yearsplit(df)
eigthies, nineties, thousands, tens = decadesplit(df)
decadelist = [eigthies, nineties, thousands, tens]

addPercentages(sumsByYear(dfbyyear)).to_csv("years.csv")
addPercentages(sumsByDecade(decadelist)).to_csv("decades.csv")

for index, decade in enumerate(decadelist):
    correlation(decade).to_csv('correlation-decade' + str(index))


