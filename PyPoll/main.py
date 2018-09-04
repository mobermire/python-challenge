import csv
import os

csvpath = "election_data.csv"


totalvotes = 0
candidate = {}


with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader,None)
    
    for row in csvreader:
        
        
        totalvotes += 1

        if row[2] in candidate:
            candidate[row[2]] +=1
        else:
            candidate[row[2]] = 1

print ("Election Resuls")
print ("Total Votes: " + str(totalvotes))
for key , value in candidate.items():
    print (key + ": " + str((value/totalvotes * 100)) + "  (" + str(value) +")" )
print ("Winner: " + max(candidate, key=candidate.get) ) 



output = "results.txt"
with open(output, 'w') as f:
    f.write ("Election Resuls")
    f.write ("Total Votes: " + str(totalvotes))
    for key , value in candidate.items():
        f.write (key + ": " + str((value/totalvotes * 100)) + "  (" + str(value) +")" )
    f.write ("Winner: " + max(candidate, key=candidate.get) )   
            

        
        
        
        

