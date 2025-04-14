#opening the file in read mode
file=open("file.txt","r")
content=file.read()
print(content)

#append mode
file=open("file.txt","a")
file.write("\n a system of words, letters, or signs used to represent \n a message in secret form, or a system of numbers,\n letters, or signals used to represent something in a shorter \n or more convenient form: in code \n The message was written in code")
file.close()

#write mode
file=open("file.txt","w")
file.write("To define something is to give it a meaning.\n We define a variable by assigning it a value.\n a, defined as string. The above defines a as referencing a primitive ")
file.close()

#reading a file using with
with open("file.txt","r") as f:
    print(f.read())

#append mode using with
with open("file.txt","a") as f:
    f.write("\nCoding creates a set of instructions for computers to follow. \nThese instructions determine what actions a computer can and cannot take. \nCoding allows programmers to build programs, such as websites and apps.")

#write mode using with
with open("file.txt","w") as f:
    f.write("In lay terms, coding (or programming) creates instructions a computer can understand and execute. ")