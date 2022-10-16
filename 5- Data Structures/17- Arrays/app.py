from array import array

# tycode это определение типа переменных внутри массива
a = array("i", [1, 2, 3])
a.append(4)
a.insert(4, 6)
a.pop()
print(a[1])

# только тип определенный "i"
# a.append("v") # -> error
