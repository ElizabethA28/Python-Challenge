# Dependencies 
import csv
import os

# Store file path
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")
print(csvpath)


# Open and read file
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=".")
    first_row = next(csvreader)
    print(csvreader)

    # Read the header rows
    csv_header = next(csvreader)

    #skip the header rows
    header = next(csvreader)

    # track the data
    months = []
    profit_loss_changes = []
    count_months = 0
    net_profit_loss = 0
    previous_month_profit_loss = 0
    current_month_profit_loss = 0
    profit_loss_change = 0



    # Read through the first row after the header
    for row in csvreader:


        # Calculate total number of months
        total_months = total_months + 1


       # Net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss

        else:

            # The changes in "Profit/Losses" over the entire period
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss
            previous_month_profit_loss = current_month_profit_loss

        #sum and average of the changes in "Profit/Losses" over the entire period
        sum_profit_loss = sum(profit_loss_changes)
        average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

        # greatest increase and greatest decrease in "Profit/Losses" over the entire period
        greatest_change = max(profit_loss_changes)
        lowest_change = min(profit_loss_changes)

        # The greatest increase in profits (date and amount) over the entire period
        greatest_month_index = profit_loss_changes.index(greatest_change)
        lowest_month_index = profit_loss_changes.index(lowest_change)

        # Assign best and worst date
        best_date = months[greatest_month_index]
        worst_date = months[lowest_month_index]
        

# Print financial summary
print("Financial Analysis")
print("-----------------------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  $ {net_profit_loss}")
print(f"Average Change:  $ {average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_date} ($ {greatest_change})")
print(f"Greatest Decrease in Losses:  {worst_date} ($ {lowest_change})")

# Export file
output = os.path.join ("AnalysisL", "budget_summary.txt")
file = open(output, "w")
file.write(print_statement)