# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mkYOqJXsEzFyjzqKm_vOF0je7b4zwD4j
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import re
import string
import nltk
from nltk.corpus import stopwords
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from nltk.tokenize import word_tokenize,RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from platform import python_version
print (python_version())
nltk.download('stopwords')
nltk.download('wordnet')

import pandas as pd
from datetime import datetime
now = datetime.now()

df = pd.read_csv("/content/tweets.xls")
split_percent = 0.7
df_length = int(len(df)*split_percent)
train_df = df.iloc[:df_length,:]
test_df = df.iloc[df_length:,:]
train_df.to_csv("train.csv")
test_df.to_csv("test.csv")

print(len(train_df))
print(len(test_df))

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words

def pre_process_text_combined(text):
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
    cleaned_txt = clean_text(text)
    tokenized_text = tokenizer.tokenize(cleaned_txt)
    remove_stopwords = [w for w in tokenized_text if w not in stopwords.words('english')]
    combined_text = ' '.join(remove_stopwords)
    return  combined_text

train_df2=train_df.copy()
train_df2['text'] = train_df2['text'].apply(lambda x : pre_process_text_combined(x))

test_df2=test_df.copy()
test_df2['text'] = test_df2['text'].apply(lambda x : pre_process_text_combined(x))

count_vectorizer = CountVectorizer()
train_cv = count_vectorizer.fit_transform(train_df2['text'])
test_cv = count_vectorizer.transform(test_df2["text"])

tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1, 2))
train_tf = tfidf.fit_transform(train_df2['text'])
test_tf = tfidf.transform(test_df2["text"])

X_train_cv, X_test_cv, y_train_cv, y_test_cv =train_test_split(train_cv,train_df.target,test_size=0.2,random_state=2020)

# Fitting 'LogisticRegression()' with CountVectorizer() fit dataset
clf_logreg = LogisticRegression(C=1.0)
clf_logreg.fit(X_train_cv, y_train_cv)
pred=clf_logreg.predict(X_test_cv)
confusion_matrix(y_test_cv,pred)
print(classification_report(y_test_cv,pred))
print('Accuracy of classifier on training set:{}%'.format(round(clf_logreg.score(X_train_cv, y_train_cv)*100)))
print('Accuracy of classifier on test set:{}%' .format(round(accuracy_score(y_test_cv,pred)*100)))

# Tempo di esecuzione
print(datetime.now() - now)