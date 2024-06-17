import pandas as pd

def convertCSVtoARFF(fileIn, fileOut):

  data = pd.read_csv(fileIn)

  with open(fileOut, "w", encoding='utf-8') as f:
    # Adaugarea liniei @relation
    f.write("@relation Threads_Reviews\n\n")
    
    for column in data.columns[:-1]:  # Exclude last column
        if (column == 'rating'):
            f.write("@attribute rating numeric\n")
        else:
            f.write(f"@attribute {column} string\n")
    # f.write("@attribute sentiment {1, 0, 2}\n\n")  # Last attribute
    f.write("@attribute sentiment {positive, negative, neutral}\n\n")  # Last attribute

    f.write("@data\n")


    for index, row in data.iterrows():
       row_values = []
       for value in row.values[:-1]:
        if isinstance(value, str) :
            row_values.append(f"'{value}'")
        else:
            row_values.append(str(value))

    # Convert the sentiment to str
       sentiment = str(row.values[-1])

    # Append sentiment without quotes
       row_values.append(sentiment)

    # Convert all values in row_values to strings
       row_values = [str(val) for val in row_values]

       f.write(",".join(row_values) + "\n")



def convertCSVtoARFF_forBOW(fileIn, fileOut):
# Citirea datelor CSV într-un DataFrame pandas
  data = pd.read_csv(fileIn)

# Salvarea datelor în format ARFF cu adăugarea manuală a liniei @relation
  with open(fileOut, "w", encoding='utf-8') as f:
    # Adăugarea liniei @relation
    f.write("@relation Threads_Reviews\n\n")

    f.write("@attribute rating numeric\n")
    f.write("@attribute sentiment {positive, negative, neutral}\n")

# Identify the index of the "sentiment" column
    sentiment_index = data.columns.get_loc('sentiment')

        # Adding attribute definitions for each column after the "sentiment" column
    for column in data.columns[sentiment_index + 1:]:
        f.write(f"@attribute {column} numeric\n")

    f.write("@data\n")


    for index, row in data.iterrows():
       row_values = []
       for value in row.values[:-1]:
        if isinstance(value, str) :
            row_values.append(f"'{value}'")
        else:
            row_values.append(str(value))

    # Convert the sentiment to str
       sentiment = str(row.values[-1])

    # Append sentiment without quotes
       row_values.append(sentiment)

    # Convert all values in row_values to strings
       row_values = [str(val) for val in row_values]

       f.write(",".join(row_values) + "\n")





#-----------------------------------------------------------------------------------------

def convertCSVtoARFF_forRandomForest_training(fileIn, fileOut):
# Citirea datelor CSV într-un DataFrame pandas
  data = pd.read_csv(fileIn)

# Salvarea datelor în format ARFF cu adăugarea manuală a liniei @relation
  with open(fileOut, "w", encoding='utf-8') as f:
    # Adăugarea liniei @relation
    f.write("@relation Threads_Reviews\n\n")

    f.write("@attribute rating numeric\n")
    f.write("@attribute sentiment {positive, negative, neutral}\n")

# Identify the index of the "sentiment" column
    sentiment_index = data.columns.get_loc('sentiment')

        # Adding attribute definitions for each column after the "sentiment" column
    for column in data.columns[sentiment_index + 1:]:
        f.write(f"@attribute {column} numeric\n")

    f.write("@data\n")


    for index, row in data.iterrows():
       row_values = []
       for value in row.values[:-1]:
        if isinstance(value, str) :
            row_values.append(f"'{value}'")
        else:
            row_values.append(str(value))

    # Convert the sentiment to str
       sentiment = str(row.values[-1])

    # Append sentiment without quotes
       row_values.append(sentiment)

    # Convert all values in row_values to strings
       row_values = [str(val) for val in row_values]

       f.write(",".join(row_values) + "\n")

