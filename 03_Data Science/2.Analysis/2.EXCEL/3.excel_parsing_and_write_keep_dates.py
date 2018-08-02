from datetime import date
from xlrd import open_workbook
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = "input_files/sales_2013.xlsx"
output_file = "output_files/3e.output.xls"

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet("jan_2013_output")

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name("january_2013")
    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, col_index) == 3:
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index,
                                                                 col_index), workbook.datemode)
                # date_cell = date(*date_cell[0:3.Homenetwork]).strftime
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index,col_index,non_date_cell)
output_workbook.save(output_file)