try:
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError) as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print("Procces.")
print("Done.")
