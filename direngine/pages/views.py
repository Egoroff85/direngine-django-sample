from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class HomeSearchView(View):
    def post(self, request):
        return render(request, 'index-search.html')


class HomeSubscribeView(View):
    def post(self, request):
        return render(request, 'index-subscribe.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class TourView(View):
    def get(self, request):
        return render(request, 'tour.html')


class TourSearchView(View):
    def post(self, request):
        return render(request, 'tour-search.html')


class HotelView(View):
    def get(self, request):
        return render(request, 'hotel.html')


class HotelSearchView(View):
    def post(self, request):
        return render(request, 'hotel-search.html')


class SingleHotelView(View):
    def get(self, request):
        return render(request, 'hotel-single.html')


class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')


class SingleBlogView(View):
    def get(self, request):
        return render(request, 'blog-single.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        return render(request, 'contact-message.html')
