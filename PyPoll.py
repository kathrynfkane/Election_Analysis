# #The data we need to retrieve.
# #1.The total number of votes cast
# #2. A complete list of candidates who received votes
# #3. The percentage of votes each candidate won
# #4. The total number of votes each candidate won
# #5. The winner of the election based on popular vote. 
# # Resources/election_results.csv
# #Import the datetime class from the datetime module
# # import datetime as dt
# # #Use the now() attribute on the datetime class to get the present time
# # now = dt.datetime.now()
# # #print the present time
# # print("The time right now is", now)
# #Assign a variable for the file to load and the path
# # file_to_load = 'Resources/election_results.csv'
# # # #open the election results and read the file.
# # # election_data = open(file_to_load, 'r')
# # # #To do: Perform Analysis

# # # #Close the file
# # # election_data.close()
# # with open(file_to_load) as election_data:
# #     #to do: perform analysos
# #     print(election_data)
# import csv
# import os
# file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# open(file_to_save,"w")
# #create a filename or variable to a direct or indirect path to the file
# file_to_save = os.path.join("analysis","election_analysis.txt")
# #using the with statement open the file as a text file
# outfile = open(file_to_save, "w")
# #write some data to the file
# outfile.write("Hello World")
# #Close the file
# outfile.close()
# # create filename variable to a direct or indirect path to the file
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Hello World!")

# file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Araphoe\nDenver\nJefferson")
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#candidate options
candidate_options = []
#declare empty dictionary
candidate_votes = {}
#winnin candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #Read and Print the header row. 
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's vote count
        candidate_votes[candidate_name]+= 1
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        if(votes>winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        #Print the winning candidate, vote count, and percentage
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    winning_candidate_summary = (
        f"---------------------\n"
        f"winner: {winning_candidate}\n"
        f"winning vote count: {winning_count:,}\n"
        f"----------------------------------------\n")
    txt_file.write(winning_candidate_summary)




