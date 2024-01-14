import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def recomand(mov):
	try:
		data = pd.read_csv("../top10K-TMDB-movies.csv")

		ndata = data[['id','title','genre','overview']]
		finalData = ndata
		finalData['tags'] = ndata['genre'] + ndata['overview']
		finalData = ndata.drop(columns=['genre', 'overview'])

		cv = CountVectorizer(max_features = 10000)

		vector = cv.fit_transform(finalData['tags'].values.astype("U")).toarray()
		sim = cosine_similarity(vector)

		index = finalData[finalData['title']== mov].index[0]


		dist = sorted(list(enumerate(sim[index])), reverse=True,key = lambda vector:vector[1])
		for i in dist[0:5]:
		  print(finalData.iloc[i[0]].title)
	except Exception as e:
		print("Enter correct movie name")
	else:
		pass
	finally:
		pass
  

mov = input("Enter Movie name: ")
recomand(mov)