import nltk
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
    