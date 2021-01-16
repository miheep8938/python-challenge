#import buget_data.csv file 
import os 
import csv 

#set the path
csvpath = os.path.join ('Resources', 'budget_data.csv')

#Set the variables with empty lists 
total_months = [] 
total_profit = []
profit_change = [] 
previous_row_PL = 0  

#Read the file
with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter= ',')
        
        #To ensure the file is on the right track
        #print(csvreader) --> <_csv.reader object at 0x00000235383CDAD8>

#Read the header row first 
        csv_header = next(csvreader)
        
        
        #To ensure it indicates the header row
        # print(f"Header: {csv_header}") --> Header: ['Date', 'Profit/Losses']

        #Iterate through the rows 
        for row in csvreader: 

                #Assign the rows representing months  
                total_months.append(row[0])

                #Assign the row representing profits 
                total_profit.append(int(row[1]))
                
                #Assign the two values to see the profit change and move to the next row 
                profit_change.append(int(row[1])- int(previous_row_PL))
                previous_row_PL = int(row[1]) 

                #Get the greatest increase and decrease value 
                greatest_increase_value = max(profit_change)
                greatest_decrease_value = min(profit_change)

                #Read through the whole rows to find the index matching with the greatest increase and decrease values  
                greatest_increase_date = profit_change.index(max(profit_change)) 
                greatest_decrease_date = profit_change.index(min(profit_change))
                
#Calculate all the values then print 
analysis_output = (
        f"Total Months: {len(total_months)}\n"
        f"Net Total Amount: {sum(total_profit)}\n"
        f"Average of Profit Change: {round(sum(profit_change[1:])/len(profit_change[1:]),2)}\n"
        f"Greatest Increase in Profits: {total_months[greatest_increase_date]} (${(greatest_increase_value)})\n"
        f"Greatest Decrease in Profits: {total_months[greatest_decrease_date]} (${(greatest_decrease_value)})"
)
print(analysis_output)

#Ensure the change calculates from the second value 
# print(profit_change[1:])

#Export a text file 
with open("analysis_output.txt",'w') as txtfile:
        txtfile.write(analysis_output)