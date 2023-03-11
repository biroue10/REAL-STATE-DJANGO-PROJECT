from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Listing
from .forms import ListingForm


def listing_list(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings.html', context)


def listing_retrieve(request, pk):
    listings = Listing.objects.get(id=pk)
    context = {'listings': listings}
    return render(request, 'retrieve.html', context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

        return

    context = {'form': form}
    return render(request, 'listing_create.html', context)


def listing_update(request, pk):

    listings = Listing.objects.get(id=pk)
    form = ListingForm(instance=listings)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=listings)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {'form': form}
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listings = Listing.objects.get(id=pk)
    listings.delete()
    return redirect("/")

