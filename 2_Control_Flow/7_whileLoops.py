
number = 100

while number > 0:
    print(number)
    number //= 2

command = ""

while command != "quit":
   command = input("> ")
   # edits
   # while quit no matter how "quit" is used
   command= command.lower() 
   print("ECHO", command)
