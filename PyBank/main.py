import os
import csv

# Define the path to the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Open the CSV file and read the data
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    data = [(row[0], int(row[1])) for row in reader]

# Calculate the total number of months
num_months = len(data)

# Calculate the net total amount of Profit/Losses
net_total = sum(row[1] for row in data)

# Calculate the changes in Profit/Losses over the entire period
changes = [data[i+1][1] - data[i][1] for i in range(len(data)-1)]

# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Calculate the greatest increase and decrease in profits
max_increase = max(changes)
max_decrease = min(changes)
max_increase_date = data[changes.index(max_increase)+1][0]
max_decrease_date = data[changes.index(max_decrease)+1][0]

# Print the results to the terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# Write the results to a text file
with open('analysis_data.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {num_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")
