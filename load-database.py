from openpyxl import load_workbook

wb = load_workbook(filename='Dummy Listing.xlsx')
sheet = wb['Sheet1']
for row in range(2, 20):
    vendor_name = sheet['{}{}'.format('A', row)].value
    city = sheet['{}{}'.format('F', row)].value
    venue = sheet['{}{}'.format('G', row)].value

    
    

    
