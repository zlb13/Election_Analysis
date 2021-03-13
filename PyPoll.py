# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votese each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os.path

# Assign a variable for the file to load and the path

file_to_load = './Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: read and analyze the data
     print(election_data.read())


# Create a filename variable to direct or indirect path to the file
# assign a variable to save the file to path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file

open(file_to_save, "w")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

# Write some data to the file
txt_file.write("Hello World")

# Write three counties to the file
txt_file.write("Arapahoe\nDenver\nJefferson")

# Read the file object with the reader function
file_reader = csv.reader(election_data)

# (another way to Print each row in the CSV file
for row in file_reader
    print(Row)

# Print the header row
headers = next(file_reader)
print(headers)


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and primint the header row.
 headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # 2. add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
     candidate_name = row[2]
        # if candidate does  not mathch any existing candidate
        if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list
        candidate_options.append(candidate_name)

# Print the candidate list

    print(candidate_options)

    #3. Print the total votes
    print(total_votes)

    

#declare empty dictionary
    candidate_votes = {}


