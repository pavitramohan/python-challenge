import os
import csv

cereal_csv = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("..", "Resources", "output.txt")
candidates = {}
totalVotes = 0
winningCount = 0
# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    
    # Read through each row of data after the header
    for row in csvreader:

        totalVotes += 1

        # Convert row to float and compare to grams of fiber
        try:
            candidates[row[2]] += 1
        
        except KeyError:
            candidates[row[2]] = 1


lines = "Election Results " + "\n" + \
            "-------------------"+ "\n" + \
            "Total Votes: " + str(totalVotes) + "\n" + \
            "-------------------"+ "\n" 
for x in candidates:
    lines += x + ": " +  str(round(candidates[x] / totalVotes * 100, 3)) + " % (" + str(candidates[x]) + ")" + "\n"
    if (candidates[x] > winningCount):
        winningCount = candidates[x]
        winner = x

lines +=  "-------------------"+ "\n" + \
           "Winner: " + winner + "\n" + \
           "-------------------"
print(lines)

with open(output_file, 'w') as text:

   # Print the contents of the text file
    text.write(lines)
