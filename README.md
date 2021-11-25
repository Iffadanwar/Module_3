# Election_Analysis

## Project overview
An employee of a colorado commission has given me these tasks to audit a local congressional election.
The colorado commission also requests information about the different counties and their turnover in the election. They further ask if the scrip can be upscaled to incorporate larger voting districts and give them examples. 

1. calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner based on the popular votes.
6. list the different counties
7. list their turnout and total votes from each county
8. lastly list the largest county turnover
9. list each county by per cent turnover

## Resources
 - Data Source: election_results.csv
 - Software: Python 3.9.0, Spyder 5.1.5

## Summary
The election analysis shows:
- There were "369,711" votes cast in the election.
  - the code uses a for loop to count all the votes cast by adding to total_votes
     23. for row in file_reader:
     25. total_votes += 1
     
- The Candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
      - The code uses a for loop to shift through all the data and if loop to only count unique terms in the list. giving us the names of the candidates.
        23. for row in file_reader:
        30.   if candidate_name not in candidate_options:
        32.   candidate_options.append(candidate_name)
       
- The Candidate results were:
    - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane received "3.1%" of the vote and "11,606" votes.
      - the code calculates per cent votes and tallies up the code within the for a loop.
        49. for candidate_name in candidate_votes:
        51.   votes = candidate_votes[candidate_name]
        52.   vote_percentage = float(votes) / float(total_votes) * 100
       
- The winner of the election was:
    - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
      - The code was a collection of the different already available. The if statement keys throughout the           candidate_votes dictionary and takes the heist vote percentage and votes to declare a winner.
      60. if (votes > winning_count) and (vote_percentage > winning_percentage):
      61.      winning_count = votes
      62.      winning_candidate = candidate_name
      63.      winning_percentage = vote_percentage
- County results were:
    - Jefferson County had 10.5% of the votes with 38,855 votes.
    - Denver county had 82.8% of the votes with 306,055 votes.
    - Arapahoe county had 6.7% of the votes with 24,801 votes.
      - the code used is similar to calculating candidate results. it uses a for loop to shift through            all the data and a formula to collect total county_percentage and county_turnout 
          97.  for county_name in county_dictionary:
          99.        county_vote = county_dictionary.get(county_name)
          101.       county_rate = (float(county_vote) / float(total_votes)) * 100

- County with the largest number of votes?
    - Denver county had 82.8% turnover with 306,055 votes.
    
## Challenge Summary
the script used today was able to accurately extract vital information from the raw data and give us a clearer picture of who won the election and by what margins. This script can be used to evaluate any election with a few modifications to the code. 
If for example this script was used to count federal elections, vital data such as state, county, ZIP code, and city district would be required. However, if only state and county were to be considered the following changes would allow states to be an additional conditional factor to further help the commission break down results. assuming a new data set has state name listed on row "D".
-  state_list = [] 
-  state_dictionary = {}
     - with open(file_to_load) as election_data:
     - reader = csv.reader(election_data)
     - for row in reader:
      -  state_list = row[3]
      ---this will allow us the have the list of state names into the state_list list.
      - if state_list not in state_name:
          -  state_list.append(state_name)
          - state_dictionary[state_name] = 0
          - state_dictionary[state_name] += 1
     --- this code will allow me to track votes of states and place them inot a dictionary for each   `            state.
       - for state_name in state_dictionary:
        -  state_vote = state_dictionary.get(state_name)
        -  state_rate = (float(state_vote) / float(state_votes)) * 100
       --- finally this last set of code will give us a state vote turnout and vote percentage.
Another change that would make this script more universal is adding voting districts to the dataset giving the commission electoral college a capable voting calculating system. 
 - the code for calculating voting districts are similar to implementing state results but adding the different districts up for a candidate will require additional work.
  - winning_counter = 0
       - candidiate_district_win_count = {}
       - for winning_candidiate in candiaite_options
       - winning_counter += 1
       - candidate_results = (f"{candidate_name}: {winning_counter})\n")
---the winning_counter will hold the number of districts a candidiate won.
---this can be used to see who won a presidential race.
