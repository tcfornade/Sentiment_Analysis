from langdetect import detect, LangDetectException
from googletrans import Translator
import pandas as pd
import time

translator = Translator()

def is_english(word):
    try:
        return detect(word) == 'en' #se verifica daca cuvantul este in engleza
    except LangDetectException:
        return False

def translate_to_english(word): #functie pentru traducerea unui cuvant 
    try:
        translation = translator.translate(word, dest='en')
        return translation.text
    except Exception as e:
        return word  

def clean_review(review):
    words = review.split() #se imparte descrierea on cuvinte
    english_words = [] #se creaza un vector gol in care vor fi adaugate doar cuvintele corespunzatoare
    for word in words:
        if is_english(word): #se verifica daca este deja in engleza
            english_words.append(word) #daca da, atunci se adauga cuvantul la vectorul english_words[]
        else:
            translated_word = translate_to_english(word) #se traduce cuvantul in engleza cu ajutorul functiei
            if is_english(translated_word):  #daca traducerea a functionat atunci se adauga la vectorul de cuvinte
                english_words.append(translated_word)
    return ' '.join(english_words)

def file_translation(input): #functie principala care traduce intreg fisierul dat ca parametru
   df = pd.read_csv(input)
   start_time = time.time()
   df['review_description'] = df['review_description'].apply(clean_review)
   df.to_csv('dataSet/cleaned_threads_reviews.csv', index=False)
   end_time = time.time()
   elapsed_time = end_time-start_time
   print(f"Time to perform translation: {elapsed_time:.2f} seconds")
