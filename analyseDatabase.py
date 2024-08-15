import pandas as pd
import matplotlib.pyplot as plt


# # Replace 'your_database.csv' with your actual CSV file path
# df = pd.read_csv('dataSet/threads_reviews.csv')
# # Count occurrences of each source
# source_counts = df['source'].value_counts()
# colors = ['orange', 'blue'] 
# # # Plotting the distribution as a pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
# plt.title('Distibuția sursei datelor')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

# ------------------------ fig
# # Group by 'rating' and 'source' and count the number of entries
# grouped_df = df.groupby(['rating', 'source']).size().unstack(fill_value=0)
# colors = ['blue', 'orange']  # Adjust the colors if you have more than two sources

# # Plot the grouped data with specified colors
# ax = grouped_df.plot(kind='bar', stacked=True, figsize=(10, 7), color=colors)


# # Add labels and title
# plt.xlabel('Rating')
# plt.ylabel('')
# plt.title('Numărul de recenzii în funcție de rating și sursă')

# # Add count labels on the bars
# for container in ax.containers:
#     ax.bar_label(container)

# # Show the plot
# plt.show()



# df = pd.read_csv('dataSet/sentiment_analysis.csv')
# sentiment_counts = df['sentiment'].value_counts()
# plt.figure(figsize=(8, 8))
# plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=140)
# plt.title('Distribuția sentimentelor')
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.show()

# # Group by rating and sentiment, and count occurrences
# sentiment_by_rating = df.groupby(['rating', 'sentiment']).size().unstack(fill_value=0)
# # Plotting sentiments in function of rating using bar plots
# sentiment_by_rating.plot(kind='bar', stacked=True, figsize=(10, 6))

# # Customize the plot
# plt.title('Sentimentele în funcție de rating')
# plt.xlabel('Rating')
# plt.ylabel('Nr.')
# plt.xticks(rotation=0)  # Ensure x-axis labels are not rotated
# plt.legend(title='Sentiment', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('sentiment_analysis.csv')

# # Count occurrences of each sentiment
# sentiment_counts = df['sentiment'].value_counts()

# # Plotting the bar graph
# plt.figure(figsize=(10, 6))
# ax = sentiment_counts.plot(kind='bar', color='blue')

# # Adding numerical values on the bars
# for i, count in enumerate(sentiment_counts):
#     ax.text(i, count + 0.5, str(count), ha='center', va='bottom')

# # Adding labels and title
# plt.xlabel('Sentiment')
# plt.ylabel('Numărul de apariții')
# plt.title('Numărul de sentimente distribuit pe clase')
# plt.xticks(rotation=0)  # Ensure x-axis labels are not rotated

# # Show the plot
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('sentiment_analysis.csv')

# grouped_df = df.groupby(['rating', 'sentiment']).size().unstack(fill_value=0)

# # Calculate the total counts per rating
# total_counts = grouped_df.sum(axis=1)

# # Plotting the bar graph
# plt.figure(figsize=(12, 8))
# ax = grouped_df.plot(kind='bar', stacked=True, figsize=(7, 5))

# # Adding total numbers above each bar
# for i, total in enumerate(total_counts):
#     ax.text(i, total + 0.5, str(total), ha='center', va='bottom')

# # Adding labels and title
# plt.xlabel('Rating')
# plt.ylabel('Număr')
# plt.title('Sentimentele în funcție de rating')

# # Show the plot
# plt.show()




# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.feature_extraction.text import CountVectorizer

# # Load the CSV file into a pandas DataFrame
# df = pd.read_csv('sentiment_analysis.csv')

# # Assuming the text data is in a column named 'review_description'
# documents = df['review_description'].dropna().tolist()

# # Create BoW model
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(documents)

# # Get word frequency
# word_freq = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
# word_freq_sum = word_freq.sum().sort_values(ascending=False)

# # Plotting word frequency distribution
# plt.figure(figsize=(10, 6))
# word_freq_sum.head(20).plot(kind='bar')  # Plotting top 20 words for better visibility
# plt.xlabel('Cuvântul')
# plt.ylabel('Frecvența')
# plt.title('Distribuția de frecvență a cuvintelor')
# plt.xticks(rotation=40)
# plt.show()
