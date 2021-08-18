
course = " python programming "

#! Strings have their own functions
print(course.upper()) #! Makes everthing upercase
print(course.lower()) #! Makes everthing lowercase
print(course.title()) #! Capitalizes first letters
print(course.strip()) #! Removes space from front and rear

print(course.find("pro")) #! Index of where the word or character begins

print(course.replace("p", "j"))

print("pro" in course) #! Returns a boolean instead of index

