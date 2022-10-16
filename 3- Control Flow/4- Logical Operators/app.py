high_income = True
good_credit = False
student = True
# print("and")
# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")
# print("or")
# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")
# print("not")
# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
