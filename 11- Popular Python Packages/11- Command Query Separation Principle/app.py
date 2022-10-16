from typing import Literal
import openpyexcel

wb = openpyexcel.load_workbook(
    "11- Popular Python Packages\\11- Command Query Separation Principle\\transactions.xlsx")


sheet = wb["Sheet1"]

for row in range(1, 10):
    cell = sheet.cell(row, 1)
    print(cell.value)

sheet.append([1, 2, 3])
wb.save("11- Popular Python Packages\\11- Command Query Separation Principle\\transactions2.xlsx")

dict = []
dict = {}
dict = ()
dict = ''
dict = ""
dict = 1
dict = "213"
