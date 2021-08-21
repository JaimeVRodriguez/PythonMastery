
#! Logical operators include
#! and, or, not

high_income = True
good_credit = False
student = False

#! and - Both must be true for true result
#! or - Only one must be true

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

