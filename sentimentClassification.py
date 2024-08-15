import nltk
<<<<<<< HEAD
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import time

def classify_sentiments(description, rating):
    
    if not isinstance(description, str):
        description = str(description)

    if description == "" :
        if rating > 3:
            sentiment = 'positive'
        elif rating < 3:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    else: 
        sid = SentimentIntensityAnalyzer()

        scores = sid.polarity_scores(description)
    
        if scores['compound'] > 0.05 or rating > 3:
            sentiment  ='positive'
        elif scores['compound'] < -0.05 or rating < 3 :
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    
    return sentiment


def add_sentiment_to_dataset(dataFrame):
    data = pd.read_csv(dataFrame)
    sentiments=[]
    
    start_time = time.time()
    for description, rating in zip(data['review_description'], data['rating']):
       sentiment = classify_sentiments(description, rating)
       sentiments.append(sentiment)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Time to perform sentiment analysis: {elapsed_time:.2f} seconds")

    data['sentiment'] = sentiments 
    data.to_csv("sentiment_analysis.csv", index = False) 
    sentiment_counts = data['sentiment'].value_counts() #numarare a sentimentelor 
    print(sentiment_counts)
    
=======
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_sentiments(description):
    sid = SentimentIntensityAnalyzer()

    # Convert the description to a string if it's not already
    if not isinstance(description, str):
        description = str(description)
        
    # Get the sentiment scores for the description
    scores = sid.polarity_scores(description)
    
    # Classify the sentiment based on the compound score
    if scores['compound'] >= 0.05:
        sentiment = 'positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return sentiment
    
>>>>>>> 240a3aa8907706a030455032fae9f8f2dab59bf8
