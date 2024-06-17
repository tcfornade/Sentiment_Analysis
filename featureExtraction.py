# -------- bag of words----------------

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def create_bag_of_words_from_csv(input_csv_file, output_csv_file):
  
    df = pd.read_csv(input_csv_file)

    # Fill empty strings in review_description column with a placeholder
    df['review_description'] = df['review_description'].fillna("no_review")

    # Tokenize the review descriptions
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['review_description'])

    # Create a bag of words representation
    bag_of_words = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

    # Drop the original review_description column
    df.drop(columns=['review_description'], inplace=True)

    # Concatenate bag of words with other columns
    bag_of_words = pd.concat([df, bag_of_words], axis=1)

    # Write to a new CSV file
    bag_of_words.to_csv(output_csv_file, index=False)


# ----- n-grams algorithm ----------------

