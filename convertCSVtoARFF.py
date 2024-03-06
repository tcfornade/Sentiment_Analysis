import csv
import os

fileToRead = "test.csv"  # csv file name or absolute path to be open.
fileToWrite = "test.arff"  # name as how you'll save your arff file.
relation = "textID text sentiment Time_of_Tweet Age_of_User Country Population Land_Area Density"  # how you'll like to call your relation as.

# Opening and Reading a CSV file
with open(fileToRead, 'r') as f:
    reader = csv.reader(f)
    allData = list(reader)
    attributes = allData[0]

totalCols = len(attributes)
totalRows = len(allData)

# Add a '0' for each empty cell
for i in range(totalRows):
    allData[i] += ["0"] * (totalCols - len(allData[i]))

# Check for commas or blanks and add single quotes
for i in range(1, totalRows):
    allData[i] = [value.lower() for value in allData[i]]
    allData[i] = [value.rstrip(os.linesep).rstrip("\n").rstrip("\r") if "\r" in value or '\r' in value or "\n" in value or '\n' in value else
                  "'" + value + "'" if not value.replace('.', '').replace('-', '').isdigit() else value
                  for value in allData[i]]

# Write ARFF file
with open(fileToWrite, 'w') as writeFile:
    # Show comments
    writeFile.write("%\n% Comments go after a '%' sign.\n%\n")
    writeFile.write("%\n% Relation: " + relation + "\n%\n%\n")
    writeFile.write("% Attributes: " + str(totalCols) + " " * 5 + "Instances: " + str(totalRows - 1) + "\n%\n%\n\n")

    # Show Relation
    writeFile.write("@relation " + relation + "\n\n")

    # Show Attributes
    for attribute in attributes:
        writeFile.write("@attribute '" + attribute + "' numeric\n")

    # Show Data
    writeFile.write("\n@data\n")
    for i in range(1, totalRows):
        writeFile.write(','.join(allData[i]) + "\n")

print(fileToWrite + " was converted to " + fileToRead)
