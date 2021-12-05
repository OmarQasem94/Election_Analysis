# Election_Audit


## **Overview of Election Audit**
This project is designed to assist a Colorado board of election employye in performing an audit of the tabulated results for a US congressional precinct in Colorado. The audit entails a report of the total number of votes cast, voter turnout and percentage of votes from each county, county with the highest turonut, total number and percentage of votes for each candidate, and the winner of the election based on the popular vote. The analysis is administered using python to read a csv file which holds the election data and the results are depicted in a text file.  



## **Results of Election Audit**

#### Total Number of Votes Cast
The first objective of the analysis was to identify the total number of votes cast. This was completed by assigning a variable named total_votes and having the variable increase by one for each row in the dataset using a for loop which holds the information of a vote. The outcomes derived depicts that there were 329,711 total votes in the precinct. 

![Total_Votes](https://github.com/OmarQasem94/Election_Analysis/blob/main/Resources/Total_Votes.PNG)


#### Voter Turnout and Percentage of Votes for each County
Once the total number of votes was identified the analysis pivoted to identifying the vote turnout based on the county. This was completed by assigning a list named county_names to hold the county names and a dictionary named county_votes to count the votes cast in each county. The county names and county votes are collected by utilizing a for loop and an if statement to add the county to the list once a new county name is detected (line ) and by counting the number of votes from each county line 20. This was followed by calculating the percentage of votes for each county (line ). The outcome of this porion of the analyis shows that Denver was the ocunty with the highest number of votes (306,055) which amounted to 82.8% of the votes, while Jefferson and Arapahoe recorded (38,855 votes and 10.5% of the votes) and (24,801 votes and 6.7% of the votes) respectively.

![County_Votes](https://github.com/OmarQasem94/Election_Analysis/blob/main/Resources/County_Votes.PNG)


#### County with the Highest Turnout
The county with the highest turnout was identified using a for loop to go over the data set and count each counties votes. Coupled with an if statement, which is used to identify which county accumulated the most votes (line). The county with the highest turnount was Denver.

![Largest_COunty_Turnover](https://github.com/OmarQasem94/Election_Analysis/blob/main/Resources/Largest_County_Turnover.PNG)


#### Total Number and Percentage of Votes for each Candidate
The next objective of the anlaysis was to identify the number of votes acquired by each candidate. This was completed by creating a list named candidate_options (line 14) and a for loop which goes through the data and adds the candidate's name on the first instance it is detected. A dictionary named candidate_votes was utilized to count the number of votes aquired by the respective candidate. Finally, a calculation was administered using a for loop to identify the percentage of votes acquired by each candidate (line ). The results of this segement of the analysis show that Dianna DeGette accumulated 272,892 votes which was 73.8% of the votes, while Charles Casper Stockham and Raymon Anthony Doane aquired (85,213 votes and 23.0% of the votes), and (11,606 votes and 3.1% of the votes) respectively. 

![Votes_By_Candidate](https://github.com/OmarQasem94/Election_Analysis/blob/main/Resources/Votes_By_Candidate.PNG)


#### Winner of the Election Based on the Popular Vote
The final objective of the analysis was to identify which candidate won the elections based on the popular vote. Within the same loop which identified the number of votes each candidate acquired an if statement was utilized to identify Diana DaGette was the winner of the election based on the popular vote.  

![Winner_Summary](https://github.com/OmarQasem94/Election_Analysis/blob/main/Resources/Winner_Summary.PNG)



## **Summary**
The election audit was completed successfuly and all the desired inferences about the election were derived from the dataset. The utility of this analysis could be enhanced on by modifying the script to incorporate more lists and dictionaries that would account for the votes and candidates of cities and/or states to analyse state and federal elections. By incorporating further loops and conditional satements  that would account for votes and candidates from more cities and/or states inferences can be derived from any other election contingent on the availability of the data. 
 