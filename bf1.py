import pandas as pd
import statistics as stat
import math
import csv

df = pd.read_csv('movie_industry.csv', engine = 'python')

na = ['USA', 'Canada', 'Jamaica', 'Bahamas']
latina = ['Mexico', 'Argentina', 'Cuba', 'Peru', 'Brazil', 'Colombia', 'Chile', 'Panama']
eur = ['UK', 'Italy', 'France', 'Sweden', 'Spain', 'Switzerland', 'Netherlands', 'West Germany', 'Denmark', 'Ireland', 'Germany', 'Soviet Union', 'Belgium', 'Austria', 'Protugal', 'Republic of Macedonia', 'Russia', 'Greece', 'Norway', 'Romania', 'Federal Republic of Yugoslavia', 'Aruba', 'Czech Republic', 'Hungary', 'Finland', 'Poland', 'Ukraine', 'Iceland', 'Malta']
asia = ['Japan', 'Hong Kong', 'China', 'Taiwan', 'India', 'South Korea', 'Thailand', 'Indonesia']
africa = ['South Africa', 'Kenya']
mideast = ['Israel', 'Iran', 'Palestine', 'Saudi Arabia']
aus = ['Australia', 'New Zealand']
regionnames = ['North America', 'Latin America', 'Europe', 'Asia', 'Africa', 'Middle East', 'Australia']

def filterBudgets(blist):
    newlist = []
    for item in blist:
        if item != 0.0:
            newlist.append(item)
    return newlist

def sortbycountry(dataset):
    byCountryData = dataset.groupby('country')
    countries = dataset.country.unique()

    filmsByCountry = []

    for country in countries:
        data = byCountryData.get_group(country)
        filmsByCountry.append(data.reset_index())

    return filmsByCountry

def filter1000votes(dataset):
    isReviewed = dataset.loc[dataset['votes'] >= 1000]
    return isReviewed

def sortbyregion(dataset):
    byCountry = sortbycountry(filter1000votes(dataset))
    emptyData = {'budget' : [], 'company' : [], 'country' : [], 'director' : [], 'genre' : [], 'gross' : [], 'name' : [], 'rating' :[], 'released' : [], 'runtime' : [], 'score' : [], 'star' : [], 'votes' : [], 'writer' : [], 'year' : []}
    nadata = pd.DataFrame(emptyData)
    latinadata = pd.DataFrame(emptyData)
    eurdata = pd.DataFrame(emptyData)
    asiadata = pd.DataFrame(emptyData)
    africadata = pd.DataFrame(emptyData)
    mideastdata = pd.DataFrame(emptyData)
    ausdata = pd.DataFrame(emptyData)
    for data in byCountry:
        nation = data.country.unique()[0]
        if nation in na:
            nadata = pd.concat([data, nadata])
        if nation in latina:
            latinadata = pd.concat([data, latinadata])
        if nation in eur:
            eurdata = pd.concat([data, eurdata])
        if nation in asia:
            asiadata = pd.concat([data, asiadata])
        if nation in africa:
            africadata = pd.concat([data, africadata])
        if nation in mideast:
            mideastdata = pd.concat([data, mideastdata])
        if nation in aus:
            ausdata = pd.concat([data, ausdata])
    regList = [nadata, latinadata, eurdata, asiadata, africadata, mideastdata, ausdata]
    return regList

def analyzebyregion():
    sc = sortbyregion(df)
    data = {'region' : [], 'count' : [], 'meangross' : [], 'meanbudget' : [], 'totalgross' : [], 'meanrating' : []}
    for index, cd in enumerate(sc):
        data['region'].append(regionnames[index])
        data['count'].append(len(cd))
        data['meangross'].append(stat.mean(cd['gross']))
        try:
            data['meanbudget'].append(stat.mean(filterBudgets(cd['budget'])))
        except:
            data['meanbudget'].append(math.nan)
        data['totalgross'].append(sum(cd['gross']))
        data['meanrating'].append(stat.mean(cd['score']))

    regDF = pd.DataFrame(data)
    print(regDF)
    return regDF

def analyzebycountry():
    sc = sortbycountry(filter1000votes(df))
    data = {'country' : [], 'count' : [], 'meangross' : [], 'meanbudget' : [], 'totalgross' : [], 'meanrating' : []}

    for cd in sc:
        data['country'].append(cd.country.unique()[0])
        data['count'].append(len(cd))
        data['meangross'].append(stat.mean(cd['gross']))
        try:
            data['meanbudget'].append(stat.mean(filterBudgets(cd['budget'])))
        except Exception as e:
            data['meanbudget'].append(math.nan)
        data['totalgross'].append(sum(cd['gross']))
        data['meanrating'].append(stat.mean(cd['score']))

    nationDF = pd.DataFrame(data)
    print(nationDF)
    return nationDF

countries = analyzebycountry()
regions = analyzebyregion()

countries.to_csv('countrydata.csv')
regions.to_csv('regiondata.csv')