import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HotelManagement.settings')
django.setup()


from openpyxl import load_workbook
from hotel.models import Vendor


wb = load_workbook(filename='Dummy Listing.xlsx')
sheet = wb['Sheet1']
for row in range(2, 256):
    h = Vendor()
    h.name = sheet['{}{}'.format('A', row)].value
    h.city = sheet['{}{}'.format('F', row)].value
    h.venue_type = sheet['{}{}'.format('G', row)].value
    h.save()
