import csv
import os

budget_data = os.path.join("Resources","budget_data.csv")
output_budget_data = os.path.join("analysis", "budget_analysis.txt")

# Initialize variables needed from the ReadMe
totalMonths = 0
netTotal = 0
averageChanges = 0
monthChangeList = []
netChangeList = []
# Initialize greatest increase and decrease as lists so they can store the month and its associated numeric value, respectively
greatestProfitsIncrease = ["", 0]
greatestProfitsDecrease = ["", 999999999999999999999999999]

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Initialize the first row of data to the next row after the header
    first_row = next(csvreader)
    # Increment totalMonths
    totalMonths = totalMonths + 1
    # Initialize netTotal with second cell of first non-header row
    netTotal = netTotal + int(first_row[1])
    # Initialize netPreviousRow as the value from the first non-header row to prepare for it to be referenced by the loop
    netPreviousRow = int(first_row[1])

#   Loop through data
    for row in csvreader:
        # Increment totalMonths
        totalMonths = totalMonths + 1
        # Increment netTotal with integer value of cell 2 of current row
        netTotal = netTotal + int(row[1])

        netChange = int(row[1]) - netPreviousRow
        # Set net previous row to current row in loop cell 2 so we don't keep using the value from the second row
        netPreviousRow = int(row[1])
        netChangeList = netChangeList + [netChange]
        monthChangeList = monthChangeList + [row[0]]

        #monthOfChange = monthOfChange + row[0]
        
        # Calculate greatest increase and insert it and its associated month into the greatestProfitsIncrease dictionary
        if netChange > greatestProfitsIncrease[1]:
            greatestProfitsIncrease[0] = row[0]
            greatestProfitsIncrease[1] = netChange

        # Performing same calculation for decrease
        if netChange < greatestProfitsDecrease[1]:
            greatestProfitsDecrease[0] = row[0]
            greatestProfitsDecrease[1] = netChange

netMonthlyAverage = sum(netChangeList) / len(netChangeList)

summary = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${netTotal}\n"
    f"Average Change: ${netMonthlyAverage:.2f}\n"
    f"Greatest Increase in Profits: {greatestProfitsIncrease[0]} (${greatestProfitsIncrease[1]})\n"
    f"Greatest Decrease in Profits: {greatestProfitsDecrease[0]} (${greatestProfitsDecrease[1]})"
)

with open(output_budget_data, "w+") as outputFile:
    outputFile.write(summary)

print(summary)