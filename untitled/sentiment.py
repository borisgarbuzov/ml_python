from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import os
import re
import nltk


basepath = './aclImdb_short'

labels = {'pos':1, 'neg':0}
df = pd.DataFrame()
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = os.path.join(basepath, s, l)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]], ignore_index=True)
df.columns = ['review', 'sentiment']

np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
print("df = \n", df)

df.to_csv('./movie_data.csv', index=False)

df = pd.read_csv('./movie_data.csv')
df.head(3)

count = CountVectorizer(ngram_range=(1,1))
docs = np.array([
        'The sun is shining',
        'The weather is sweet',
        'The sun is shining and the weather is sweet'])
bag = count.fit_transform(docs)
print("bag = \n", bag)

print(count.vocabulary_)

print(bag.toarray())

np.set_printoptions(precision=2)

tfidf = TfidfTransformer(use_idf=True, norm='l2', smooth_idf=True)
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())

tf_is = 2
n_docs = 3
idf_is = np.log((n_docs+1) / (3+1) )
tfidf_is = tf_is * (idf_is + 1)
print('tf-idf of term "is" = %.2f' % tfidf_is)

tfidf = TfidfTransformer(use_idf=True, norm=None, smooth_idf=True)
raw_tfidf = tfidf.fit_transform(count.fit_transform(docs)).toarray()[-1]
print(raw_tfidf)
raw_tfidf_all = tfidf.fit_transform(count.fit_transform(docs)).toarray()
print ("raw_tfidf_all =\n", raw_tfidf_all)

l2_tfidf = raw_tfidf / np.sqrt(np.sum(raw_tfidf**2))
print(l2_tfidf)

print(df.loc[0, 'review'][-50:])


def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + \
           ' '.join(emoticons).replace('-', '')
    return text

print(preprocessor(df.loc[0, 'review'][-50:]))

print(preprocessor("</a>This :) is :( a test :-)!, Я його з'їв."))

print("before preprocessing:\n", df.head())
df['review'] = df['review'].apply(preprocessor)
print("after preprocessing")
print(df.head())

porter = PorterStemmer()

def tokenizer(text):
    return text.split()

def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]

tokenizer('runners like running and thus they run')
ukrText = "</a>This :) is :( a test :-)!, Я його з'їв."
print(tokenizer(ukrText))

tokenizer_porter('runners like running and thus they run')
print(tokenizer_porter(ukrText))

nltk.download('stopwords')

stop = stopwords.words('english')
print("len =", len(stop))
print("stop =\n", stop)

myPorter = tokenizer_porter('a runner likes running and runs a lot')
print("myPorter =\n", myPorter)

lexemmas = []
for word in myPorter:
    if word not in stop:
        lexemmas.append(word)
print("full cycle lexemmas =\n", lexemmas)

lexemmasMinus10 = [w for w in
                   tokenizer_porter('a runner likes running and runs a lot')
                   [-10:] if w not in stop]
print("lexemmasMinus10 =", lexemmasMinus10)

print("no -10 =")
without_stop = [w for w in tokenizer_porter('a runner likes running and runs a lot') if w not in stop]
print(without_stop)

X_train = df.loc[:19, 'review'].values
y_train = df.loc[:19, 'sentiment'].values
X_test = df.loc[20:, 'review'].values
y_test = df.loc[20:, 'sentiment'].values

tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None)

param_grid = [{'vect__ngram_range': [(1,1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
             {'vect__ngram_range': [(1,1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__use_idf':[False],
               'vect__norm':[None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
             ]

lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=0, solver='liblinear'))])

gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5, verbose=1,
                           n_jobs=-1)

gs_lr_tfidf.fit(X_train, y_train)

print('Best parameter set: %s ' % gs_lr_tfidf.best_params_)
print('CV Accuracy: %.3f' % gs_lr_tfidf.best_score_)

clf = gs_lr_tfidf.best_estimator_
print('Test Accuracy: %.3f' % clf.score(X_test, y_test))