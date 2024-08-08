import os
import csv

election_csv = os.path.join('PyPoll/Resources/election_data.csv')

count = 0
candidates = [] 
cunique = []
vcount = [] 
vperc = [] 

with open(election_csv, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
        
    # Ask 

    for row in csvreader: 
        count = count + 1
        candidates.append(row[2])
    
    for x in set(candidates):
        cunique.append(x)

        cand_total = candidates.count(x)
        vcount.append(cand_total)

        cand_perc = (cand_total/count)*100 
        vperc.append(cand_perc)

    winner_count = max(vcount)
    winner = cunique[vcount.index(winner_count)]

print("--------------------")
print("Election Report")
print("--------------------")
print("Total Number of Votes:" + str(count))

for i in range(len(cunique)):
    print(cunique[i]) + ":" + str(vperc[i]) + "% (" + str(count[i]) + ")"
print("The winner is..." + winner)

