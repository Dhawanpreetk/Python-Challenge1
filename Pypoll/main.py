import os
import csv

candidates = []
votes = {}
total= 0
winning_count = 0
winning_percentage = 0
winner = " "
percentage = 0   
result = {}
unique_candidate = []

# Giving the file path 
filepath = os.path.join("Resources","election_data.csv")

# Reading the csv file
with open (filepath,'r') as electiondata:

    csvreader = csv.reader(electiondata ,delimiter=',')
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')
    
    
    #Candidates lists for storing number of counts of votes and number of times candidates appeared
    
 # for loop to loop in each row of data after the header

    for row in csvreader:
      
     # total number of votes   
      total += 1
     
      name = row[2]

    
    # Checking if the name is already in the candidates list if not adding it to the list and adding the vote count
        
      if name not in candidates:
          candidates.append(name)
          votes[name] = 0
         
      
      votes[name] += 1

# Calculating the percentages
       
    for candidates in votes:
        vote_candidates = votes[candidates]

        
        results = (f'{candidates}: {percentage:,.2f}% ({vote_candidates:})\n')

         
        #print(type(results))

        if(vote_candidates> winning_count):
    
           winning_count = vote_candidates
           winner = candidates
 
 # printing the results
           
print("Election Results")
print("--------------------------------------------------------------------")   
print('Total votes',total) 
print("--------------------------------------------------------------------") 
for candidates in votes:
  vote = votes.get(candidates)
  percentage = float(vote) / float(total) * 100
  (f'{candidates}: {percentage:,.2f}% ({vote:})\n')
 
   #voter_output = f('Candidates')
  print(f'{candidates}: {percentage:,.2f}% ({vote:})\n')
print("--------------------------------------------------------------------")  
print(f'Winner:', winner)    
        





