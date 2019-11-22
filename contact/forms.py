from django import forms
from .models import Contact

##Put your forms here
"""
class ContactForm(forms.Form):
	name = forms.CharField(label="Name", max_length=40, initial="Your name")
	firstname = forms.CharField(label="Firstname",max_length=40, initial="You firstname")
	email = forms.EmailField(label="Email")
	gender = forms.ChoiceField(label="Gender",widget=forms.RadioSelect,choices=choice_gender) 
	message = forms.CharField(label="Message",initial="Type your message ...",widget=forms.Textarea)
"""
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'gender': forms.RadioSelect,
		}
