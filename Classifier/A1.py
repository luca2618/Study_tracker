import pandas as pd
import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter("ignore")

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import word_tokenize
import string



#Tokenizer with added lemmatization and stemming options
class My_Tokenizer(object):
    def __init__(self, lemma=False, stem=False):
        self.lemma = lemma
        self.stem = stem
        self.Lemmatizer = WordNetLemmatizer()
        self.Stemmer = PorterStemmer()
        self.translate_table = dict((ord(char), None) for char in string.punctuation)  
    def __call__(self, sentence):
        #remove punctuation
        sentence = sentence.translate(self.translate_table)
        if self.lemma:
            return [self.Lemmatizer.lemmatize(t) for t in word_tokenize(sentence)]
        elif self.stem:
            return [self.Stemmer.stem(t) for t in word_tokenize(sentence)]
        else:
            return [t for t in word_tokenize(sentence)]
    

        
#seperator mean nothing here, we have a new point in each line, 
#so the seperator should just not show up in any sentence.
fakes = pd.read_csv("fakes.txt", sep="EOS", header=None)[0].to_numpy()
facts = pd.read_csv("facts.txt", sep="EOS", header=None)[0].to_numpy()

X = np.append(facts, fakes)
Y = np.array(["fact"]*len(facts))
Y = np.append(Y,["fake"]*len(fakes))
#split into train and test dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=42)
#split training set into validation and hyperparameter selection training set.
X_sel, X_val, Y_sel, Y_val = train_test_split(X_train, Y_train, test_size=0.15, random_state=42)
#Preprocessing methods
method1 = TfidfVectorizer(tokenizer=My_Tokenizer(),stop_words="english", lowercase=True, strip_accents="unicode") 
method2 = TfidfVectorizer(tokenizer=My_Tokenizer(stem=True),stop_words="english", lowercase=True, strip_accents="unicode")
method3 = TfidfVectorizer(tokenizer=My_Tokenizer(lemma=True),stop_words="english", lowercase=True, strip_accents="unicode")
dataset_methods = [method1, method2, method3]
print(dataset_methods)


# Define the outer and inner cross-validation splits
outer_cv = KFold(n_splits=5, shuffle=True, random_state=5)
inner_cv = KFold(n_splits=3, shuffle=True, random_state=5)

# Define the hyperparameters you want to tune, including preprocessing steps.
#change the parameters depending on the classifier here:
param_grid = {
    'preprocessing': [method1, method2, method3],
    'classifier__C': [10**t for t in range(-5,5)], #use this for Logistic and SVM classicfier
    #'classifier__alpha': [10**t for t in range(-1000,0,100)], #use this for Perceptron classicfier
}

# Create a pipeline with preprocessing and classifier steps
pipeline = Pipeline([
    ('preprocessing', None),  # This will be replaced by different preprocessing methods
    ('classifier', LinearSVC()) # change model here!, but also change model paramters accordingly! SVC and logistic use C for regulization, but Perceptron uses the alpha parameter.
])


# Initialize the outer cross-validation loop
outer_scores = []

for train_outer_idx, test_outer_idx in outer_cv.split(X):
    X_train_outer, X_test_outer = X[train_outer_idx], X[test_outer_idx]
    y_train_outer, y_test_outer = Y[train_outer_idx], Y[test_outer_idx]

    # Initialize the inner cross-validation loop for hyperparameter tuning
    clf = GridSearchCV(estimator=pipeline, param_grid=param_grid, cv=inner_cv)
    
    # Fit the classifier on the inner training data to find the best hyperparameters
    clf.fit(X_train_outer, y_train_outer)
    
    # Use the best hyperparameters to train the model on the outer training data
    best_params = clf.best_params_
    best_estimator = clf.best_estimator_
    best_estimator.fit(X_train_outer, y_train_outer)
    
    # Evaluate the model on the outer test data
    outer_score = best_estimator.score(X_test_outer, y_test_outer)
    print(best_params)
    print(f"Fold Accuracy: {outer_score:.3f}")
    outer_scores.append(outer_score)

# Calculate and print the final cross-validation score
mean_score = np.mean(outer_scores)
print(f"Mean Accuracy: {mean_score:.3f}")
CI = [mean_score-1.96*math.sqrt(mean_score*(1-mean_score))/math.sqrt(len(Y)),mean_score+1.96*1.96*math.sqrt(mean_score*(1-mean_score))/math.sqrt(len(Y))]
print(CI)
