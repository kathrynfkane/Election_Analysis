# Election_Analysis

## Project Overview
An election commission in Colorado has tasked me with performing an audit on their local election in order to determine the winner as well as analyze the outcomes by county. They requested the following information:
<br/>
* Calculate total number of votes
* Get a complete list of candidates who received votes
* Calculate the total number of vates each candidate won
* Calculate the percentage of votes each candidate won
* The winner of the election based on popular vote
* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout
<!-- end of the list -->
In order to find these values, I used Python 3 to read the election data and perform my analysis. 
<br/>
## Election Audit Results
* **Total Votes**: 369,711
* **County Votes**:
  * Jefferson:10.5%, (38,855 votes)
  * Denver:82.8%, (306,055 votes)
  * Arapahoe:6.7%, (24,801 votes)
  <!-- end of the list -->
* **Largest County turnout:** Denver
* **Candidate results**
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* **Winner**: Diana DeGette
  * Vote Count: 272,892
  * Percentage of votes: 73.8%
  
## Election-Audit Summary 
<br/>
The script I used to perform the audit on this election is easy to use and modify. I recommend using it in future elections as it eases the process of calculating results. One aspect of the code that is easily modifiable to another election is the code to read and open the csv file. In the script pictured below, I used dependencies to create a path to the file and read it. Dependencies are programming script that has been writen by someone else. The "os" module is used when creating an indirect path to a file by allowing the user to act within their operating system. As we can see in the code below, you must import this module. I then declared a variable "file_to_load" and referenced the path to the file. The syntax for the path may be modified to reflect where the file is being kept on that computer. <br/>
<<<<<<image>>>>>>>
I then used the with open() function to read the file. This line of code can be used in another election audit as well. See below. <br/>
Additionally, the code can be modified if there was additional variables that the election commission wanted account for. I used if statements to count votes both per candidate and per county. If there were another variable in the election data, for which the commission wanted to track votes for we could amend the if statements to tally votes. *i.e: perhaps in a different election they want to track votes for age groups of voters.* See below for an example of how to construct the if statement and notice that I keep the same structure while only changing the variable names for what I want to tally votes in relation to. <br/>
 
 
 
