import xlrd

workbook = xlrd.open_workbook('translate.xlsx')

sheet = workbook.sheet_by_index(0)

print (sheet.cell_value(0,0))
