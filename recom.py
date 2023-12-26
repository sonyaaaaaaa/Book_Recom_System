import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_data(x):
	return str.lower(x.replace(" ", ""))

def create_soup(x):
	return x['original_title']+ ' ' + x['authors'] + ' ' + x['average_rating']
	
def get_recommendations_new(title):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(fbooks['soup'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    title=title.replace(' ','').lower()
    idx = indices[title]

    # Получим оценки парного сходства всех книг с этой книгой
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Отсортируем книги по показателям сходства
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Получим оценки 10 самых похожих книг
    sim_scores = sim_scores[1:15]

    # Получим индексы книг
    book_indices = [i[0] for i in sim_scores]

    # Выведем топ-10 самых похожих книг
    return list(books['original_title'].iloc[book_indices])
	
books=pd.read_csv(r"D:\univer\3course\Proj_Books_Recom\books.csv")
books=books.dropna()

features=['original_title','authors','average_rating']
fbooks=books[features]
fbooks = fbooks.astype(str)
for feature in features:
    fbooks[feature] = fbooks[feature].apply(clean_data)

fbooks['soup'] = fbooks.apply(create_soup, axis=1)

fbooks=fbooks.reset_index()
indices = pd.Series(fbooks.index, index=fbooks['original_title'])




