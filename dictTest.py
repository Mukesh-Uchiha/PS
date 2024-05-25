import  os
import ast

contact={}



f = open("dictTest.txt","a")
name = input("Enter a name")
number = input("number")
number = "+91" + number
contact[name] = number

for name, number in contact.items():
 
 f.write('%s:%s\n' % (name, number))



file = open("dictTest.txt", "r")

contents = file.read()
for line in file:
    x=line.split(":").strip(":")
    name = x[0]
    number = x[1]
    last = len(number)-1
    number = number[0:last]

contact[name] = number
print(contact)
file.close()
f.close()

f2 = open("dictTest.txt","r")
try:
    name1= input("enter a name")
    flag = 0
    index = 0
    for line in f2:  
        index += 1 
        
        # checking string is present in line or not
        if name1 in line:
            
            flag = 1
            
            if ":" in line:
                x=line.split(":")
                name = x[0]
                number = x[1]
                last = len(number)-1
                number = number[0:last]
            break     

    # checking condition for string found or not
    if flag == 0: 
        print('String', name1 , 'Not Found') 
    else: 
        print('String', name1, "\nNumber: "+number)

except:
    pass    


print("Name: " +name+ "\nNumber: "+number)

f2.close()
f3 = open("dictTest.txt","r")
try:
    delete = input("enter a name")
    del contact[delete]
except:
    pass    

f3.close()