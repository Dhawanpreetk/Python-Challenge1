import os
import csv

filepath = os.path.join("Resources","election_data.csv")

with open (filepath,'r') as electiondata:

    csvreader = csv.reader(electiondata ,delimiter=',')
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')
    total= 0
    
    #Candidates lists for storing number of counts of votes and number of times candidates appeared
    candidates = []
    votes = []
    Charles =[]
    Diana = []
    Raymon = []

 # for loop to loop in each row of data after the header

    for row in csvreader :
      candidates.append(row[2])
      votes.append(row[0])
     
     # total number of votes   
      total += 1

      
      for name in candidates:
         
       if name =="Charles Casper Stockham":
        Charles.append(candidates) 
        votes_charles = len(Charles) 

       elif name == "Diana DeGette":
         Diana.append(candidates)
         votes_diana = len(Diana)
       
       else: 
          Raymon.append(candidates)
          votes_raymon = len(Raymon)

    percentage_charles = round(((votes_charles / total) * 100), 2)
    percentage_diana = round(((votes_diana / total) * 100), 2)
    percentage_raymon = round(((votes_raymon / total) * 100), 2)

print(f'Election Analysis')
print("----------------------------------------------------------------------------------")
print(f'total votes :',total)

print(f"Charles: %{percentage_charles} ({votes_charles})")   
print(f"Charles: %{percentage_diana} ({votes_diana})")   
print(f"Charles: %{percentage_raymon} ({votes_raymon})")   




