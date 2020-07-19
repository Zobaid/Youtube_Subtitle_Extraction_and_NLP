#Import packages and data
import pandas as pd
import re, string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob

df=pd.read_csv('addidas3.csv')

##### DATA CLEANING ########
sw = stopwords.words('english')

def clean_text(text):

    text = text.lower()
    text = re.sub('@', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub(r"[^a-zA-Z ]+", "", text)
    
    #Tokenize the data
    text = nltk.word_tokenize(text)
    #Remove stopwords
    text = [w for w in text if w not in sw]

    return text

# Applying the cleaning function to data
df['comment'] = df['comment'].apply(lambda x: clean_text(x))


#Lemmatizer
lemmatizer = WordNetLemmatizer()
def lem(text):
    text = [lemmatizer.lemmatize(t) for t in text]
    text = [lemmatizer.lemmatize(t, 'v') for t in text]

    return text

df['comment'] = df['comment'].apply(lambda x: lem(x))


#Remove all empty comments
empty_comment = df['comment'][19]

for i in range(len(df)):
    if df['comment'][i]==empty_comment:
        df=df.drop(i)

df=df.reset_index(drop=True)

######### ANALYSIS ########

#From lists to single list       
all_words=[]        
for i in range(len(df)):
    all_words = all_words + df['comment'][i]


#Get word frequency        
nlp_words = nltk.FreqDist(all_words)
nlp_words.plot(20, color='salmon', title='Word Frequency')

#Bigrams
bigrm = list(nltk.bigrams(all_words))
words_2 = nltk.FreqDist(bigrm)
words_2.plot(20, color='salmon', title='Bigram Frequency')

#Trigrams
trigrm = list(nltk.trigrams(all_words))
words_3 = nltk.FreqDist(trigrm)
words_3.plot(20, color='salmon', title='Trigram Frequency')


#Get sentiment from comments
df['comment'] = [str(thing) for thing in df['comment']]

sentiment = []
for i in range(len(df)):
    blob = TextBlob(df['comment'][i])
    for sentence in blob.sentences:
        sentiment.append(sentence.sentiment.polarity)

df['sentiment']=sentiment
df['sentiment'].plot(color='salmon', title='Comments Polarity')
        
#Basic stats
df['sentiment'].describe()
nlp_words['criminal']
