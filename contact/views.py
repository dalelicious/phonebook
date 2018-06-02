# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .viewmodels import ContactViewModel
from .forms import ContactForm

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
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.create_contact(request)
            return redirect('/contact?message=success form')
        else:
            return redirect('/contact?message=invalid form')

def update(request, contactId):
    if request.method == "GET":
        contact = Contact.get_id(contactId)
        form = ContactForm(contact.__dict__)
        return render(request, 'contact/update.html', {'form':form, 'contactId':contact.id})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.update_contact(request, contactId)
            return redirect('/contact?message=success form')
        else:
            return redirect('/contact?message=invalid form')


def delete(request, contactId):

    Contact.delete_contact(contactId)

    return redirect('/contact')
