import openpyxl as op

wb = op.load_workbook('test2.xlsx')
ws = wb['a']

rng = ws['A1:C3']

for row_data in rng:
	for data in row_data:
		if data.value % 2 == 0:
			data.value = '' 

wb.save('result2.xlsx')