# import os

# # Specify the path to your file
# file_path = 'dataSet/threads_reviews.csv'

# # Get the size of the file in bytes
# file_size = os.path.getsize(file_path)

# # Convert the size to kilobytes (KB)
# file_size_kb = file_size / 1024

# # Print the size in KB
# print(f'The file size is {file_size_kb:.2f} KB')

# #------ plot files chart
# import matplotlib.pyplot as plt

# # Data
# file_sizes_kb = [3362, 1875, 850, 779, 648, 514]
# file_names = ['Originală', 'După traducere', 'Eliminarea coloanelor', 'Eliminare caractere speciale', 'Trunchiere', 'Eliminarea cuvintelor comune']

# plt.figure(figsize=(7, 6))
# plt.plot(file_names, file_sizes_kb, marker='o', linestyle='-', color='b')

# # Adding numerical values on the plot
# for i, value in enumerate(file_sizes_kb):
#     plt.text(i, value + 50, str(value), ha='center', va='bottom')

# # Adding labels and title
# plt.xlabel('Fișierul')
# plt.ylabel('Dimensiunea (KB)')
# plt.title('Dimensiunea fișierului în Kilobytes')

# plt.xticks(rotation=20)

# # Show the plot
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# # Example data (replace with your actual accuracy values)
# cases = ['Case 1', 'Case 2', 'Case 3']
# algorithms = ['J48', 'Random Forest', 'Random Tree', 'SVM', 'Naive Bayes Multinomial']
# accuracies = np.array([
#     # [98.28, 98.49, 98.25],  # J48
#     # [98.26, 98.8, 98.56],  # Random Forest
#     # [95.89, 96.92, 94.22], #Random Tree
#     # [98.79, 98.69, 98.53], #SVM
#     # [57.79, 59.29, 56.26] #Naive Bayes

#     [98.73, 98.77, 98.12], #J48
#     [98.73, 98.8, 98.64], #Random Forest
#     [96.91, 97.35, 94.26], #Random Tree
#     [99, 98.81, 98.55], #SVM
#     [73.49, 73.6, 73.63]#Naive Bayes
# ])

# # Plotting
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plot bars for each case and algorithm
# bar_width = 0.2  # Width of the bars
# space_between_bars = 0.0  # Space between different cases

# index = np.arange(len(algorithms))  # Index for the algorithms

# for i, case in enumerate(cases):
#     bar_positions = index + i * (bar_width + space_between_bars)
#     ax.barh(bar_positions, accuracies[:, i], height=bar_width, label=case)

#     # Annotate each bar with its accuracy value
#     for j, acc in enumerate(accuracies[:, i]):
#         ax.text(acc + 0.5, bar_positions[j], f'{acc:.2f}', va='center')

# # Customize plot
# ax.set_yticks(index + ((len(cases) - 1) / 2) * (bar_width + space_between_bars))
# ax.set_yticklabels(algorithms)
# ax.set_xlabel('Acuratețea (%)')
# ax.set_title('Compararea valorii acurateței pentru cele 3 cazuri de testare pentru setul de date dezechilibrat')
# ax.legend(title='Cazul', loc='upper right')

# # Display the plot
# plt.tight_layout()
# plt.show()




# # ---------- training model -------------

from trainData import run_weka_cross_validation, run_weka_data_splitting

# data_dir = "dataSet/bag_of_words_with_small_data.arff"
# data_dir = "dataSet/bag_of_words_with_all_data.arff"


# data_dir = "bag_of_words_new.arff"
# data_dir="bag_of_words_with_small_data.arff"

# # train_data = 70


# -------------------#J48--------------
# classifier_name = "weka.classifiers.trees.J48"
# classifier_options = ["-C", "0.25", "-M", "2"]

# #--------------- #Random Forest---------------
# classifier_name = "weka.classifiers.trees.RandomForest"
# classifier_options = ["-P", "100" ,"-I", "800", "-num-slots", "1", "-K", "0" ,"-M", "2.0", "-V", "0.001", "-S", "1"]

#----------Random Tree
# classifier_name = "weka.classifiers.trees.RandomTree"
# classifier_options = ["-K", "20", "-M", "1.0" ,"-V" ,"0.001","-S" ,"1", "-depth", "0", "-N", "0"]

# # ---------------------SVM -----------------
# classifier_name = "weka.classifiers.functions.SMO"
# classifier_options = ["-C", "1.0", "-L", "0.001" ,"-P" ,"1.0E-12","-N" ,"0", "-V", "-1", "-W", "1", "-K", "weka.classifiers.functions.supportVector.PolyKernel",
#                        "-calibrator", "weka.classifiers.functions.Logistic", "-num-decimal-places", "4"]


# ---------NaiveBayesMultinomial
# classifier_name = "weka.classifiers.bayes.NaiveBayesMultinomial"
# classifier_options = []

# run_weka_cross_validation(data_dir, classifier_name, classifier_options)

# run_weka_data_splitting(data_dir, classifier_name, classifier_options, 50)

# dataFrame = "sentiment_analysis.csv"
# create_bag_of_words_from_csv(dataFrame, "bag_of_words_new.csv")
# convertCSVtoARFF("bag_of_words_new.csv", "bag_of_words_new.arff")


# extract_data_from_csv("sentiment_analysis.csv")
# create_bag_of_words_from_csv("sentiment_analysis_with_small_data.csv", "bag_of_words_with_small_data.csv")
# convertCSVtoARFF('bag_of_words_with_small_data.csv', 'bag_of_words_with_small_data.arff')