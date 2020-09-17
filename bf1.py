import csv
import pandas as pd
import statistics as stat

df = pd.read_csv('movie_industry.csv', engine = 'python')

na = ['USA', 'Canada', 'Jamaica', 'Bahamas']
latine = ['Mexico', 'Argentina', 'Cuba', 'Peru', 'Brazil', 'Colombia', 'Chile', 'Panama']
eur = ['UK', 'Italy', 'France', 'Sweden', 'Spain', 'Switzerland', 'Netherlands', 'West Germany', 'Denmark', 'Ireland', 'Germany', 'Soviet Union', 'Belgium', 'Austria', 'Protugal', 'Republic of Macedonia', 'Russia', 'Greece', 'Norway', 'Romania', 'Federal Republic of Yugoslavia', 'Aruba', 'Czech Republic', 'Hungary', 'Finland', 'Poland', 'Ukraine', 'Iceland', 'Malta']
asia = ['Japan', 'Hong Kong', 'China', 'Taiwan', 'India', 'South Korea', 'Thailand', 'Indonesia']
africa = ['South Africa', 'Kenya']
mideast = ['Israel', 'Iran', 'Palestine', 'Saudi Arabia']
aus = ['Australia', 'New Zealand']

def sortbycountry(dataset):
    byCountryData = dataset.groupby('country')
    countries = dataset.country.unique()

    filmsByCountry= []

    for country in countries:
        data = byCountryData.get_group(country)
        filmsByCountry.append(data.reset_index())

    return filmsByCountry

def filter1000votes(filmData):
    isReviewed = filmData.loc[filmData['votes'] >= 1000]
    return isReviewed

sc = sortbycountry(filter1000votes(df))
data = {'country' : [], 'count' : [], 'meangross' : [], 'meanbudget' : []}

for cd in sc:
    data['country'].append(cd.country.unique()[0])
    data['count'].append(len(cd))
    data['meangross'].append(stat.mean(cd['gross']))
    data['meanbudget'].append(stat.mean(cd['budget']))

nationDF = pd.DataFrame(data)
print(nationDF)