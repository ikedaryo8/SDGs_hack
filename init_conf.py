import csv
import os
from datetime import date

def YourName():
    Directory_Names = os.listdir(path=".")
    
    name = input("Enter project name: ") 
    name = name + '.csv'

    if name in Directory_Names:
        while name in Directory_Names:
            name = input("Your name has already used \n please enter other one : ")
            name = name + ".csv"

    return name 

#Initioal config
name = YourName()
time_stamp = str(date.today())

with open(name, mode='w', encoding='utf-8', newline='') as f:
    writer =  csv.writer(f)
    writer.writerow([name, time_stamp])


