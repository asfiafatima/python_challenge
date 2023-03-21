import csv
import os

# Define the path to the CSV file
csv_path = os.path.join("Resources", "election_data.csv")

# Open the CSV file and read the data
with open(csv_path,'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = [row[2] for row in reader]

# Calculate the total number of votes cast
num_votes = len(data)

# Calculate the complete list of candidates who received votes
candidates = list(set(data))

# Calculate the percentage of votes each candidate won
vote_counts = [data.count(candidate) for candidate in candidates]
vote_percents = [count/num_votes*100 for count in vote_counts]

# Calculate the total number of votes each candidate won
vote_totals = dict(zip(candidates, vote_counts))

# Determine the winner of the election based on popular vote
winner = max(vote_totals, key=vote_totals.get)

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {num_votes}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_percents[i]:.3f}% ({vote_counts[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open('analysis_election.txt', 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {num_votes}\n")
    file.write("-------------------------\n")
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {vote_percents[i]:.3f}% ({vote_counts[i]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

