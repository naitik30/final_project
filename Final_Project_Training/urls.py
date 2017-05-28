from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.first_About_ME,name="About Me"),
    url(r'contact/$', views.contact_Details, name="Details"),
    url(r'download/$', views.download_data, name="download"),
]