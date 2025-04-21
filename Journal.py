from datetime import datetime

def add_entry():
    entry=input("Write your diary entry: ")
    file=open("journal.txt","a")
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write("[{}]: {}\n".format(date,entry))
    print("Your entry is saved")

def view_entry():
    file=open("journal.txt","r")
    print("Your journal entries:")
    count=0
    for i in file:
        print("{}. {}\n".format(count,i.strip()))
        count+=1

while True:
    print("My Journal")
    print("1.Add new entry\n2.View entry\n3.Exit")
    a=int(input("Choose an option: "))
    if a==1:
        add_entry()
    elif a==2:
        view_entry()
    elif a==3:
        print("Exiting journal")
        break



