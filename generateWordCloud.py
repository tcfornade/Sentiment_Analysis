from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import urllib
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_word_cloud(dataFrame, sentiment_label):
    dataFrame['review_description'] = dataFrame['review_description'].astype(str)
    words = ' '.join(text for text in dataFrame['review_description'][dataFrame['sentiment']==sentiment_label])
    # combining the image with the dataset
    Mask = np.array(Image.open('threads_logo.jpg'))

# We use the ImageColorGenerator library from Wordcloud 
# Here we take the color of the image and impose it over our wordcloud
    image_colors = ImageColorGenerator(Mask)

# Now we use the WordCloud function from the wordcloud library 
    wc = WordCloud(background_color='gray', height=1500, width=4000,mask=Mask).generate(words)
# Size of the image generated 
    plt.figure(figsize=(10,20))

# Here we recolor the words from the dataset to the image's color
# recolor just recolors the default colors to the image's blue color
# interpolation is used to smooth the image generated 
    plt.imshow(wc.recolor(color_func=image_colors),interpolation="hamming")

    plt.axis('off')
    plt.show()

df = pd.read_csv("dataSet/sentiment_analysis_5%_data.csv")

generate_word_cloud(df, 'positive')
#generate_word_cloud(df, 'negative')
# generate_word_cloud(df, 'neutral')