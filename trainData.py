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
