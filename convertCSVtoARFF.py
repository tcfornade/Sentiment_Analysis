import pandas as pd
<<<<<<< HEAD
def convertCSVtoARFF(fileIn, fileOut):
# Citirea datelor CSV într-un DataFrame pandas
  data = pd.read_csv(fileIn)

# Salvarea datelor în format ARFF cu adăugarea manuală a liniei @relation
  with open(fileOut, "w", encoding='utf-8') as f:
    # Adăugarea liniei @relation
    f.write("@relation Threads_Reviews\n\n")

    f.write("@attribute rating numeric\n")
    f.write("@attribute sentiment {positive, negative, neutral}\n")

    sentiment_index = data.columns.get_loc('sentiment')
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

    # Convertire a sentimentelor to string
       sentiment = str(row.values[-1])
       row_values.append(sentiment)
       row_values = [str(val) for val in row_values]
       f.write(",".join(row_values) + "\n") #scrie in fisier

=======

# Citirea datelor CSV într-un DataFrame pandas
data = pd.read_csv("dataSet/sentiment_analysis.csv")

# Salvarea datelor în format ARFF cu adăugarea manuală a liniei @relation
with open("dataSet/sentiment_analysis_data.arff", "w", encoding='utf-8') as f:
    # Adăugarea liniei @relation
    f.write("@relation Google_Play_Reviews\n\n")

    # Adăugarea definițiilor de atribut pentru fiecare coloană
    for column in data.columns[:-1]:  # Exclude last column
        if column == 'rating':
            f.write("@attribute rating numeric\n")
        else:
            f.write(f"@attribute {column} string\n")
    f.write("@attribute sentiment {positive, negative, neutral}\n\n")  # Last attribute

    f.write("@data\n")

    # Scrierea datelor
    for index, row in data.iterrows():
        row_values = [f"'{value}'" if isinstance(value, str) else str(value) for value in row.values[:-1]]
        row_values.append(row.values[-1])  # Append sentiment without quotes
        f.write(",".join(row_values) + "\n")
>>>>>>> 240a3aa8907706a030455032fae9f8f2dab59bf8
