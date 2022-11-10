# import os and csv files
import os
import csv


# creating csv path

election_data_path = os.path.join("C:\\Users\\ryche\\Desktop\\python-challenge\\Resources\\election_data.csv")

# set variables
total_votes = 0
candidates = []
vote_counts = []

# open and read csv file
with open(election_data_path,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    # skip the header row
    line = next(csvreader,None)

    # read through each row of data after header
    for line in csvreader:

        # add to total number of votes
        total_votes = total_votes + 1

        # candidate voted for
        candidate = line[2]

        
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

# calculate percentage of vote for  candidates and for the winner
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/total_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

# print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


 # output to a final text file
text_path = os.path.join("C:\\Users\\ryche\\Desktop\\python-challenge\\PyPoll\\final.txt")
with open(text_path, 'w') as file:
 file.write("Election Results\n")
 file.write("--------------------------\n")
 file.write(f"Total Votes: {total_votes}\n")
 for count in range(len(candidates)):
    file.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
 file.write("---------------------------\n")
 file.write(f"Winner: {winner}\n")
 file.write("---------------------------\n")
 file.close()
    



    



