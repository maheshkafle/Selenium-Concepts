import xlrd

workbook = xlrd.open_workbook("DataFile.xlsx")
sheet = workbook.sheet_by_name("Credential")

# get total no. of rows
row_count = sheet.nrows
column_count = sheet.ncols
print(row_count)
print(column_count)

for row in range(1, row_count):
    user_name = sheet.cell_value(row, 0) # '0' means it reads value from 1 column
    password = sheet.cell_value(row, 1) # '1' means it reads value from 1 column

    print(user_name + " " + str(password))




