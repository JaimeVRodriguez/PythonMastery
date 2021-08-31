
#! Python has built in functions
# print(), round(), etc
#! Functions Peform a task or Return a value

#! Perform a task
# Parameters are things the function can take
def greet(firstName, lastName):
    print(f"Hi {firstName} {lastName}")
    print("Welcome")

#! Calling a function - using it
# Argument is the value for a parameter
greet("Jaime", "Rodriguez")


# Will not "print" anything
def getGreeting(name):
    return f"Hi {name}"

message = getGreeting("Jaime")
print(message)