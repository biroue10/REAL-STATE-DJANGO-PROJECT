from django.contrib import admin
from django.urls import path
from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',listing_list),
    path('listings/<pk>/',listing_retrieve),
    path('add-listing/',listing_create),
    path('listings/<pk>/edit/',listing_update),
    path('listings/<pk>/delete/',listing_delete),
]
