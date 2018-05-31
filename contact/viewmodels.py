from .models import Contact

class ContactViewModel():

    def get_id(self, contactId):

        getId = Contact.objects.get(id=contactId)
        return getId

    def contact_list(self):

        contactList = Contact.objects.all()
        return contactList

    def create_contact(self, request):

        contact = Contact()
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        self.save_to_db(contact)

    def update_contact(self, request, contactId):

        contact = Contact.objects.get(id=contactId)
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        self.save_to_db(contact)

    def delete_contact(self, contactId):

        contact = Contact.objects.get(id=contactId)
        contact.delete()

    def save_to_db(self, contact):
        
        contact.save()
