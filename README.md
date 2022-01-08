# Election_Analysis

## Project Overiew
The Colorado Board of Elections has requested am election audit of teh results of the recent local congressional election.  
The Colorado Board of Elections has sepcifically requested the following infromation:
1. **The total number of votes cast.**
2. **A list of the counties participating in the vote.**
3. **The total votes cast by each county and the percentage each county contributed to the total vote count.**
4. **The county with the largest turnout of voters**
5. **A list of all candidates that recieved votes.**
6. **The total number of votes by candidate and the percentage of total vote each candiate recieved.**
7. **The winner of the election based on popular votes.**

## Resources
- **Data Source** (provided by Colorado Board of Elections)**:** ***election_results.csv***
- **Software:** ***Pyton 3.7.6, Visual Studio Code, 1.63

## Data Output Files
- **Calculation Code:** ***PyPoll_Challenge.py***
- **Result Text File:** ***election_results.txt***

## Election-Audit Method and Results

### Election_Audit Results Summary
All calculations necessary to answer the project objectives stated in the **Project Overview** were completed with ***Python 3.7.6*** with the attached ***PyPoll_Challenge.py*** script.  Results for the analysis can be found by running the ***PyPoll_Challenge.py*** script in the command prompt, terminal, or gitbash with the python.  **The election audit results are:**

1. **The Total number of votes  = 369,711**

2. **County Participation in Vote**: Denver had the largest voter turnout with 82.8% of the total vote.  
   - **Jefferson: 38,855 votes (10.5% of total vote)**
   - **Denver: 306,055 votes (82.8% pf total vote)**
   - **Arapahoe: 24,801 votes (6.7% of total vote)**

3. **Results by Canidate**:  Three candidates recieved votes during the election:
   -**Charles Casper Stockham: 85,213 votes (23.0% of total popular vote) 
   -Diana DeGette: 272,892 votes (73.8% of total popular vote)
   -Raymon Anthony Doane: 11,606 votes (3.1% of total popular vote)
   
4. **Winnier of the Election: *Diana DeGette*
   -Winning Vote Count: 272,892
   -Winning Percentage: 73.8%

The results from the script create a terminal output and the resulting output file (***election_results.txt***) created by the python script.  The results for both can be seen below.

