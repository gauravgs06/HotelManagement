from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from .models import Vendor

# Create your views here.


def listing(request):
    page = request.GET.get('page')
    if page == None:
        page = 1
    else:
        page = int(page)    
    gt = request.GET.copy()
    city = gt.get('city')
    veg_price = gt.get('veg_price')
    max_cap = gt.get('max_cap')
    if 'page' in gt:
        del gt['page']
    hotels = Vendor.objects.all().order_by('name')
    if city is not None:
        hotels = hotels.filter(city=city).order_by('name')
    if veg_price is not None:
        hotels = hotels.filter(veg_price=veg_price)
    # except:
    paginator = Paginator(hotels, 12)
    if page > paginator.num_pages:
        raise Http404("Page not found")
    pageObject = paginator.get_page(page)
    params = gt.urlencode()
    city_list = Vendor.objects.values_list('city',flat=True).order_by('city').distinct() 
    return render(request, 'hotels/listing.html', {"pageObjects": pageObject, 'params': params, 'city_list': city_list})

def get_city_list():
    return Vendor.objects.distinct('city')