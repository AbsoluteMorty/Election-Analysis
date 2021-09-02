import csv
import os

#assign a variable for the file to load and the path
fileToLoad = os.path.join("Resources", "election_results.csv")
election_data = open(fileToLoad, 'r')

#open the election result and read the file
with open(fileToLoad) as election_data:

    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the new file as a txt file
with open(file_to_save, "w") as txt_file:

    # write three counties to the file
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson ")

