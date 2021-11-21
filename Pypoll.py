# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:27:25 2021

@author: Sued Iffad Anwar
"""

# The data we need to retrieve.
import os
import csv
#print(dir(csv))
#election_data = "resources\election_results.csv"
#election_data = open(resources\election_results.csv, "r")       ###same as the one below it
#with open(file_to_load) as election_data:
    
#print(dir(os.path))
    
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
            # Print the header row.
    headers = next(file_reader)
    print(headers)





# 1. the total number of voters.
# 2. A complete list of candidates who received voters.
# 3. The percentage of votes each candidate won.
# 4. the total number of votes each candidate won.
# 5. the winner of the election based on popular votes.



