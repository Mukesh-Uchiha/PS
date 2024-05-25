import pywhatkit
import datetime
import time
import math

contact={
    "sri ram" : "+919790692626",
    "amma"  : "+919788179740",    
}



start = time.time()
name=str(input("Enter a name"))
number= (contact[name])

msg=(input("Enter a Msg "))
end = time.time()
time_taken = end-start
if(time_taken <= 60):
    sec = 1
elif(time_taken >=60):
    sec=2   
elif(time_taken >= 180):
    sec = 3   

h = int(time.strftime("%H"))
m = int(time.strftime("%M"))
m = m + sec
pywhatkit.sendwhatmsg(number,msg,h,m,10,True,3)

