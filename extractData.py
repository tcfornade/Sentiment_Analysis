# import pandas as pd
from convertCSVtoARFF import convertCSVtoARFF

# df = pd.read_csv("dataSet/sentiment_analysis.csv")

# total_positive_samples = len(df[df['sentiment'] == 'positive'])
# total_negative_samples = len(df[df['sentiment'] == 'negative'])
# total_neutral_samples = len(df[df['sentiment'] == 'neutral'])

# samples_for_positive = int(0.03 * total_positive_samples)
# samples_for_negative = int(0.1 * total_negative_samples)
# samples_for_neutral = int(0.05 * total_neutral_samples)

# # Separate data based on sentiment
# positive_df = df[df['sentiment'] == 'positive'].sample(n=samples_for_positive)
# negative_df = df[df['sentiment'] == 'negative'].sample(n=samples_for_negative)
# neutral_df = df[df['sentiment'] == 'neutral'].sample(n=samples_for_neutral)

# selected_data = pd.concat([positive_df, negative_df, neutral_df])

# # Shuffle the data
# selected_data = selected_data.sample(frac=1, random_state=3).reset_index(drop=True)

# selected_data.to_csv("dataSet/sentiment_analysis_5%_data.csv", index=False)


import pandas as pd

def extract_data_from_csv():
    
# Read the CSV file into a DataFrame
 df = pd.read_csv("dataSet/sentiment_analysis.csv")

# Group the DataFrame by the 'sentiment' column and count the number of rows for each sentiment
 sentiment_counts = df['sentiment'].value_counts()

# Find the minimum count among all sentiment categories
 min_count = sentiment_counts.min()
#min_count = 500

# Sample an equal number of rows for each sentiment category
 sampled_data = pd.concat([df[df['sentiment'] == sentiment].sample(min_count) for sentiment in sentiment_counts.index])

 sampled_data = sampled_data.sample(frac=1, random_state=42)

# Save the sampled data back to a CSV file
 sampled_data.to_csv("dataSet/sentiment_analysis_5%_data.csv", index=False)

 #convertCSVtoARFF("dataSet/sentiment_analysis_5%_data.csv", "dataSet/sentiment_analysis_5%_data.arff")

# ## ---- 

# import csv
# sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}

# with open('dataSet/sentiment_analysis_5%_data.csv', mode='r', newline='', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         sentiment_counts[row['sentiment']] += 1

# print("Sentiment Counts:")
# for sentiment, count in sentiment_counts.items():
#     print(f"{sentiment.capitalize()}: {count}")
