# ----------------- special characters ----------------------
import re
def remove_special_characters(text):
    # Check if the value is a string
    if isinstance(text, str):
        # Define the regular expression pattern to identify unwanted characters
        text = text.lower()
        pattern = r'[^a-zA-Z\s]'  # Keep only alphabetic characters

        # Replace unwanted characters with an empty string
        clean_text = re.sub(pattern, '', text)
        return clean_text
    else:
        return text  # Return the original value if it's not a string

# ---------------------- remove stop words function--------------------------------------------
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stop_words(string):
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words and len(word) > 3]
    new_string = ' '.join(filtered_words)
    return new_string

# ------------------- cleaning dataset --------------------------
import pandas as pd

def process_description(row):
     return remove_stop_words(row['review_description'])

def cleaning_dataset(dataFrame):
  # 1.Text cleaning 
  #---- remove special characters, numbers and punctuation,and lowercasing----
 data = pd.read_csv(dataFrame)
 data["review_description"] = data["review_description"].apply(remove_special_characters)


# 2. Stop word removal
 data['review_description'] = data.apply(process_description, axis=1)
 data.to_csv(dataFrame, index = False) 

# 3. Remove duplicates 
 data.drop_duplicates(inplace=True) 
 data.to_csv(dataFrame, index = False)



# ---------------------------------------- Tokenization, Stemming & Spelling Correction--------------------------------
#  nltk.download('punkt')
#  nltk.download('averaged_perceptron_tagger')
#  nltk.download('wordnet')

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from textblob import TextBlob

def stemming_tokenization(dataFrame):
    df = pd.read_csv(dataFrame)
    porter = PorterStemmer()

    def stem_tokens(tokens):
        return ' '.join([porter.stem(token) for token in tokens])

    def spell_check_and_correct(text):
        blob = TextBlob(text)
        corrected_text = []
        for word in blob.words:
            corrected_text.append(word.correct())  # Correct the word
        print(corrected_text, '\n')
        return ' '.join(corrected_text)

    df['review_description'] = df['review_description'].fillna('')
    df['review_description'] = df['review_description'].apply(spell_check_and_correct)

    df['review_description_tokens'] = df['review_description'].apply(lambda x: word_tokenize(x))
    df['review_description'] = df['review_description_tokens'].apply(stem_tokens)
    df = df.drop(columns=['review_description_tokens'])
    df.to_csv(dataFrame, index=False)

