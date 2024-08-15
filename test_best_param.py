
import weka.core.jvm as jvm
import weka.classifiers as classifiers
from weka.core.converters import Loader
from itertools import product


def cross_validate_with_loader(dataset_path, classifier, n_folds=10):

    loader = Loader(classname="weka.core.converters.ArffLoader" if dataset_path.endswith(".arff") else "weka.core.converters.CSVLoader")
    data = loader.load_file(dataset_path, class_index='second')

    evaluation = classifiers.Evaluation(data)
    evaluation.crossvalidate_model(classifier, data, n_folds, classifiers.Random(1))

    # returneaza acuratetea
    accuracy = evaluation.percent_correct
    return accuracy

def find_best_params(dataset_path, classifier_name, param_grid, n_folds=10):

    jvm.start(packages=True)

    # initializeaza variabila pentru a stoca cei mai buni parametrii
    best_params = None
    best_accuracy = 0

    # genereaza toate combinatiile de parametri
    param_names = list(param_grid.keys())
    param_combinations = list(product(*param_grid.values()))

    # numarul total de combinatii
    total_combinations = len(param_combinations)
    
    classifier_simple_name = classifier_name.split('.')[-1]
    output_file = f"{classifier_simple_name}_best_parameters.txt"

    for index, param_comb in enumerate(param_combinations):
              
        print(f"Processing combination {index + 1}/{total_combinations}: {dict(zip(param_names, param_comb))} \n")
        # creaza clasificatorul cu parametri curenti
        options = []
        for param_name, param_value in zip(param_names, param_comb):
            options.append(f"-{param_name}")
            options.append(str(param_value))

        classifier = classifiers.Classifier(classname=classifier_name, options=options)

        # realizeaza testarea prin validare incrucisata stocand acuratetea
        accuracy = cross_validate_with_loader(dataset_path, classifier, n_folds)
        with open(output_file, "a") as file:
         file.write(f"\nProcessing combination {index + 1}/{total_combinations}: {dict(zip(param_names, param_comb))}")
         file.write(f"\n  Accuracy: {accuracy}%")

        # reinnoieste parametrii daca acuratetea este peste cea anterioara
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_params = {param_name: param_value for param_name, param_value in zip(param_names, param_comb)}
        
        
    with open(output_file, "a") as file:
        file.write(f"\nBest Parameters: {best_params}")
        file.write(f"\nBest Accuracy: {best_accuracy}")
    jvm.stop()
    return best_params, best_accuracy

dataset_path = "dataSet/bag_of_words_with_all_data.arff"
# dataset_path = "dataSet/bag_of_words_with_small_data.arff"

# J48:
classifier_name = "weka.classifiers.trees.J48"
param_grid = {
    "C": [0.25, 0.5, 0.75],
    "M": [2, 3, 4, 5]
}

# Random Forest
# classifier_name = "weka.classifiers.trees.RandomForest"
# param_grid = {
#     "I": [100, 200, 400, 800],  # Number of trees to construct
#     "depth": [0, 10],        # Maximum depth of the trees
#     "K": [0, 5],            # Number of attributes to randomly investigate
#     "M": [1, 2],             # Minimum number of instances per leaf
#     "num-slots": [1]      # Number of execution slots (threads) to use
# }

# RandomTree:
# classifier_name = "weka.classifiers.trees.RandomTree"
# param_grid = {
#     "K": [0, 10, 20],  # Number of attributes to randomly investigate
#     "M": [1, 2, 3, 4],    # Minimum number of instances per leaf
#     "depth": [0, 5, 10],  # Maximum depth of the tree
#     "N": [0, 2] # Number of folds for backfitting
# }

#Naive Bayes Multinomial
# classifier_name = "weka.classifiers.bayes.NaiveBayesMultinomial"
# param_grid = {
#     "do-not-check-capabilities": ["", "-do-not-check-capabilities"],  # Whether to skip capability checks
# }

# classifier_name = "weka.classifiers.functions.SMO"
# # classifier_options = ["-C", "1.0", "-L", "0.001" ,"-P" ,"1.0E-12","-N" ,"0", "-V", "-1", "-W", "
# param_grid = {
#     "C": [1.0, 2.0],
#     "K": ["weka.classifiers.functions.supportVector.PolyKernel",
#            "weka.classifiers.functions.supportVector.RBFKernel"],
#     "calibrator": ["weka.classifiers.functions.Logistic -R 1.0E-8 -M -1 -num-decimal-places 4"]
# }


best_params, best_accuracy = find_best_params(dataset_path, classifier_name, param_grid)
print("Best Parameters:", best_params)
print("Best Accuracy:", best_accuracy)
