
import csv
import pandas as pd
import matplotlib.pyplot as plt
from removeStopWords import remove_stop_words

# csv file name
filename = "threads_reviews.csv"

# ---- read CSV file using pandas
dataFrame = pd.read_csv(filename)
#print(dataFrame.head(7))

#print(dataFrame.info()) #permite sa analizam daca avem valori de null in tabel, pentru ca ulterior sa le putem elimina

#cleaning dataset:
#removing rows
dataFrame = dataFrame.dropna()

#discover duplicates
#print(dataFrame.duplicated())

dataFrame.drop_duplicates(inplace=True) #remove all duplicates

print(dataFrame.columns)
#remove stopWords from description column

def process_description(row):
    return remove_stop_words(row['review_description'])

dataFrame['review_description'] = dataFrame.apply(process_description, axis=1)

dataFrame.to_csv(filename, index = False)