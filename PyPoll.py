
import csv
from functools import total_ordering
import os

#Assign a variable to load a file from path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to load a file from path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

# candidate options
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    #read and analysze the data
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)
    #print(headers)


    for row in file_reader:
        # adds the total vote count
        total_votes += 1

        # candidates name for each row
        candidate_name = row[2]

        # if the candidate does not match any existing
        if candidate_name not in candidate_options:
            # add candidate name to the candidate list
            candidate_options.append(candidate_name)

            # begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            
        # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

print(total_votes)
print(candidate_options)
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100


    # Determine winning vote count and candidate.
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count votes and winning_percentage = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning candidate equal to the candidate's name.
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% of the votes\n")

winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)
    
#print the file object
print(election_data)


with open(file_to_save, "w") as txt_file:
    txt_file.write("counties in the Election\n")
    txt_file.write(("-" * 30) + "\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
txt_file.close()


