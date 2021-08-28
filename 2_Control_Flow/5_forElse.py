
#! Can "break out" of the loop befor it goes through the whole range
successful = False
for number in range(1, 4):
    print(f"Attempt: {number}")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times. Fail")
