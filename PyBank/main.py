import os
import csv 
# Path to collect data from the Resources folder
csvpath = os.path.join('/Users/apple/Desktop/bootcamp/python/python_homework/python-challenge/PyBank/budget_data.csv')
# Read in the CSV file
with open(csvpath,newline='') as data:
    bank_data = csv.reader(data)
    print(bank_data)
    bank_header = next(bank_data)
    print(f'csv_header:{bank_header}')
#Create lists to be used to record variable values at each row
    row_list=[]
    revenue_list=[]
    month_list=[]
    for row in bank_data:
        row_list.append(1)
        revenue_list.append(int(row[1]))
        month_list.append(row[0])
    Total_Months = sum(row_list)
    Total = sum(revenue_list)
#Create and update change_list for monthly change of revenue
    change_list = []
    for i in range(1,len(revenue_list)):
        change_list.append(revenue_list[i]-revenue_list[i-1])
#Finding of statistics to be printed in Financial Analysis
    Average_Change = round(sum(change_list)/len(change_list),2)
    Greatest_Increase = max(change_list)
    Greatest_Decrease = min(change_list)
    Increase_index = change_list.index(Greatest_Increase)
    Decrease_index = change_list.index(Greatest_Decrease)
    Increase_Month = month_list[Increase_index+1]
    Decrease_Month = month_list[Decrease_index+1]
#Financial Analysis
    print("Financial Analysis")
    print("-----------------------------------------------")
    print(f'Total Months: {Total_Months}')
    print(f'Total: ${Total}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase in Profits: {Increase_Month} (${Greatest_Increase})')
    print(f'Greatest Decrease in Profits: {Decrease_Month} (${Greatest_Decrease})')
    
    
    
    
    
    