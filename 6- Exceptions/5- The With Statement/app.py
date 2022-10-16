try:
    with open("app.py") as file:
        print(file)
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError) as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print("Procces.")
print("Done.")
