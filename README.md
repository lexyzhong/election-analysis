# Election-Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has requested the following to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of counties from which the votes were cast.
3. Calculate the total number of votes cast from each county.
4. Calculate the percentage of votes cast from each county.
5. Determine the county that cast the highest number of votes.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular votes.


## Resources
- Data Source: election_results.csv
- Software: Pthon 3.6.1, Visual Studio Code, 1.62.3

## Election-Audit Results
The analysis of the election show that:

![election-results_command-line.png](https://github.com/lexyzhong/election-analysis/blob/main/Resources/election-results_command-line.png)

![election_analysis.txt](https://github.com/lexyzhong/election-analysis/blob/main/analysis/election_analysis.txt)

- There were 369,711 votes cast in the election.
- The counties were:
    - Jefferson
    - Denver
    - Arapahoe
- The county results were:
    - Jefferson county cast 10.5% of the votes with 38,855 votes.
    - Denver county cast 82.8% of the votes with 306,055 votes.
    - Arapahoe count cast 6.7% of the votes with 24,801 votes.
- The county with the largest number of votes was:
    - Denver
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the votes and 85,213 votes.
    - Diana DeGette received 73.8% of the votes and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the votes and 11,606 votes.
- The winner of the election was:
    - Diana DeGette received 73.8% of the vote and 272,892 votes.

## Election-Audit Summary
With minor modifications, this script can be used for any election. For federal elections, the "county"/"counties" in the script should be changed to "state"/"states". For public opinion or initiative polls, instead of a list of candidates, the polling options can be changed to, for example, "in favor of" or "against". For determinations of voter turnout in areas where the total number of eligible voters are available, an additional line to calculate the percentage of votes cast over the total number of eligible voters can be added.
