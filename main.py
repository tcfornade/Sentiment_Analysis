
import csv
from dataPreprocessing import cleaning_dataset, stemming_tokenization
from sentimentClassification import add_sentiment_to_dataset
from copyDataFile import copy_data_file
import pandas as pd

#-> threads_reviews.csv - document initial pe care l-am copiat in alt document
#-> data_cleaned.csv - document copiat dupa threads.reviews pentru a curata datele
#-> sentiment_analysis.csv - document creat pentru a analiza sentimentele(se adauga coloana 'sentiment')

filename = "dataSet/threads_reviews.csv"
dataFrame = "dataSet/data_cleaned.csv"

#copy_data_file(filename, dataFrame)

#Setul de date are initial coloanele source, review_description, rating si review_date
#pentru modelul pe care il constrim nu avem nevoie de coloanele source si review_date, deci le vom sterge:

# df = pd.read_csv(dataFrame)
# df = df.drop(['source', 'review_date'], axis=1)
# df.to_csv(dataFrame, index=False)

#--------------------------------------------cleaning dataset:-------------------------------------
#cleaning_dataset(dataFrame)

# ! - de afisat word cloud pentru a face diferenta intre cuvinte inainte si dupa corectare

#stemming_tokenization(dataFrame)# + spelling correction

# # ----------------------------------#perform sentiment analysis------------------------------------
#add_sentiment_to_dataset(dataFrame) # -- sentiment_analysis.csv

#--------------------------------- BOW --------------------------
import csv
from featureExtraction import create_bag_of_words_from_csv
from convertCSVtoARFF import convertCSVtoARFF_forRandomForest_training

dataFrame = "dataSet/sentiment_analysis.csv"
create_bag_of_words_from_csv(dataFrame, "dataSet/bag_of_words.csv")
convertCSVtoARFF_forRandomForest_training("dataSet/bag_of_words.csv", "dataSet/bag_of_words.arff")

# #----------------- SMOTE -----------------------------

# extract_data_from_csv() #extract the minimum amount of data for each class
# dataFrame = "dataSet/sentiment_analysis_5%_data.csv"
# #create_bag_of_words_from_csv(dataFrame, "bag_of_words.csv")
# convertCSVtoARFF_forBOW('bag_of_words.csv', 'bag_of_words.arff')

# ---------- training -------------
from trainData import run_weka

data_dir = "dataSet/bag_of_words.arff"

#J48
# classifier_name = "weka.classifiers.trees.J48"
# classifier_options = ["-C", "0.3", "-M", "2"]
# run_weka(data_dir, classifier_name, classifier_options)

#Random Forest
# classifier_name = "weka.classifiers.trees.RandomForest"
# classifier_options = ["-P", "100" ,"-I", "100", "-num-slots", "1", "-K", "0" ,"-M", "1.0", "-V", "0.001", "-S", "1"]
# run_weka(data_dir, classifier_name, classifier_options)

#Random Tree
classifier_name = "weka.classifiers.trees.RandomTree"
classifier_options = ["-K", " 0", "-M", "1.0" ,"-V" ,"0.001","-S" ,"1"]
run_weka(data_dir, classifier_name, classifier_options)

