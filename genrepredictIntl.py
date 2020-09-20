import pandas as pd

def pickleSave(object, file):
    with open(file, 'wb') as handle:
        pickle.dump(object, handle, pickle.HIGHEST_PROTOCOL)

def unPickle(file):
    with open(file, 'rb') as handle:
        obj = pickle.load(handle)
    return obj

df = pd.read_csv("newerfile2.csv")
df.drop('title', axis=1)
df.drop('tags', axis=1)

allgen = set()

for index, row in df.iterrows():
    try:
        allgen.update(row['genres'].split("|"))
    except:
        a = 0
    print(index)

genlistlist = []

for genre in allgen:
    genlist = []
    for index, row in df.iterrows():
        print(index)
        try:
            if genre in row['genres'].split("|"):
                genlist.append(1)
            else:
                genlist.append(0)
        except:
            genlist.append(0)

    genlistlist.append(genlist)

pickleSave(genlistlist, 'genlistlist.pickle')