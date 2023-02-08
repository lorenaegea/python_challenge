import os
import csv

# store the relative file path as 'Resources/budget_data.csv'
budgetDataCsv = os.path.join("Resources", "budget_data.csv")

# use with open command to read the .csv file
with open(budgetDataCsv) as csvFile:

    # set up the reader for the csv file
    csvReader = csv.reader(csvFile, delimiter=',')

     # read the row of headers
    csvHeader = next(csvReader)

    # calculate the total number of months included in the dataset
    months = []
    monthsTotal = 0 

     # calculate the net total amount of "Profit/Losses" over the entire period
    netTotal = 0

    # calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
    netChange = []
    previousNetChange = 0
    # find the greatest increase in profits (date and amount) over the entire period
    greatestIncrease = 0
    greatestIncreaseDate = ""

    # find the greatest decrease in profits (date and amount) over the entire period
    greatestDecrease = 1000000000000000000
    greatestDecreaseDate = ""

    for row in csvReader:
        months.append(row[0])
        monthsTotal += 1

        netTotal += int(row[1])

        netChange.append(int(row[1]) - previousNetChange)
        previousNetChange = int(row[1])

# print(months)

for i in netChange:
    if float(i) > greatestIncrease:
        greatestIncrease = float(i)
        index1 = netChange.index(float(i))
        greatestIncreaseDate = months[index1]

    if float(i) < greatestDecrease:
        greatestDecrease = float(i)
        index2 = netChange.index(float(i))
        greatestDecreaseDate = months[index2]

    # define function to calculate the total of netChanges 
def total(list):
    total = 0
    for i in list:
        total += i
    return total

averageChange = total(netChange[1:]) / len(netChange[1:])

print("\nFinancial Analysis \n----------------------------")
print(f"Total months: {monthsTotal}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange: .2f}") 
print(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease: .0f})")
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease: .0f})\n")

# export text file with the results
file_to_save = os.path.join("analysis", "financial_analysis.txt")

with open(file_to_save, "w") as txt_file:

    budget_results = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total months: {monthsTotal}\n"
    f"Total: ${netTotal}\n"
    f"Average Change: ${averageChange: .2f}\n" 
    f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease: .0f})\n"
    f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease: .0f})\n")

    txt_file.write(budget_results)