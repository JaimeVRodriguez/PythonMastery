
#! Strings can be surrounded by single or double quotes
course = "Python Programming"
#! To use quotes inside a quote use escape character "\"
course2 = "Python \"Programming\""

#! Triple quotes are for multi-line strings
message = """
This is a long
message for a user
"""

print(course2)

#! Function is an already established code to produce an output
#! Arguments are "inputs" for a function
# Examples
print(len(course))
#! 0 is the first character
print(course[0])
#! Last index number is not included
print(course[0:3])
print(course[0:])
print(course[:3])