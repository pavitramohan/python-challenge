import os
import csv

cereal_csv = os.path.join("..", "Resources", "budget_data.csv")
output_file = os.path.join("output.txt")

# Open and read csv
with open(cereal_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    totalRowsCount = 0
    totalProfitLoss = 0
    totalChange = 0
    greatestChangeProfits = 0
    greatestDecreaseProfits = 0

    previousValue = 0
    presentChange = 0

    # Read through each row of data after the header
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        totalRowsCount += 1
        totalProfitLoss += int(row[1])

        if(totalRowsCount != 1):
            presentChange = int(row[1]) - previousValue
        totalChange += presentChange
        previousValue = int(row[1])

        if(presentChange > greatestChangeProfits):
            greatestChangeProfits = presentChange
            greatestIncreaseProfitsMonth = row[0]
        if(presentChange < greatestDecreaseProfits):
            greatestDecreaseProfits = presentChange
            greatestDecreaseProfitsMonth = row[0]


lines = "Financial Analysis " + "\n" + \
            "-------------------"+ "\n" + \
            "Total Months: " + str(totalRowsCount) + "\n" + \
            "Total : " + str(totalProfitLoss)  + "\n" + \
            "Average  Change : " + str(totalChange/(totalRowsCount -1))  + "\n" + \
            "Greatest Increase in Profits : " + str(greatestIncreaseProfitsMonth) + " (" +str(greatestChangeProfits) + ") " + "\n" + \
            "Greatest Decrease in Profits : " + str(greatestDecreaseProfitsMonth) + " (" + str(greatestDecreaseProfits) + ")" 

print(lines)

with open(output_file, 'w') as text:

   # Print the contents of the text file
    text.write(lines)
