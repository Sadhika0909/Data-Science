from datetime import datetime

def add_entry():
    input("Write your diary entry: ")
    file=open("journal.txt","a")
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    print("My Journal")
    print("1.Add new entry\n2.View entry\n3.Exit")
    a=int(input("Choose an option: "))

