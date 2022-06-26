from django.http import HttpResponse
import requests


def index(request):
    if request.method == 'POST':
        username= requests.get('https://www.youtube.com/shorts/E6F6LeO0nYc')
        print(username)
        return HttpResponse(username)
    else :
        return HttpResponse("Hello, world")
