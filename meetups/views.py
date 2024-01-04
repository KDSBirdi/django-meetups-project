from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

from .models import Meetup

def index(request):
    meetups = Meetup.objects.all()
    # meetups = [
    #     {'title' : 'A First Meetup', 
    #     'location':'New York',
    #     'slug':'a-first-meetup'},
    #     { 'title' : 'A Second Meetup',
    #     'location':'Paris', 
    #     'slug':'a-second-meetup'}
    # ]
    return render(request, 'meetups/index.html', {
        # 'show_meetups': 1,
        'meetups': meetups 
    })


def meetup_details(request, meetup_slug):
    # print(meetup_slug)
    # selected_meetup = {'title':'A First Meetup',
    #                    'description':'This is the first meetup'}
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
    
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':True,
            'meetup_title':selected_meetup.title,
            'meetup_decription':selected_meetup.description
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found':False,
        })