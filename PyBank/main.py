import csv
import os


csvpath = "budget_data.csv"

#read the file and convert to dictionary
with open (csvpath, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)   
    
    # Set variables 
    
    count = 0
    profitloss = []
    date = []
    
    
    for row in csvreader:
        
        profitloss.append(int(row['Profit/Losses']))
        date.append(row['Date'])
    
        #The total number of months included in the dataset
        count += 1
        
        # The total net amount of "Profit/Losses" over the entire period
        netamount = sum(profitloss)
        
        change = [profitloss[i] - profitloss[i-1] for i, value in enumerate(profitloss[1:], 1)]

        
        
 #Zip date and change lists
    
    my_dict = dict(zip(date, change))
    
 #Find min and max

    maxprofit = max(zip(my_dict.keys(), my_dict.values()))
    minprofit = min(zip(my_dict.keys(), my_dict.values()))

    
 # The average change in "Profit/Losses" between months over the entire period            
    avgchange = sum(change)/len(change)

    #Output Summary
    
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: ", count)
    print("Total: ", netamount)
    print("Average Change: ", avgchange)
    print("Greatest Increase in Profits: ", maxprofit)
    print("Greatest Decrease in Profits: ",minprofit)


# Open the file using "write" mode. Specify the variable to hold the contents

with open("main.txt", "w") as f:
    f.write("Financial Analysis")
    f.write("------------------------")
    f.write("Total Months: " + str(count))
    f.write("Total: " + str(netamount))
    f.write("Average Change: " + str(avgchange))
    f.write("Greatest Increase in Profits: " + str(maxprofit))
    f.write("Greatest Decrease in Profits: " + str(minprofit))
    f.write("/n")