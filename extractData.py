
import pandas as pd

def extract_data_from_csv(dataframe):
 df = pd.read_csv(dataframe)
 sentiment_counts = df['sentiment'].value_counts() #grupeaza DataFrame-ul in functie de coloana 'sentiment' si numara numarul de randuri pentru fiecare sentiment
 min_count = sentiment_counts.min()#gaseste numarul minim de date
 sampled_data = pd.concat([df[df['sentiment'] == sentiment].sample(min_count) for sentiment in sentiment_counts.index]) #concateneaza acelasi numar de date pentru fiecare clasa
 sampled_data = sampled_data.sample(frac=1, random_state=1) #amesteca baza de date 
 sampled_data.to_csv("sentiment_analysis_with_small_data.csv", index=False) #salveaza fisierul
