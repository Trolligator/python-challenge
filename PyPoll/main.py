import csv
import os

csvFile = os.path.join("Resources", "election_data.csv")

totalVotes = 0
candidateList = {}
candidateVotes = []
winner = ""
winnerVotes = 0

with open(csvFile, newline="") as file:
    csvreader = csv.reader(file, delimiter=',')


    header = next(csvreader)


    for row in csvreader:
        totalVotes+=1
        if row[2] not in candidateList:
            candidateList[row[2]]=1
        else:
            candidateList[row[2]]=candidateList[row[2]]+1

votesFile = os.path.join("output.txt")
with open(votesFile, "w") as textFile:
    textFile.write(f"Election Results \n")
    textFile.write(f"-------------------------\n")
    textFile.write(f"Total Votes: {str(totalVotes)}\n")
    textFile.write(f"-------------------------\n")
    for i in candidateList:
            votePercentage = candidateList[i] / totalVotes
            textFile.write(f"{i}: {'{:,.3%}'.format(votePercentage)} ({str(candidateList[i])})\n")
            if candidateList[i] > winnerVotes:
                winnerVotes = candidateList[i]
                winner = i
    textFile.write(f"-------------------------\n")
    textFile.write(f"Winner: {winner} \n")
    textFile.write(f"-------------------------\n")
with open(votesFile, "r") as textFile:
    print(textFile.read())
                
