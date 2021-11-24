# Election_Analysis

## Project overview
An employee of a colorado commision has given me these tasks to audit a local congressonal election.
The colorado commision also requests information about the different countys and their turnover in the election. They further ask if the scrip can be up scaled to incorporate larger voting districts and giving them examples. 

1. calculate the total number of votes casted.
2. Get a complete list of candidates who recived votes.
3. Calculate the total number of votes each candidate received.
4. Calcualte the percentage of votes each candidate won.
5. Determine the winner based on the popular votes.
6. list the different counties
7. list their turnout and total votes from each county
8. lastly list the largest county turnover
9. list each county by percent turnover

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.9.0, Spyder 5.1.5

## Summary
The election analysis shows:
- There were "369,711" votes casted in the election.
- The Candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The Candidiate results were:
    - Charles Casper Stockham recived "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette recived "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane recived "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
    -Diana DeGette recived "73.8%" of the vote and "272,892" number of votes.
- County results were:
    - Jefferson county had 10.5% of the votes with 38,855 votes.
    - Denver county had 82.8% of the votes with 306,055 votes.
    - Arapahoe county had 6.7% of the votes with 24,801 votes.
- County with the largest number of votes?
    - Denver county had 82.8% turnover with 306,055 votes.
 
## Challenge Summary
the script used today was able to accuratly extract vital information from the raw data and give us a clearer picture of who won the election and by what margins. This script can be used to eveluate any election with a few modifications to the code. 
If for example this script was used to count federal elections, vital data such as state, county, ZIP code, and city districting would be required. However if only state and county were to be considered the following changes would allow states to be an additional conditional factor to further help the commition break down results.
    
    
Another change that would make this script more universal is adding voting districts to the dataset giving the commission electoral college capatable voting calculating system. 
