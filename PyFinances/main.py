import os
import csv

csv_path = os.path.join('LearnPython','Python Homework','PyFinances','budget_data.csv')
csv_out = os.path.join('LearnPython','Python Homework','PyFinances','budget_analysit.csv')



#--Variable for storing data in dictionary 
total_month = 0
net_total = 0
cal_change = []
cal_percent_change = []
last_row = 0
count = 0
acc_bd = 0
budget_diff = 0    
great_inc = 0
great_dec = 0

#--Reading data to store in budget{}
with open (csv_path, encoding='utf-8') as f:
    csv_reader = csv.reader(f,delimiter=',')
    header = next(csv_reader)  
    for row in csv_reader:

        #--Count number of month
        total_month += 1

        #--Sum profit/loss
        net_total  += int(row[0])

        cal_percent_change.append(int(row[0]))

        #--Calculate Greates Increase/Decrease
        month_change = int(row[0]) - last_row
        last_row = int(row[0])
        # print (month_change)

        cal_change.append(month_change)
        if (month_change > great_inc):
            great_inc_month = row[1]
            great_inc = month_change
        elif (month_change) < great_dec:
            great_dec_month = row[1]
            great_dec = month_change
        #--End Calculate loop------------------

    #--Calculate Average Change   
    for i in range(len(cal_percent_change)):
        if i != 0:
            count += 1
            budget_diff = (cal_percent_change[i]-cal_percent_change[i-1]) 
            acc_bd += budget_diff

    avg_of_change = acc_bd/count
with open(csv_out,'w') as output_file: 
    #--Print
    print('Financial Analysis')
    print('---------------------------------')
    print(f'Total Months: {total_month}')
    print(f'Total : ${net_total}')
    print(f'Average Change : ${avg_of_change:.2f}')
    print(f'Greatest Increase in Profits : {great_inc_month} (${great_inc})')
    print(f'Greatest Decrease in Profits: {great_dec_month} (${great_dec})')
    output_file.write(f'Financial Analysis')
    output_file.write('\n---------------------------------')
    output_file.write(f'\nTotal Months: {total_month}')
    output_file.write(f'\nTotal : ${net_total}')
    output_file.write(f'\nAverage Change : ${avg_of_change:.2f}')
    output_file.write(f'\nGreatest Increase in Profits : {great_inc_month} (${great_inc})')
    output_file.write(f'\nGreatest Decrease in Profits: {great_dec_month} (${great_dec})')
