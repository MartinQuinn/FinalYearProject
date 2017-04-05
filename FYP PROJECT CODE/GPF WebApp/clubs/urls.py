from django.conf.urls import url
from . import views

app_name = 'clubs'

urlpatterns = [
    url(r'^create/', views.create, name="create"),
    url(r'^listing/', views.listing, name="listing"),
    url(r'^listingcounties/', views.listingCounties, name="listingcounties")

]
