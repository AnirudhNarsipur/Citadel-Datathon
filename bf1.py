import csv
import pandas as pd
import statistics as stat

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
        if item !== 0.0:
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
    nadata = pd.DataFrame()
    latinadata = pd.DataFrame()
    eurdata = pd.DataFrame()
    asiadata = pd.DataFrame()
    africadata = pd.DataFrame()
    mideastdata = pd.DataFrame()
    ausdata = pd.DataFrame()
    for data in byCountry:
        nation = data.country.unique()[0]
        if na.contains(nation):
            nadata = pd.concat(nadata, data)
        if latina.contains(nation):
            latinadata = pd.concat(latinadata, data)
        if eur.contains(nation):
            eurdata = pd.concat(eurdata, data)
        if asia.contains(nation):
            asiadata = pd.concat(asiadata, data)
        if africa.contains(nation):
            africadata = pd.concat(africadata, data)
        if aus.contains(nation):
            ausdata = pd.concat(ausdata, data)
    regList = [nadata, latinadata, eurdata, asiadata, africadata, mideastdata, ausdata]
    return regList

def analyzebyregion():
    sc = sortbyregion(dataset)
    data = {'region' : [], 'count' : [], 'meangross' : [], 'meanbudget' : [], 'totalgross' : []}

    for index, cd in enumerate(sc):
        data['region'].append(regionnames[index])
        data['count'].append(len(cd))
        data['meangross'].append(stat.mean(cd['gross']))
        try:
            data['meanbudget'].append(stat.mean(filterBudget(cd['budget'])))
        except:
            data['meanbudget'].append(math.nan)
        data['totalgross'].append(stat.sum(cd['gross']))

    regDF = pd.DataFrame(data)
    print(regDF)
    return regDF

def analyzebycountry():
    sc = sortbycountry(filter1000votes(df))
    data = {'country' : [], 'count' : [], 'meangross' : [], 'meanbudget' : [], 'totalgross' : []}

    for cd in sc:
        data['country'].append(cd.country.unique()[0])
        data['count'].append(len(cd))
        data['meangross'].append(stat.mean(cd['gross']))
        try:
            data['meanbudget'].append(stat.mean(filterBudget(cd['budget'])))
        except:
            data['meanbudget'].append(math.nan)
        data['totalgross'].append(stat.sum(cd['gross']))

    nationDF = pd.DataFrame(data)
    print(nationDF)
    return nationDF


analyzebycountry()
analyzebyregion()