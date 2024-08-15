# ----------------- eliminarea caracterelor speciale ----------------------
import re
def remove_special_characters(text):
    if isinstance(text, str):
        text = text.lower()
        pattern = r'[^a-zA-Z\s]'  
        clean_text = re.sub(pattern, '', text)
        return clean_text
    else:
        return text  

# ---------------------- eliminarea cuvintelor comune --------------------------------------------
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stop_words(string):
    if pd.isnull(string):
        return ''
    string = str(string) 
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words and len(word) > 3]
    new_string = ' '.join(filtered_words)
    return new_string


import pandas as pd
def cleaning_dataset(dataFrame):
  # curatarea textului:
 data = pd.read_csv(dataFrame)
   
 data["review_description"] = data["review_description"].apply(remove_special_characters)
 data.to_csv("data_without_specialch.csv", index=False)
 print("Removing special characters successfully!\n")
 data.to_csv("data_cleaned_specialch_stopwords_dupl.csv", index = False)
 data.to_csv(dataFrame, index=False)

 data['review_description'] = data['review_description'].apply(remove_stop_words)
 data.to_csv("data_without_stopwords.csv", index=False)
 print("Removing stop words successfully!\n")
 data.to_csv(dataFrame, index = False) 


# --------------------- Tokenizare, Stemming si corectarea cuvintelor--------------------------------
 nltk.download('punkt') #pentru operatia de tokenizare
 nltk.download('wordnet') #pentru stematizare

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob
import time

def stem_tokens(tokens):
    porter = PorterStemmer()
    return ' '.join([porter.stem(token) for token in tokens])

def spell_check_and_correct(text):
        blob = TextBlob(text)
        corrected_text = blob.correct()
        print(corrected_text)
        return str(corrected_text)

def stemming_tokenization(dataFrame):
    df = pd.read_csv(dataFrame)
    df['review_description'] = df['review_description'].fillna('')

    start_time = time.time()
    df['review_description'] = df['review_description'].apply(spell_check_and_correct)
    end_time = time.time()

    elapsed_time_for_spelling = end_time-start_time
    print(f"Time taken for spelling and correction: {elapsed_time_for_spelling:.2f} seconds")
    
    df['review_description_tokens'] = df['review_description'].apply(lambda x: word_tokenize(x))
    df['review_description'] = df['review_description_tokens'].apply(stem_tokens)
    df = df.drop(columns=['review_description_tokens'])
    df.to_csv(dataFrame, index=False)
    df.to_csv("data_cleaned_stem_spelling_corr.csv")
    return df

