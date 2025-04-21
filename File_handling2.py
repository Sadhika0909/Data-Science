
file=open("file2.txt","r")
content=file.read()
print(content)

with open("file2.txt","a") as f:
    f.write("Easter, also called Pascha  or Resurrection Sunday,\nis a Christian festival and cultural holiday commemorating the resurrection of Jesus from the dead")

with open("file2.txt","w") as f:
    f.write("\nEaster traditions vary across the Christian world, and include sunrise services\nor late night vigils, exclamations and exchanges of Paschal greetings, flowering the cross,\nthe wearing of Easter bonnets by women, clipping the church and the decoration and\nthe communal breaking of Easter eggs ")

with open("file2.txt","r") as f:
    print(f.read())

file=open("file2.txt","w")
file.write("The modern English term Easter, cognate with German Ostern, developed from an Old English word\nthat usually appears in the form Easter.")
file.close()

file=open("file2.txt","a")
file.write("\nIn Latin and Greek, the Christian celebration was, and still is, called Pascha")
file.close()