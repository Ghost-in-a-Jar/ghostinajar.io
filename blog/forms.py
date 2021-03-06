from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'Name'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control input-md', 'placeholder':'Email'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':'form-control input-md', 'placeholder':'Message'})
    )