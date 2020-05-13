from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404
from .models import Vendor

# Create your views here.


def listing(request, page):
    hotels = Vendor.objects.all()
    paginator = Paginator(hotels, 12)
    if page > paginator.num_pages:
        raise Http404("Page not found")
    pageObject = paginator.get_page(page)
    return render(request, 'hotels/listing.html', {"pageObjects": pageObject})
