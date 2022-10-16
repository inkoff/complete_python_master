high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")

if high_income or good_credit or not student:
    print("Eligible")
else:
    print("Not eligible")
