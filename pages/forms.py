from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="What's your name?")
    email = forms.EmailField(required=True, label="What's your email address?")
    subject = forms.CharField(max_length=250, required=True, label="Subject?")
    message = forms.CharField(widget=forms.Textarea, required=True, label="How can we help you?")

