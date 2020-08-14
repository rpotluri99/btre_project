from django.shortcuts import render
from .models import Listing
# Create your views here.
def search(request):
    return render(request, 'listings/search.html')


def listing(request,listing_id):
    return render(request, 'listings/listing.html')


def index(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request, 'listings/listings.html',context)
