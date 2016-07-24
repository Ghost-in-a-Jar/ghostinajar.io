from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput)
    contact_email = forms.EmailField(required=True, widget=forms.EmailInput)
    content = forms.CharField(
        required=True,
        widget=forms.TextInput
    )