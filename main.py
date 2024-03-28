
import csv
import nltk
import pandas as pd
import shutil
import matplotlib.pyplot as plt
from removeStopWords import remove_stop_words
from sentimentClassification import classify_sentiments
from removeSpecialCharacters import remove_special_characters

#-> threads_reviews.csv - document initial pe care l-am copiat in alt document
#-> data_cleaned.csv - document copiat dupa threads.reviews pentru a curata datele
#-> sentiment_analysis.csv - document creat pentru a analiza sentimentele(se adauga coloana 'sentiment')

filename = "dataSet/threads_reviews.csv"
dataFrame = "dataSet/data_cleaned.csv"

try:
    shutil.copyfile(filename, dataFrame)
    print(f"File '{filename}' copied to '{dataFrame}' successfully.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occured: {e}")

#--------------------------------------------cleaning dataset:-------------------------------------
#discover duplicates
#print(dataFrame.duplicated())
source = pd.read_csv(dataFrame)
source.drop_duplicates(inplace=True) #remove all duplicates

#-----remove stopWords from description column
def process_description(row):
    return remove_stop_words(row['review_description'])

source['review_description'] = source.apply(process_description, axis=1)
source.to_csv(dataFrame, index = False) #save the DataFrame back to csv

#---- remove special characters -----
data = pd.read_csv("dataSet/data_cleaned.csv")
data["review_description"] = data["review_description"].apply(remove_special_characters)

# ----------------------------------#perform sentiment analysis------------------------------------
sentiments=[]

for description in data['review_description']:
    sentiment = classify_sentiments(description)
    sentiments.append(sentiment)

data['sentiment'] = sentiments #create a column for sentiment classification

data.to_csv("dataSet/sentiment_analysis.csv", index = False) #save the DataFrame back to csv

#see if dataset is balanced

import csv
sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}

with open('dataSet/sentiment_analysis.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sentiment_counts[row['sentiment']] += 1

print("Sentiment Counts:")
for sentiment, count in sentiment_counts.items():
    print(f"{sentiment.capitalize()}: {count}")

