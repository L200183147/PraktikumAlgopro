##Activity 1
a = {'Triangle':'L=0.5*a*t',
     'Square':'L=s**2',
     'Rectangle':'L=p*l',
     'Circle':'L=pi*r**2',
     'Parellelogram':'L=a*t'}
print("""
    No | Name of build      | Broad of formula
    ---|--------------------|--------------
    1  | Triangle           | %s
    2  | Square             | %s
    3  | Rectangle          | %s
    4  | Circle             | %s
    5  | Parellelogram      | %s
    """%(a['Triangle'], a['Square'],
         a['Rectangle'], a['Circle'],
         a['Parellelogram']))


## Activity 2
n = 2
while n<5:
    x = input('Enter password :')
    n = n + 1
    if x!='Annida':
        if n==5:
            print ('Sorry, you have tried 3 times. Your access denied')
        else:
            print ('Sorry, you entered the incorrect password')
    elif x=='Annida':
        n=5
        print ('You logged in')       
       
        
##Activity 3,
a = ("morning", "noon", "afternoon", "evening", "night")
b = input("enter your name, please: ")
c = float(input("What time is it?"))
if c>=1.00 and c<=10.59:
    print ('Good', a[0], b)
elif c>=11.00 and c<=14.59:
    print ('Good' + a[1], b)
elif c>=15.00 and c<=18.00:
    print ('Good', a[2], b)
elif c>=18.01 and c<=20.30:
    print ('Good' + a[3], b)
elif c>=20.31 and c<=24.59:
   print ('Good', a[4], b)


##Activity 4
from datetime import datetime
import time
print ("Program showing computer time")
while int(datetime.now().strftime("%S"))> 0:
    print (datetime.now().strftime("%H:%M:%S"))
    time.sleep(1)
print ("No more practical time. Please go hoome")
