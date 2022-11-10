#import library
import os
import csv

# creating path
budget_data = os.path.join("C:\\Users\\ryche\\Desktop\\python-challenge\\Resources\\budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # calculate profit and loss
    Profit_losses = []
    months = []

    # read through each row of data after header
    for rows in csvreader:
        Profit_losses.append(int(rows[1]))
        months.append(rows[0])

    # calculate profitlosse  change
    profitlosses_change = []

    for x in range(1, len(Profit_losses)):
        profitlosses_change.append((int(Profit_losses[x]) - int(Profit_losses[x-1])))
    
    # calculate average profitlosses change
    profitlosses_average = sum(profitlosses_change) / len(profitlosses_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in profitlosses
    greatest_increase = max(profitlosses_change)
    # greatest decrease in profitlosses
    greatest_decrease = min(profitlosses_change)

    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(Profit_losses)))

    print("Average change: " + "$" + str(profitlosses_average))

    print("Greatest Increase in Profits: " + str(months[profitlosses_change.index(max(profitlosses_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[profitlosses_change.index(min(profitlosses_change))+1]) + " " + "$" + str(greatest_decrease))

    # output to a text file
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(Profit_losses)) + "\n")

    file.write("Average change: " + "$" + str(profitlosses_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[profitlosses_change.index(max(profitlosses_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[profitlosses_change.index(min(profitlosses_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()