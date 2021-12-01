from django.forms import ModelForm
from web.models import Contact
from django.forms.widgets import EmailInput,TextInput,Textarea


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "email" : EmailInput(attrs={"placeholder":"Enter your Email id"}),
            "name" : TextInput(attrs={"placeholder":"Name","class":"name"}),
            "subject" : TextInput(attrs={"placeholder":"Subject","class":"subject"}),
            "message" : Textarea(attrs={"placeholder":"Message","rows":10,"cols":30}),
            # "company_size" : Select(attrs={"class:hello"}),
        }