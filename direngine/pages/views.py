from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class HomeSearchView(View):
    def post(self, request):
        html = '<html><body>'
        html += f"You was searching for: {request.POST['type']}<br>"
        html += f"At: {request.POST['location']}<br>"
        html += "We will let you know if there is something you are looking for.<br>"
        html += '</body></html>'
        return HttpResponse(html)


class HomeSubscribeView(View):
    def post(self, request):
        html = '<html><body>'
        html += f"Congratulations!<br>"
        html += f"Your e-mail address: {request.POST['email']} is now subscribed to our newsletter<br>"
        html += '</body></html>'
        return HttpResponse(html)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class TourView(View):
    def get(self, request):
        return render(request, 'tour.html')


class TourSearchView(View):
    def post(self, request):
        html = '<html><body>'
        html += 'Your are looking for the following tour:<br>'
        html += f"Destination: {request.POST['destination']}<br>"
        html += f"Location: {request.POST['location']}<br>"
        html += f"Date From: {request.POST['date-from']}<br>"
        html += f"Date To: {request.POST['date-to']}<br>"
        html += 'We will let you know if we will find anything suitable for you!'
        html += '</body></html>'
        return HttpResponse(html)


class HotelView(View):
    def get(self, request):
        return render(request, 'hotel.html')


class HotelSearchView(View):
    def post(self, request):
        html = '<html><body>'
        html += 'Your are looking for the following hotel:<br>'
        html += f"Destination: {request.POST['destination']}<br>"
        html += f"Location: {request.POST['location']}<br>"
        html += f"Date From: {request.POST['date-from']}<br>"
        html += f"Date To: {request.POST['date-to']}<br>"
        html += 'We will let you know if we will find anything suitable for you!'
        html += '</body></html>'
        return HttpResponse(html)


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
        html = '<html><body>'
        html += 'Thank you for contacting us! We received the following information from you:<br>'
        html += f"Your name: {request.POST['name']}<br>"
        html += f"Your e-mail: {request.POST['email']}<br>"
        html += f"Message subject: {request.POST['subject']}<br>"
        html += f"Your Message: {request.POST['message']}<br>"
        html += 'We will answer your message as soon as possible!'
        html += '</body></html>'
        return HttpResponse(html)
