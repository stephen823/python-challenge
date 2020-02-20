import os
import csv 
# Path to collect data from the Resources folder
csvpath = os.path.join('/Users/apple/Desktop/bootcamp/python/python_homework/python-challenge/PyPoll/election_data.csv')
# Read in the CSV file
with open(csvpath,newline='') as data:
    poll_data = csv.reader(data)
    print(poll_data)
    poll_header = next(poll_data)
    print(f'csv_header:{poll_header}')
#Create lists to be used to record imformation about voting results
    vote_list1 =[]
    vote_list2 =[]
    candidate_list=[]
    for row in poll_data:
        vote_list1.append(1)
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            I=candidate_list.index(row[2])
            vote_list2.append(0)
            vote_list2[I]=vote_list2[I]+1
        else:
            I=candidate_list.index(row[2])
            vote_list2[I]=vote_list2[I]+1
    total_vote = sum(vote_list1)
#This code shows that there are 4 candidates
    print(len(candidate_list))
#Finding statistics to be printed in Election Result
    winner_place = vote_list2.index(max(vote_list2))
    winner = candidate_list[winner_place]
    vote_share0 = round(vote_list2[0]/total_vote*100,4)
    vote_share1 = round(vote_list2[1]/total_vote*100,4)
    vote_share2 = round(vote_list2[2]/total_vote*100,4)
    vote_share3 = round(vote_list2[3]/total_vote*100,4)
#Election Result
    print("Election Results")
    print("---------------------------------------")
    print(f'{candidate_list[0]}: {vote_share0}00%  ({vote_list2[0]})')
    print(f'{candidate_list[1]}: {vote_share1}00%  ({vote_list2[1]})')
    print(f'{candidate_list[2]}: {vote_share2}00%  ({vote_list2[2]})')
    print(f'{candidate_list[3]}: {vote_share3}00%  ({vote_list2[3]})')
    print("----------------------------------------")
    print(f'Winner:  {winner}')
        