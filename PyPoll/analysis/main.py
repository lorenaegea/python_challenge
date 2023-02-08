import os 
import csv

# import pandas to use unique() function
import pandas as pd

# store the relative file path as 'Resources/election_data.csv'
electionDataCsv = os.path.join("Resources", "election_data.csv")

# use with open command to read the .csv file
with open(electionDataCsv) as csvFile:

     # set up the reader for the csv file
     csvReader = csv.reader(csvFile, delimiter = ",")

     # read the row of headers
     csvHeader = next(csvReader)
     
     # calculate the total number of votes cast
     votesTotal = 0

     # calculate a complete list of candidates who received votes
     # Use Pandas to read data
     electionDataCsvDF = pd.read_csv(electionDataCsv)
     # The unique method shows every element only once
     uniqueCandidates = electionDataCsvDF["Candidate"].unique()   

     #calculate how many votes each candidate received
     candidate1 = 0
     candidate2 = 0
     candidate3 = 0

     for row in csvReader:
        votesTotal += 1

        if row[2] == uniqueCandidates[0]:
            candidate1 += 1
        elif row[2] == uniqueCandidates[1]:
            candidate2 += 1
        else:
            candidate3 +=1

        totalVotes = candidate1 + candidate2 + candidate3

        c1Percent = (candidate1 / totalVotes) * 100
        c2Percent = (candidate2 / totalVotes) * 100
        c3Percent = (candidate3 / totalVotes) * 100

        allVotes = [candidate1, candidate2, candidate3]
        maxVotes = max(allVotes)
        index = allVotes.index(maxVotes)
        winner = uniqueCandidates[index]

print(f"\nElection Results \n------------------------- \nTotal Votes: {votesTotal} \n-------------------------")
print(f"{uniqueCandidates[0]}: {c1Percent: .3f}% ({candidate1})")
print(f"{uniqueCandidates[1]}: {c2Percent: .3f}% ({candidate2})")
print(f"{uniqueCandidates[2]}: {c3Percent: .3f}% ({candidate3})")
print(f"------------------------- \nWinner: {winner} \n")



# export text file with the results
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {votesTotal}\n"
    f"-------------------------\n"
    f"{uniqueCandidates[0]}: {c1Percent: .3f}% ({candidate1})\n"
    f"{uniqueCandidates[1]}: {c2Percent: .3f}% ({candidate2})\n"
    f"{uniqueCandidates[2]}: {c3Percent: .3f}% ({candidate3})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n")

    txt_file.write(election_results)