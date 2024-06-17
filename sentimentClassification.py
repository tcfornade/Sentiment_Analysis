import nltk
import pandas as pd
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def classify_sentiments(description, rating):

    if not isinstance(description, str):
        description = str(description)

    if description == "":
        if rating > 3:
            sentiment = 'positive'
        elif rating < 3:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    else: 
        sid = SentimentIntensityAnalyzer()
    # Get the sentiment scores for the description
        scores = sid.polarity_scores(description)
    
    # Classify the sentiment based on the compound score
        if scores['compound'] >= 0.05  or (pd.Series(rating) > 3).any():
            sentiment  ='positive'
        elif scores['compound'] <= -0.05 or (pd.Series(rating) < 3).any():
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
    
    return sentiment

def add_sentiment_to_dataset(dataFrame):
    data = pd.read_csv(dataFrame)
    sentiments=[]

    for description, rating in zip(data['review_description'], data['rating']):
       sentiment = classify_sentiments(description, rating)
       sentiments.append(sentiment)

    data['sentiment'] = sentiments #create a column for sentiment classification
    data.to_csv("dataSet/sentiment_analysis.csv", index = False) #save the DataFrame back to csv
    