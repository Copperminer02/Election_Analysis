# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of the candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter.
total_votes = 0

# Candidate Option
candidates_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]

    # If the candidate does not match any existing candidate
        
        if candidate_name not in candidates_options:

            # Add the candidate name to the candidate list.
            candidates_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save,"w") as txt_file:
   # Print the election results results to the terminal.    
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end=" ")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
        for candidate_name in candidate_votes:

            #Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]

            #Calculate the percntage of votes.
            vote_percentage = float(votes)/float(total_votes)*100

            # print out each candidate's name, vote count, and percentage of votes to the terminal
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)

            # Save the candidate results to the text file.
            txt_file.write(candidate_results)
            
            #Determine the winning vote count and candidate
            # Determine if the vote is greater thant the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true the set winning_count = votes and winning_percentage = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                # And, set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name

        # Print the winning candidates' results to the terminal.    
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)

     
