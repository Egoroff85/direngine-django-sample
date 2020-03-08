from django.urls import path, include
from pages.views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('home/search/', HomeSearchView.as_view()),
    path('home/subscribe/', HomeSubscribeView.as_view()),
    path('about/', AboutView.as_view()),
    path('tour/', TourView.as_view()),
    path('tour/search/', TourSearchView.as_view()),
    path('hotel/', HotelView.as_view()),
    path('hotel/search/', HotelSearchView.as_view()),
    path('hotel/single/', SingleHotelView.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/single/', SingleBlogView.as_view()),
    path('contact/', ContactView.as_view()),
]