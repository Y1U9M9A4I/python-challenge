import os
import csv

monthly_change = []
profit =[] 
dates = []
budget_csv = os.path.join('PyBank/Resources/budget_data.csv')

# Variable initialization

count = 0 
prof_total = 0 
prof_change = 0
prof_init = 0

# open CSV file 

with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter= ",")
    budget_header = next(budget_reader)

# Ask 

    for row in budget_reader:
        count += 1
        dates.append(row[0])
        profit.append(int(row[1]))
        prof_total += int(row[1])

        #calc monthly changes 

        if count > 1: 
            monthly_changes = profit[count - 1] - profit[count - 2]
            monthly_change.append(monthly_changes)

        # profit average calculation 

        if len(monthly_change) > 0:
            prof_avg_change = sum(monthly_change) / len (monthly_change)
        else: 
            prof_avg_change = 0

        # Max increase and decrease in profit + day of 

    max_in = max(monthly_change)
    max_dec = min(monthly_change)

    # index of greatest increase and decrease in profit

    max_in_index = monthly_change.index(max_in)
    max_dec_index = monthly_change.index(max_dec)

# Get the corresponding dates for the greatest increase and decrease in profits (change starts AFTER seond month involved = +1)
inc_date = dates[max_in_index + 1] 
dec_date = dates[max_dec_index + 1]  

print("Financial Analysis")
print("----------------------------")
print("Total Months:" + str(count))
print("Total Profits:" "$" + str(prof_total))
print("Average Change:" "$" + str(int(prof_avg_change)))
print("Greatest Increase in Profits:" + str(inc_date) + "($" + str(max_in)+")")
print("Greatest Decrease in Profits:" + str(dec_date) + "($" + str(max_dec)+")")

export_path = "PyBank/Analysis/budget.txt"

with open(export_path, "w") as file: 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months:" + str(count) + "\n")
    file.write("Total Profits:" "$" + str(prof_total) + "\n")
    file.write("Average Change:" "$" + str(int(prof_avg_change)) + "\n")
    file.write("Greatest Increase in Profits:" + str(inc_date) + "($" + str(max_in)+")\n")
    file.write("Greatest Decrease in Profits:" + str(dec_date) + "($" + str(max_dec)+")\n")

    print("Bank Budget results have been saved to: " + "PyBank/Analysis")    



            




