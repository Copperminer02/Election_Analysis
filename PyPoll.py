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
#Assign a variable to save teh file path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in teh CSV file.
    headers = next(file_reader)
    print(headers)
