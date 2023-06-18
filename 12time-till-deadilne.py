from datetime import datetime

today_date = datetime.now()

due_date = input("What is the goal date dd.mm.yyyy?\n")
due_date = datetime.strptime(due_date,"%d.%m.%Y")

print(f"Project due on {due_date} Days Remaining : {(due_date- today_date).days}")