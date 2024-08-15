<<<<<<< HEAD
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, Evaluation
from weka.core.classes import Random
import weka.plot.classifiers as plot_cls
import time
from confusionMatrix import plot_confusion_matrix

#functia de testare prin validarea incrucisata
def run_weka_cross_validation(data_dir, classifier_name, classifier_options=None):

    jvm.start() #pornirea JVM
    
    try:
        start_time = time.time()
        #incarcarea datelor
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file(data_dir, class_index="second")

        # setarile clasificatorului
        classifier = Classifier(classname=classifier_name)
        if classifier_options:
            classifier.options = classifier_options

        # construirea clasificatorului
        classifier.build_classifier(data)

        # evaluarea modelului cu validarea incrucisata
        evaluation = Evaluation(data)
        evaluation.crossvalidate_model(classifier, data, 10, Random(1))

        # inregistrarea timpului
        end_time = time.time()
        duration = end_time - start_time

        #crearea unui fisier pentru rezultate
        classifier_simple_name = classifier_name.split('.')[-1]  
        output_file = f"{classifier_simple_name}_results_cross_validation.txt"

        # salvarea rezultatelor in fisier
        with open(output_file, "w") as file:
            file.write(f"Classifier: {classifier}\n")
            file.write(evaluation.summary() + "\n")
            file.write(f"Detailed Accuracy By Class:\n")
            file.write(evaluation.class_details() + "\n")
            file.write("Confusion Matrix:\n")

            plot_confusion_matrix(evaluation.confusion_matrix)

            file.write(str(evaluation.confusion_matrix) + "\n")
            file.write(f"Time taken: {duration} seconds\n")

    finally:
        jvm.stop() #oprirea JVM

# functie pentru testarea prin impartire a datelor
def run_weka_data_splitting(data_dir, classifier_name, classifier_options, train_percent):
    jvm.start()
    
    try:
        start_time = time.time()

        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file(data_dir, class_index="second")

        classifier = Classifier(classname=classifier_name)
        if classifier_options:
            classifier.options = classifier_options

        # generarea metodei train/test split
        train_data, test_data = data.train_test_split(train_percent, Random(1))

        classifier.build_classifier(train_data)

        evaluation = Evaluation(train_data)
        evaluation.test_model(classifier, test_data)

        end_time = time.time()
        duration = end_time - start_time

        classifier_simple_name = classifier_name.split('.')[-1]
        output_file = f"{classifier_simple_name}_results_train_test_split_{train_percent}.txt"

        with open(output_file, "w") as file:
            file.write(f"Classifier: {classifier}\n")
            file.write(evaluation.summary() + "\n")
            file.write(f"Detailed Accuracy By Class:\n")
            file.write(evaluation.class_details() + "\n")
            file.write("Confusion Matrix:\n")
            plot_confusion_matrix(evaluation.confusion_matrix)
            file.write(str(evaluation.confusion_matrix) + "\n")
            file.write(f"Time taken: {duration} seconds\n")

    finally:
        jvm.stop()

=======
# import subprocess

# # Define the command to run Weka classifier from command line
# command = ["java", "-classpath", "weka.jar", "weka.classifiers.functions.LinearRegression", "-t", "airline.arff"]

# # Run the command and capture the output
# output = subprocess.check_output(command)

# # Print the output
# print(output.decode('utf-8'))

import subprocess
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the ARFF file into a pandas DataFrame
arff_file_path = "dataSet/newData.arff"
data = pd.read_csv(arff_file_path, comment='@', header=None)

# Separate features and target variable
X = data.iloc[:, :-1]  # Features
y = data.iloc[:, -1]   # Target variable

# Convert string attributes to numerical/categorical attributes
label_encoders = {}
for column in X.columns:
    if X[column].dtype == 'object':
        label_encoders[column] = LabelEncoder()
        X[column] = label_encoders[column].fit_transform(X[column])

# Convert target variable to numerical format
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Write the preprocessed data to a new ARFF file
preprocessed_arff_file_path = "dataSet/preprocessed_data.arff"
with open(preprocessed_arff_file_path, 'w') as f:
    f.write('@relation Google_Play_Reviews\n\n')
    for column in X.columns:
        f.write(f'@attribute {column} numeric\n')
    f.write('@attribute sentiment {positive, negative, neutral}\n\n')
    f.write('@data\n')
    for i in range(len(X)):
        line = ','.join([str(val) for val in X.iloc[i]]) + f',{label_encoder.inverse_transform([y[i]])[0]}\n'
        f.write(line)

# Define the command to run Weka classifier from command line
command = ["java", "-classpath", "weka.jar", "weka.classifiers.bayes.NaiveBayes", "-t", preprocessed_arff_file_path]

# Run the command and capture the output
output = subprocess.check_output(command)

# Clean the output and print it
output = output.decode('utf-8')
print(output)
>>>>>>> 240a3aa8907706a030455032fae9f8f2dab59bf8
