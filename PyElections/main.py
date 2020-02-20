import os
import csv
import operator

csv_path = os.path.join('LearnPython','Python Homework','PyElections_Data.csv')
total_no_vote = 0

with open(csv_path,encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)

#--Add all candidates into the list    
    all_candidates =[]
    for row in csv_reader:
        name = row[0]
        all_candidates.append(name) 

#--Count number of vote on each candidates and add into the dictionary
    count_vote = {}   
    for k in all_candidates:
        if k in count_vote:
            count_vote[k] +=1
            total_no_vote +=1           
        else:
            count_vote[k] = 1
            total_no_vote += 1

#--Write output into text file
with open('candidates_analysis.txt', 'w') as output_file:

#--Print First Section
    print(f'\nHouston Mayoral Election Results')
    print('------------------------------------------')
    print(f'Total Cast Votes : {total_no_vote}')
    print('------------------------------------------')
    output_file.write(f'\nHouston Mayoral Election Results')
    output_file.write('\n------------------------------------------')
    output_file.write(f'\nTotal Cast Votes : {total_no_vote}')
    output_file.write('\n------------------------------------------')

#--Sorted Candidate List Decending
    for k in sorted(count_vote, key=count_vote.get, reverse=True):
        print(f'{k} {format(count_vote[k]/total_no_vote,".2%")} ({count_vote[k]})')
        output_file.write(f'\n{k} {format(count_vote[k]/total_no_vote,".2%")} ({count_vote[k]})')
    
#--Find 1st Advancing Candidate
    second_can = {}
    for k in count_vote:
        first_can = max(count_vote, key = lambda k: count_vote[k])

#--Pop 1st Advancing Candidate
    count_vote.pop(first_can)
    
#--Find 2nd Advancing Candidate
    for k in count_vote:
        second_can = max(count_vote, key = lambda k: count_vote[k])
    
#--Print last section
    print(f'\n------------------------------------------')
    print(f'\n1st Advancing Candidate: {first_can}')
    print(f'\n2nd Advancing Candidate: {second_can}')
    print(f'\n------------------------------------------')
    output_file.write(f'\n------------------------------------------')
    output_file.write(f'\n1st Advancing Candidate: {first_can}')
    output_file.write(f'\n2nd Advancing Candidate: {second_can}')
    output_file.write(f'\n------------------------------------------')
 