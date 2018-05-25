f=open("file.txt")
print(f.read())#-1 is implicitly put between the braces and it reads all files
print(f.read())#cursor is at the end of file so it prints blank

f.seek(20)#goes to the 20th charachter
print(f.read())
f.seek(0)#go to the beginning

print(f.readline())
f.seek(0)
print(f.readlines())#copies all lines as list
print(f.closed) #check if file is closed
f.close() #close a file
print(f.closed,"\n\n")

#OR

with open("file.txt") as file:#opens a file and automatically closes it when its done
  print(file.read())
  file.seek(0)
  for x in file.readlines():
    if x == "I am -- years old\n":#\n has to be put at the end of  ur sentence if u went to a new line
      print ("found it")


print(file.closed)

with open("new.txt","w") as file:#add a w to write from file

  file.write("Now this is how i write a file")#this overwrites


