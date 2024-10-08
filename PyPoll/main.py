import os
import csv

election_csv = os.path.join('PyPoll/Resources/election_data.csv')

# create housing lists 

count = 0
candidates = [] 
cunique = []
vcount = [] 
vperc = [] 

with open(election_csv, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
        
    # With the file in open status, iterate through rows and add the corresponding data to each of the created lists 

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

# print summary of the analyses (+ iterate through candidates to show their indiv data)

print("Election Results")
print("-------------------------")
print("Total Votes:" + str(count))
print("-------------------------")
for i in range(len(cunique)):
    print(cunique[i] + ":" + str(round(vperc[i],3)) + "% (" + str(round(vcount[i],3)) + ")")
print("-------------------------")
print("The winner is..." + winner + "!")

# export results to csv 

export_path = "PyPoll/Analysis/election_results.txt"

with open(export_path, "w") as file: 
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes:" + str(count) + "\n")
    file.write("-------------------------\n")
    for i in range(len(cunique)):
        file.write(cunique[i] + ":" + str(round(vperc[i],3)) + "% (" + str(round(vcount[i],3)) + ")\n")
    file.write("-------------------------\n")
    file.write("The winner is..." + winner + "!\n")
    print("Election results have been saved to: " + "PyPoll/Analysis")