import os
import time



now =time.time()
seconds = now - (1 * 24 * 60 * 60)
path="runCount.txt"
ctime = os.stat(path).st_ctime



opener = open("runTime.txt","r")
time = opener.read()
now = str(now)
print(time)

writer = open("runTime.txt","w")
writer.write(str(now))
writer.close

if(now == time):
    print("hello")
else:
    print("DIED")

'''open1 = open("runCount.txt", "r") #opens file to read it
count = (open1.read())
open1.close()
countAdd = open("runCount.txt", "w")
inc=str(count + "i")
count = inc
lenCount = int(len(count))
countAdd.write(str(count))
countAdd.close()

open1 = open("runCount.txt", "r") #opens file to read it
count = (open1.read())






if(lenCount <= 1):
    print ("welcome")
else:
    print("Welcome back")   ''' 
