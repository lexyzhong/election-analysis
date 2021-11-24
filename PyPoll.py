#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write("\n------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")

with open(file_to_load, 'r') as election_data:
    
    #Perform Analysis
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Prrint each row in the CSV file
    headers = next(file_reader)
    print(headers)
    
    for row in file_reader:
        print(row)
    
    # Total number of votes cast
    # A complete list of candidates who received votes
    # Total number of votes each candidate received
    # Percentage of votes each candidate won
    # The winner of the election based on popular vote
