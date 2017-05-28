from django.shortcuts import render
from .models import user_details,user_contact
import os,re,io,csv
from datetime import date
from django.http import HttpResponse
from xlsxwriter import Workbook
# Create your views here.
def first_About_ME(request):

    return render(request,"first.html")

def contact_Details(request):
    if request.POST:
        myDict = dict(request.POST)
        print(myDict)
        firstname = myDict['firstName'][0]
        lastname = myDict['lastName'][0]
        streetaddress = myDict['streetaddress'][0] +myDict['streetaddress2'][0]
        city = myDict['city'][0]
        state = myDict['state'][0]
        zipcode= myDict['zip'][0]
        phone = myDict['phone'][0]
        email = myDict['contactEmail'][0]
        user= user_details(first_name= firstname,last_name=lastname,stree_address=streetaddress,city=city,state=state,post_code=zipcode)
        user.save()
        userContact = user_contact(first_name=firstname,last_name=lastname,phone_number=phone,email=email)
        userContact.save()

        return render(request,"first.html")
    else:
        return render(request,"contact.html")

def download_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'stree_address', "City",'State', 'Post_Code',"Email","Phone_Number"])

    users = user_details.objects.all().values_list("first_name","last_name","stree_address","city","state","post_code")
    for user in users:
        user_co = user_contact.objects.filter(first_name=user[0]).values_list("email","phone_number")
        writer.writerow(user+user_co[0])

    return response