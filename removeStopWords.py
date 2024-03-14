import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def remove_stop_words(string):
    stop_words = set(stopwords.words('english'))
    words = string.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    new_string = ' '.join(filtered_words)
    return new_string
