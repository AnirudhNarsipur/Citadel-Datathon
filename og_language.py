import requests
import pandas as pd
from datetime import datetime
import pickle

def get_countries(tmdb_id):
	try:
		response = requests.get(f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=d333b0beea92fd2559700fcd8e657b16&language=en-US")
		json = response.json()
		return json["original_language"]
	except Exception as e:
		print(e)
		return ""

start_index = 19400

links = pd.read_csv("links.csv")

lang_dict = pickle.load(open(f"lang_dict-{start_index}.pkl", "rb"))

start_time = datetime.now()

for i, tmdb_id in enumerate(links["tmdbId"]):
	if i > start_index:
		if i % 100 == 0 and i != 0:
			print(i, datetime.now() - start_time)
			start_time = datetime.now()
			with open(f"lang_dict-{i}.pkl", "wb") as f:
				pickle.dump(lang_dict, f)
		lang_dict[tmdb_id] = get_countries(tmdb_id)


with open("lang_dict.pkl", "wb") as f:
	pickle.dump(lang_dict, f)