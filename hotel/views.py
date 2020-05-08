from django.shortcuts import render
from .models import Hotel

# Create your views here.
def listing(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/listing.html', { "hotels": hotels})