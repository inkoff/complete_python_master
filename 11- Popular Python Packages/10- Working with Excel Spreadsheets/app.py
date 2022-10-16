import openpyexcel

# wb = openpyexcel.Workbook()
wb = openpyexcel.load_workbook(
    "11- Popular Python Packages\\10- Working with Excel Spreadsheets\\transactions.xlsx")
print(wb.sheetnames)
sh = wb["Sheet1"]
# wb.create_sheet("Sheet2", 1)
cell = sh["a1"]
print(cell.value)
print(cell.row)
print(cell.column)
print(cell.coordinate)
cell = sh.cell(row=1, column=1)

print(sh.max_row)
print(sh.max_column)

for row in range(1, sh.max_row+1):
    for column in range(1, sh.max_column+1):
        cell = sh.cell(row, column)
        print(cell.value)

column = sh["a"]
print(column)

range = sh["a:c"]
print(range)

print(sh["a1:c3"])
print(sh[1:3])

wb.save("transaction.xlsx")
