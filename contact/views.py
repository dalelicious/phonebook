# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .viewmodels import ContactViewModel

Contact = ContactViewModel()

# Create your views here.
def view(request):

    contact_list = Contact.contact_list()

    return render(request, 'contact/index.html',
                    {'contact_list' : contact_list})


def create(request):
    if request.method == "GET":

        return render(request, 'contact/create.html')
    else:
        Contact.create_contact(request)

        return redirect('/contact')

def update(request, contactId):
    if request.method == "GET":
        contact = Contact.get_id(contactId)

        return render(request, 'contact/update.html', {'contact':contact})
    else:
        Contact.update_contact(request, contactId)

        return redirect('/contact')


def delete(request, contactId):

    Contact.delete_contact(contactId)

    return redirect('/contact')
