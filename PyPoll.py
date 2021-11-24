#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize total vote counter
total_votes = 0

#Initialize candidate options list
candidate_options = []

#Declare empty dictionary for candidate vote counts
candidate_votes = {}

#Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Perform Analysis
    #Read the header row
    headers = next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

        #Retrieve candidate name
        candidate_name = row[2]

        #Determine if name is unique
        if candidate_name not in candidate_options:
            # Add to the list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        
        #Increase candidate vote count
        candidate_votes[candidate_name] +=1
     
#Print the total votes
print(f"{total_votes:,}")
    
#Print the candidate options
print(candidate_votes)
    
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Calculate percentage of votes each candidate won & winner
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes)*100

        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        txt_file.write(candidate_results)

        # Determine the winner of the election based on popular vote
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    

