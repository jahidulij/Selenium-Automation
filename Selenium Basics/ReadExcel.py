import xlrd

workbook = xlrd.open_workbook("TestData.xls")
sheet = workbook.sheet_by_name("Login")

# Row count
rowCount = sheet.nrows
columnCount = sheet.ncols
print(rowCount)
print(columnCount)

for row in range(1, rowCount):
    username = sheet.cell_value(row, 0)
    password = sheet.cell_value(row, 1)
    print(username + " " + password)
