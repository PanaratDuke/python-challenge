import os
import csv

csv_path = os.path.join('LearnPython','Python Homework','PyElections_Data.csv')
total_no_vote = 0

with open(csv_path,encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    header = next(csv_reader)
    all_candidates =[]
    unique_candidates = []
    for row in csv_reader:
        name = row[0]
        all_candidates.append(name)
    #print (f'Name : {name}') 
    unique_candidates= {}
    count = 0
   

    count_vote = {}

    for k in all_candidates:
        if k in count_vote:
            count_vote[k] +=1
            
        else:
            count_vote[k] = 1
    #print (count_vote)
    
    for s in count_vote:
        total_no_vote += count_vote[s]
    
    #--Print First Section
    print(f'\nHouston Mayoral Election Results')
    print('------------------------------------------')
    print(f'Total Cast Votes : {total_no_vote}')
    print('------------------------------------------')
    
    result_vote = {}
    
    for k in count_vote:
        if k not in result_vote:
            result_vote['candidate'] = k
            result_vote['vote'] = count_vote[k]
            result_vote['percen resulttage_won'] = format(count_vote[k]/total_no_vote,".2%")
            
            #print (f'{result_vote['candidate']},{result_vote['percentage_won']},({result_vote['vote']})')
            print_candidate = result_vote['candidate']
            print_percentage_won = result_vote['percen resulttage_won']
            print_vote = result_vote['vote']
            print(f'{print_candidate}: {print_percentage_won} ({print_vote})')
            
    #--Sort Data from the highest vote
    # for k,v in result_vote:
    #     sorted_can = sorted(result_vote.items(), key=lambda kv: result_vote[k], reverse=True)
    #     print (k,v)
            
    #--Find 1st Advancing Candidate
    second_can = {}
    for k in count_vote:
        first_can = max(count_vote, key = lambda k: count_vote[k])

    #--Pop 1st Advancing Candidate
    count_vote.pop(first_can)
    
    #--Find 2nd Advancing Candidate
    for k in count_vote:
        second_can = max(count_vote, key = lambda k: count_vote[k])

        #print("2st can", first_can)
    
    #--Print last section

    print(f'\n--------------------------------')
    print(f'\n1st Advancing Candidate: {first_can}')
    print(f'\n2nd Advancing Candidate: {second_can}')
    print(f'\n--------------------------------')

            

        
