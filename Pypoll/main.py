#import buget_data.csv file 
import os 
import csv 

#set the path
csvpath = os.path.join ('Resources', 'election_data.csv')

#Initialize the variables' values to zero 
total_vote = 0 
khan_total_vote = 0
correy_total_vote = 0
li_total_vote = 0 
otooley_total_vote = 0 
candidates = {}


#Read the file
with open(csvpath,'r') as csvfile:
        csvreader = csv.reader(csvfile,delimiter= ',')

        #Read the header row first 
        csv_header = next(csvreader)

        #Iterate through the rows 
        for row in csvreader: 

            #Count the total votes 
            total_vote +=1 

            #conditional formatting for each candidate
            if row[2] == "Khan":
                khan_total_vote +=1 
            elif row[2] == "Correy":
                correy_total_vote +=1
            elif row[2] == "Li":
                li_total_vote +=1 
            elif row[2] == "O'Tooley":
                    otooley_total_vote +=1         
            else: 
                print("N/A")

            #convert the number into percentage 
            khan_percentage = khan_total_vote / total_vote *100
            correy_percentage = correy_total_vote / total_vote *100
            li_percentage = li_total_vote / total_vote *100 
            otooley_percentage = otooley_total_vote / total_vote *100

        #Create the dictionary using key:value pair
        candidates = {'Khan' : khan_total_vote , 'Correy': correy_total_vote, 'Li': li_total_vote, 'OTooley': otooley_total_vote}

        #Find the winner using this: max(stats, key=stats.get)
        #for key in candidates: 
        winner = max(candidates, key=candidates.get)
         
        
# Print all the values         
pypoll_analysis = (

    f"{(total_vote)}\n"
    "-------------------------------------------\n"
    f"{khan_total_vote}\n"
    "-------------------------------------------\n"
    f"Khan: {khan_percentage:.3f}% ({khan_total_vote})\n" 
    f"Correy: {correy_percentage:.3f}% ({correy_total_vote})\n"
    f"Li: {li_percentage:.3f}% ({li_total_vote})\n"
    f"O'Tooley: {otooley_percentage:.3f}% ({otooley_total_vote})\n"
    "-------------------------------------------\n"
    f"The Winner: {winner}\n"
    "-------------------------------------------\n"
)
print(pypoll_analysis)

#Export a text file 
with open("pypoll_analysis.txt",'w') as txtfile:
        txtfile.write(pypoll_analysis)