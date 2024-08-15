import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(conf_matrix ):
    conf_matrix = np.array(conf_matrix, dtype=int)
    fontsize=7
    class_names = ['positive', 'negative', 'neutral']
    
    plt.figure(figsize=(4, 3))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=class_names, yticklabels=class_names,
                annot_kws={"size": fontsize})


    plt.xlabel('Clasa prezisă', fontsize=fontsize)
    plt.ylabel('Clasa adevărată', fontsize=fontsize)
 
    plt.xticks(fontsize=fontsize)  
    plt.yticks(fontsize=fontsize)

    subplot_params = {
            'left': 0.265,   
            'right': 0.688,  
            'top': 0.9,    
            'bottom': 0.365,  
     }
    plt.subplots_adjust(**subplot_params)

    plt.show()
