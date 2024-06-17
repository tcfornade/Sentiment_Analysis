
import weka.core.jvm as jvm
from weka.core.converters import Loader
from weka.classifiers import Classifier, SingleClassifierEnhancer, MultipleClassifiersCombiner, FilteredClassifier, \
    PredictionOutput, Kernel, KernelClassifier
from weka.classifiers import Evaluation
from weka.filters import Filter
from weka.core.classes import Random, from_commandline
import weka.plot.classifiers as plot_cls
import weka.plot.graph as plot_graph
import weka.core.typeconv as typeconv
import time  # Import the time module

def run_weka(data_dir, classifier_name, classifier_options=None):
    """
    Function to run Weka classifier on a given dataset.
    
    Parameters:
    data_dir (str): Path to the ARFF file.
    classifier_name (str): Full name of the Weka classifier .
    classifier_options (list, optional): List of options for the classifier. Defaults to None.
    """
    # Start JVM (Weka runs in Java)
    jvm.start()
    
    try:
        # Record the start time
        start_time = time.time()

        # Load data using Loader
        loader = Loader(classname="weka.core.converters.ArffLoader")
        data = loader.load_file(data_dir, class_index="second")

        # Assuming the class attribute is the second one (index 1)
        # data.set_class_index(1)

        # Classifier setup
        classifier = Classifier(classname=classifier_name)
        if classifier_options:
            classifier.options = classifier_options

        # Now use the data object
        classifier.build_classifier(data)

        print(classifier)

        # Evaluate model on train/test split
        evaluation = Evaluation(data)
        pout = PredictionOutput(classname="weka.classifiers.evaluation.output.prediction.PlainText")
        evaluation.crossvalidate_model(classifier, data, 20, Random(10))
        print(evaluation.summary())

        # Record the end time
        end_time = time.time()

        # Calculate the duration
        duration = end_time - start_time
        print(f"Time taken: {duration} seconds")
    finally:
        # Stop JVM after use
        jvm.stop()