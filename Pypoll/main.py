import os
import csv

filepath = os.path.join("Resources","election_data.csv")

with open (filepath,'r') as electiondata:

    csvreader = csv.reader(electiondata ,delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    total_votes = []   
#Total number of votes 
    for row in csvreader :
      total_votes.append(row[0])
      print(total_votes)



