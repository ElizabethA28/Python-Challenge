# Dependencies 
import csv
import os

# Store file path
csvpath = os.path.join("..", "Resources", "budget_data.csv")
print(csvpath)

# track the  data
total_months = 0
net_total = 0 
previous_profit = None
changes = []
dates = []
profit_losses = 0


# Open and read the csv
with open(csvpath) as financial_data: 
    reader = csv.reader(financial_data)
    
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    net_total += int(first_row[1])
    previous_profit = int(first_row[1])

    # Track the total change
    total_months += 1
   

    # Track the net change
    net_total += profit_losses

    # Calculate changes in "Profit/Losses"
    if previous_profit is not None:
        change = profit_losses - previous_profit
        changes.append(change)
        dates.append(dates)
        previous_profit = profit_losses


        # Calculate the greatest increase in profits (month and amount)    
    if changes:
        greatest_increase = max(changes)
        greatest_increase_date = dates[changes.index(greatest_increase)]
        greatest_decrease = min(changes)
        greatest_decrease_date = dates[changes.index(greatest_decrease)]
        average_change = sum(changes) / len(changes)


# Generate the output summary
summary = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
    )

# Print the output
print(summary)

# Write the results to a text file
with open("Financial_Results", 'w') as txtfile:
        txtfile.write(summary)