
#Display the even numbers between one and ten
#Message with the number of even numbers

count = 0
for x in range(1,10):
    if x % 2 == 0:
        count += 1
        print(x)

print(f"There are {count} even numbers")