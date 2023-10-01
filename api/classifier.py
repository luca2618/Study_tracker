import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
import warnings
warnings.simplefilter("ignore")
import pickle
from nltk.corpus import stopwords
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
        self.stopwords = stopwords.words('english')
    def __call__(self, sentence):
        sentence = sentence.translate(self.translate_table)
        if self.lemma:
            return [self.Lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence) if not word.lower() in self.stopwords]
        elif self.stem:
            return [self.Stemmer.stem(word.lower()) for word in word_tokenize(sentence) if not word.lower() in self.stopwords]
        else:
            return [word.lower() for word in word_tokenize(sentence) if not word.lower() in self.stopwords]

class glove():
    def __init__(self) -> None:
        #self.glove = glove_loaded
        with open('glove.pickle', 'rb') as f:
            self.glove = pickle.load(f)
            f.close()
        self.tokenizer = My_Tokenizer()
    def fit():
        pass
    def fit_transform(self, data):
        return self.transform(data)
    def transform(self, data):
        results = []
        for document in data:
            document = self.tokenizer(document)
            vector = np.zeros(300)
            for word in document:
                if word in self.glove:
                    vector += self.glove[word]
            results.append(vector)
        results = np.array(results)
        return results


#dataset = pd.read_csv("./api/dataset.csv")

#X = dataset["X"].to_numpy()
#Y = dataset["Y"].to_numpy()


#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=42, shuffle=True)

vectorizer = glove()
 
#X_test = vectorizer.transform(X_test)

model = pickle.load(open("model.pickle", "rb"))

#print(sum(model.predict(X_test) == Y_test)/len(Y_test))

def predict(x):
    x = vectorizer.transform([x])
    return model.predict(x)


