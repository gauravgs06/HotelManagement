import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HotelManagement.settings')
django.setup()

from hotel.models import Vendor
from openpyxl import load_workbook


wb = load_workbook(filename='Dummy Listing.xlsx')
sheet = wb['Sheet1']
for row in range(2, 200):
    h = Vendor()
    h.name = sheet['{}{}'.format('A', row)].value
    h.city = sheet['{}{}'.format('F', row)].value
    h.venue_type = sheet['{}{}'.format('G', row)].value
    try:
        h.max_capacity = int(
            sheet['{}{}'.format('D', row)].value.split('-')[1])
    except IndexError:
        try:
            h.max_capacity = int(
                sheet['{}{}'.format('D', row)].value.split('-')[0])
        except ValueError:
            h.max_capacity = None
    except AttributeError:
        h.max_capacity = sheet['{}{}'.format('D', row)].value
    h.save()