![image](https://user-images.githubusercontent.com/91850824/147888868-8839db4b-17ed-4f3b-8ab6-da4fcb71f434.png)

![image](https://user-images.githubusercontent.com/91850824/147888876-e04e201f-478a-4e48-8a02-cd6ef54a56a5.png)

### Election_Audit Results Code Location and Decription
The ***PyPoll_Challenge.py*** script accesses the ***election_results.csv*** provided by the Colorado Board of Elections and sets the target output file to  ***election_results.txt***.  Variables were set to represent the file loaded (***election_results.csv***) and the target output file (***election_results.txt***) in the rest of the code.

![image](https://user-images.githubusercontent.com/91850824/147888293-0e2f3efe-1d74-4c52-97d5-621887843024.png)

The final results, as well as, their locations in the code are as follows
1. **The Total number of votes  = 369,711**
   - The total vote python calculations
     - Created and set initial variable to 0 to represent and hold Total Votes reultant ) ***total_votes***
     ![image](https://user-images.githubusercontent.com/91850824/147888573-8b2d8d5e-f707-49f1-999a-9ff4ed6f33fd.png)
     - Opened ***election_results.csv*** and read data to ***election_data*** variable
     - Initiated *for* loop (here in after *For Loop*) to run through rows in ***election_results.csv*** and sum the total votes counted and store to ***total_votes*** variable.
      
![image](https://user-images.githubusercontent.com/91850824/147888732-f059bcd8-118d-4ac9-b0df-4dddfc741873.png)

2. **Jefferson, Denver, and Arapahoe counties were included in this audit.**
   - First a python list (**county_list**) was created hold all individual counties found in the ***election_results.csv***.
   - Then a python dictionary (**county_votes**) was created to hold each county's name as key and the total votes for each county as their value:
   ![image](https://user-images.githubusercontent.com/91850824/147889015-40b88d7b-be76-451a-b94d-e7b3e2bc3860.png)
    - In the *For Loop* the county names were extracted from the second column of data and saved to the county_name variable.
   ![image](https://user-images.githubusercontent.com/91850824/147889401-48c914a1-d967-496f-94c1-4f2c2e0274be.png)
    -  A conditional if statement assigns the county name to the **county_list**.  As the data is looped through, the first county name found is appended to the county_list list, and then as a new county name is encountered in the loop, the **not in** function compares **county_list** to the **county_name** and only appends county_list if the county is not alread one of teh values of the list.
    ![image](https://user-images.githubusercontent.com/91850824/147889524-1751135b-d785-4e40-be02-f3b2d021aae6.png)

3. **The total votes cast by each county and the percentage each county contributed to the total vote count: Jefferon 10.5% (38,885 votes); Denver 82.8% (306,055 votes); Arapahoe 6.7% (24,801 votes)**
   - Inside the *For Loop* and inside the If statement to find the county list, the county_votes dictionary is initiated.  The county_name variable is applied as the key to the county_votes dictionary in line 73 and the value to all keys is set to 0.
   - The value for each key is then summed as the data is looped.  One vote is added to each county and saved as the value to the county_votes dictionary.
   ![image](https://user-images.githubusercontent.com/91850824/147889784-955b45ee-a734-48e2-9b89-acaba3b96177.png)
   - A new *for loop* is initiated to loop through the county_votes dictionary and return the total vote count (***votes_by_county*** variable) and calculate the % of total votes by county (saved to ***percent_votes_county*** variable).
   ![image](https://user-images.githubusercontent.com/91850824/147890006-eae4b2ff-66ee-436e-9e29-a197b9795f92.png)
4. **The county with the largest turnout of voters: Denver**
   - Two variables were created to hold the Total County vote ***county_turnout*** and the county with the largest number of citizens who voted ***largest_county***.
   ![image](https://user-images.githubusercontent.com/91850824/147890110-01a0735f-de26-4745-9b21-b8a65eab2006.png)
   - A new if statement is created inside the new *for loop* and it compares ***votes_by_county*** to the ***county_turnout*** variables.  Since we set the ***county_turnout*** variable to 0, the first county will be saved as the ***county_turnout*** and the ***largest_county***.  As the dictionary is looped through, the next county is compared to the saved ***county_turnout*** and the ***largest_county*** and these values are replaced if the county's values meet the condition of the if statement.  
   ![image](https://user-images.githubusercontent.com/91850824/147890200-26e016f8-ec71-4690-a28d-6ac98310872b.png)
5. **A list of all candidates that recieved votes: Charles Casper Stockham,Diana DeGette, and Raymon Anthony Doane**
   - The candidate list was found in the same manner as the county.
   - First a variable and dictionary were created to hold the data from the **election_results.csv***
   ![image](https://user-images.githubusercontent.com/91850824/147890280-a0037861-f7d0-4710-b774-7bb378f82258.png)
   - Next the candidate names were extracted from the third comlumn of the **election_results.csv*** data and saved to a candidate_name variable.
   ![image](https://user-images.githubusercontent.com/91850824/147890299-2f74eff4-334d-4700-8f60-eb08039ae0c9.png)
   - An if statement is initiated to add the candidates name to the **candidates_options** list if not already in the list.
   ![image](https://user-images.githubusercontent.com/91850824/147890352-bb65ae13-0c13-4abb-acf7-a327354ae553.png)
6. **The total number of votes by candidate the percentage of total vote each candiate recieved.**
   - In the same *for loop* and inside the same conditional mentioned in the candidate list, the candidate_votes dictionary's values are first set to 0 and then updated as each row is compared to the candidate_options list.  The candidate_vote variable is increased by 1 every time the data meets the condition (the candiates name variable matches the candidate list).
   ![image](https://user-images.githubusercontent.com/91850824/147890457-ed250610-dbc1-4a78-9cbe-c19c4a0b3761.png)
   - For percentage vote by candidate, a **for loop** was created to loop through the candidates_votes dictionary and return the votes by candidate to a new **votes** variable.  The the percent vote by candidate is then calculated from the **votes** and **total_votes** variables.
    ![image](https://user-images.githubusercontent.com/91850824/147890604-502e1aaf-c89b-4cb0-be27-17dd32d14436.png)
7. **The winner of the election based on popular votes: Diana DeGette with 272,892 votes (73.8% of the popular votes)**
   - Three variables were created to calculate the winning candidate.  One to hold the final winner's name **winning_candidate**; another to compare the winning vote count (**winning_count**), and a thrid to compare % of total vote (**winning_percentage**).
   ![image](https://user-images.githubusercontent.com/91850824/147890688-5dad4329-ddb5-42fc-9464-e45c67daa08b.png)
   - With the exception of the ***and*** statement, an indentical logic was used to find the winning candidate as was used to find teh county with the largest amount of votes. Inside the **vote_percentage** *for loop*, the winning_count variable is set to the votes variable.  As the loop progresses, the next candidate in the loop, if higher than the candidate saved, has his/her name, votes, and percentage of votes are saved.  The winner is the candidate who statisfies all the criteria (most votes, and highest vote percentage).
   ![image](https://user-images.githubusercontent.com/91850824/147890777-5911567a-4195-4183-b7d5-6c0bc5c4baf3.png)
   
## Future Potential for this Analysis
With a few changes, this script could be used for any range of election results.  The script is designed to find and store unique candidate and county values without directly knowing what those values are or having to directly input those values to calculate their totals or percentages.  This script can work with any csv file with the same data column structure (ballot_ID, county, candidate).  Since, the script imports the csv data file as a variable, to use a new data set we just need to change the path for the **file_to_load**.
![image](https://user-images.githubusercontent.com/91850824/147890948-11d83ab1-0b7b-4ba0-a406-f1020907d528.png)

Other data column structures can also be utilized.  If, for example, our csv file had more columns, or those columns were in a different order; we would only need to identify the columns that hold the candidate name and the county name and change the list index to the appropriate comlumn number.  
![image](https://user-images.githubusercontent.com/91850824/147891083-15e69882-0fb9-45cb-92f8-b89a8444f89a.png)

Lastly, since both candidate and county data were retrieved with similar scripts, it would be easy to replicate the process for other information if it exists.  By creating new variable, lists, and dictionaries for the infomation, we can resuse a lot of the existing language.  We could use the county to code to break the data into precincts if the data were available.



