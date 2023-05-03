import os
import csv


#Reading the CSV File

csvpath = os.path.join("Resources","budget_data.csv")
 

with open(csvpath,'r') as budgetfile:
 
    csvreader = csv.reader(budgetfile ,delimiter = ",")
    print(csvreader)

# printing the first header line
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    total = 0.0
#Printing the title of the file 

#Saving the months in a seperate list   
# intialising the variables  
    months = []
    profits = []
    profit = 0
    change = 0
    previous_month = 0
    Date = 0
    change_list = []
    first_row =next(csvreader)       #skipping the first row
    months.append(first_row[0])
    profit = int(first_row[1])
    profits.append(profit)
    total +=int(first_row[1])
    previous_month = profit
    
    for row in csvreader:
        months.append(row[0])
        profit = int(row[1])
        profits.append(profit)
        total += profit
    
        
        # Calculating the Change per month

        change = profit - previous_month
        change_list.append(change)

        previous_month = profit
       
        #Calculating the Greatest increase and decrease in profits
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)  

    max_index = change_list.index(greatest_increase)
    min_index = change_list.index(greatest_decrease)

    Max_month = months[max_index+1] 
    Min_month = months[min_index+1]


    # Calculating and printing the Average Change per month
    print("Financial Analysis")
    print("-------------------------------------------------------------------------------------------------")
    print(f'Total :$',total)
    print(f'Total Months:',len(months))
    print(f'Average Change:' ,round(sum(change_list)/len(change_list),2))
    print(f'Greatest increase in Profits',Max_month,(greatest_increase))
    print(f'Greatest decrease in Profits',Min_month,greatest_decrease)
    
   
    






    
  
