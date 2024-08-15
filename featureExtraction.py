import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import time

def create_bag_of_words_from_csv(input_csv_file, output_csv_file):
    
    df = pd.read_csv(input_csv_file) #importare si citire fisier CSV
    df['review_description'] = df['review_description'].fillna("no_review") #daca sunt valori lipsa vor fi inlocuite cu stringul 'no_review'
    
    start_time = time.time() #contorizare timp
    vectorizer = CountVectorizer() #se initializeaza un obiect CountVectorizer
    X = vectorizer.fit_transform(df['review_description']) #se antreneaza pe textul din coloana 'review_description'
    #rezultatul este o matrice unde fiecare rand reprezinta un review, iar fiecare coloana reprezinta un cuvant, valorile fiind frecventele cuvintelor
    bag_of_words = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out()) #se converteste matricea intr-un DataFrame unde fiecare coloana este denumita dupa cuvinte
    df.drop(columns=['review_description'], inplace=True)
    bag_of_words = pd.concat([df, bag_of_words], axis=1) #imbinarea bazei de date originale cu cea creata
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to create BoW model: {elapsed_time:.2f} seconds")
    bag_of_words.to_csv(output_csv_file, index=False) #salvarea fisierului CSV


