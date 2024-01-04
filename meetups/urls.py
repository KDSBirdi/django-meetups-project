from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #our-domain.com/meetups this will be active
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details'), #our-domain.com/meetups/<dynamic-path-segment>
]