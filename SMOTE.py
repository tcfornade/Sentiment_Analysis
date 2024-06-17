


import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder

# Load the original dataset
data = pd.read_csv("dataSet/sentiment_analysis_5%_data.csv")

# Extract columns to be ignored during SMOTE
columns_to_ignore = ['source', 'review_description', 'review_date']
ignored_columns_data = data[columns_to_ignore]

# Drop columns to be ignored during SMOTE
data = data.drop(columns_to_ignore, axis=1)

# Encode categorical variables if needed
label_encoder = LabelEncoder()
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])

# Separate features and target variable
X = data.drop('sentiment', axis=1)
y = data['sentiment']

# Apply SMOTE
smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)

# Convert back to DataFrame
resampled_data = pd.DataFrame(X_resampled, columns=X.columns)
resampled_data['sentiment'] = y_resampled

# Concatenate ignored columns back to the resampled dataset
resampled_data_with_ignored_columns = pd.concat([resampled_data, ignored_columns_data], axis=1)

# Reorder columns
resampled_data_with_ignored_columns = resampled_data_with_ignored_columns[['source', 'review_description', 'rating', 'review_date', 'sentiment']]

# Save the resampled dataset to a new CSV file
resampled_data_with_ignored_columns.to_csv('resampled_dataset.csv', index=False)
