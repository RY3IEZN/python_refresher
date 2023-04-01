import openpyxl

# load the worksheet
inventory_file = openpyxl.load_workbook(filename="inventory.xlsx")

#point to the specific worksheet
worksheet_name = inventory_file["Sheet1"]
