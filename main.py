<<<<<<< HEAD
import os
import pandas as pd
from dataPreprocessing import cleaning_dataset, stemming_tokenization
from sentimentClassification import add_sentiment_to_dataset
from copyDataFile import copy_data_file
from featureExtraction import create_bag_of_words_from_csv
from convertCSVtoARFF import convertCSVtoARFF
from extractData import extract_data_from_csv
from translateFile import file_translation
from trainData import run_weka_cross_validation, run_weka_data_splitting

def get_user_input(prompt, options):
    print(prompt)
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = int(input("Enter the number of your choice: ")) - 1
    return options[choice]

def main():
    filename = "threads_reviews.csv"
    #-> threads_reviews.csv - document initial
    if not os.path.exists("dataSet/cleaned_threads_reviews.csv"):
      file_translation(filename)
      filename = "dataSet/cleaned_threads_reviews.csv"

 #--------------------------------------------curaterea setului de date-------------------------------------
    if not os.path.exists("dataSet/data_cleaned.csv"):
      dataFrame = "dataSet/data_cleaned.csv"
      copy_data_file(filename, dataFrame)

      df = pd.read_csv(dataFrame) 
      df = df.drop(['source', 'review_date'], axis=1) #eliminarea coloanelor
      df.to_csv(dataFrame, index=False) #salvarea in tabel

      df.drop_duplicates(inplace=True) #eliminarea duplicatelor
      print("Removing duplicates successfully!\n")

      cleaning_dataset(dataFrame) #apelarea functiei de curatare a setului de date

      df = stemming_tokenization(dataFrame) #apelarea functiei de stematizare, tokenizare

 # ----------------------------------#realizarea analizei sentimentelor------------------------------------
    if not os.path.exists("dataSet/sentiment_analysis.csv"):
      dataFrame = "dataSet/data_cleaned.csv"
      add_sentiment_to_dataset(dataFrame) # -- sentiment_analysis.csv

 #--------------------------------- extragerea trasaturilor cu modelul BoW --------------------------
    if not os.path.exists("dataSet/bag_of_words.csv"):
     dataFrame = "dataSet/sentiment_analysis.csv"
     create_bag_of_words_from_csv(dataFrame, "dataSet/bag_of_words.csv")
     convertCSVtoARFF("dataSet/bag_of_words.csv", "dataSet/bag_of_words_with_all_data.arff")


# # -----------------extragerea datelor pentru o baza de date balansata ------
    if not os.path.exists("dataSet/sentiment_analysis_with_small_data.csv"):
      extract_data_from_csv()

    if not os.path.exists("dataSet/bag_of_words_with_small_data.csv"):
     dataFrame = "dataSet/sentiment_analysis_with_small_data.csv"
     create_bag_of_words_from_csv(dataFrame, "dataSet/bag_of_words_with_small_data.csv")
     convertCSVtoARFF('dataSet/bag_of_words_with_small_data.csv', 'dataSet/bag_of_words_with_small_data.arff')

 #-----------------------------------Antrenarea datelor-----------------------------
    data_files = ["bag_of_words.arff", "bag_of_words_with_small_data.arff"]
    classifiers = {
        "J48": ("weka.classifiers.trees.J48", ["-C", "0.25", "-M", "2"]),
        "Random Forest": ("weka.classifiers.trees.RandomForest", ["-P", "100" ,"-I", "800", "-num-slots", "1", "-K", "0" ,"-M", "2.0", "-V", "0.001", "-S", "1"]),
        "Random Tree": ("weka.classifiers.trees.RandomTree", ["-K", "20", "-M", "1.0" ,"-V" ,"0.001","-S" ,"1", "-depth", "0", "-N", "0"]),
        "SVM": ("weka.classifiers.functions.SMO", ["-C", "1.0", "-L", "0.001" ,"-P" ,"1.0E-12","-N" ,"0", "-V", "-1", "-W", "1", "-K", "weka.classifiers.functions.supportVector.PolyKernel",
                                                    "-calibrator", "weka.classifiers.functions.Logistic", "-num-decimal-places", "4"]),
        "NaiveBayesMultinomial": ("weka.classifiers.bayes.NaiveBayesMultinomial", [])
    }

    evaluation_methods = ["cross-validation", "train/test split"]

    # selectarea fisierului cu baza de date
    data_dir = get_user_input("Select the data file:", data_files)

    # selectarea clasificatorului
    classifier_name, classifier_options = classifiers[get_user_input("Select the classifier:", list(classifiers.keys()))]

    # selectarea metodei de testare
    evaluation_method = get_user_input("Select the evaluation method:", evaluation_methods)

    if evaluation_method == "cross-validation":
        run_weka_cross_validation(data_dir, classifier_name, classifier_options)
    else:
        train_split = int(input("Enter the train split percentage: "))
        run_weka_data_splitting(data_dir, classifier_name, classifier_options, train_split)

if __name__ == "__main__":
    main()
=======

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

>>>>>>> 240a3aa8907706a030455032fae9f8f2dab59bf8
