import os
import csv
import operator

#Reading the CSV File

csvpath = os.path.join("..","Resources","budget_data.csv")
 

with open(csvpath,'r') as budgetfile:
 
    csvreader = csv.reader(budgetfile ,delimiter =",")
    print(csvreader)

# printing the first header line
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')
    total = 0.0
#Printing the title of the file 

    print("Financial Analysis")
    print("-------------------------------------------------")

#Saving the months in a seperate list   
    months = []
    net_change =[]

    for row in csvreader:
        months.append(row[0])
        total +=int(row[1])

        if 
        net.change.append(row[1])
       
            
    print(change)
    print(f'Total Months:',len(months))
    print(f'Total :$',total)
    #print(f'Average Change:',total/len(months) )
    

# Calculating Average change
  




    
  
