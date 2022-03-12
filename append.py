import csv
import datetime

def apd_ans(name, answere_name, ans):
    time_stamp = str(datetime.datetime.now())
    with open(name, mode='a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([time_stamp, answere_name, ans])
    return None


answere_name = input("What is your name: ")
ans = input("1 ~ 4: ")
apd_ans("hoge.csv", answere_name, ans)
