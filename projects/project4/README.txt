Names: Albert Le, Charles Jenkins, Colin Bradford
Emails: leal@onid.oregonstate.edu, jenkinch@onid.oregonstate.edu, bradfoco@onid.oregonstate.edu
Class: CS325 Analysis of Algorithms
Project #: 4
Description: Program finds
possible solutions to the Traveling
Salesman Problem (TSP) for a given input
file.

How to Execute:
---------------
- This program is written in Python.

- How to output to [input filename].tour:
    - While in the project directory, run the following statement in your terminal:
      python project4.py [input filename] [optional: time limit in seconds]
    
    - To use the default time limit of 270 seconds, omit the optional argument
        - For example, for some input file "test.txt" you would type: python project4.py test.txt
    
    - To specify some other time limit (e.g. 500 seconds) you would type: python project4.py test.txt 500
        - NOTE: The time limit applies through the algorithms' calculation phases. It will likely take a few
                more seconds for output to be written to the file and the program to terminate. Also, setting
                a time limit too low for the greedy algorithm to finish will not enforce the time limit, but rather
                the program will run the greedy algorithm until it is complete and then output and terminate.

- [input filename].tour should now be created in the project directory containing a distance and route.

Testing Machine:
----------------
SSH'ing into Oregon State flip server: access.engr.oregonstate.edu