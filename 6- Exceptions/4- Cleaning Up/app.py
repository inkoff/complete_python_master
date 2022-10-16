try:
    file = open("app.py")
    age = int(input("Age: "))
    x = 10/age
except (ValueError, ZeroDivisionError) as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
else:
    print("Procces.")
finally:
    file.close()
print("Done.")
