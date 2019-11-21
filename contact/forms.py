from django import forms


##variables : list of tuples 
choice_gender = (('1','Male'),('2','Female'))


##Put your forms here

class ContactForm(forms.Form):
	name = forms.CharField(label="Name", max_length=40, initial="Your name")
	firstname = forms.CharField(label="Firstname",max_length=40, initial="You firstname")
	email = forms.EmailField(label="Email")
	gender = forms.ChoiceField(label="Gender",widget=forms.RadioSelect,choices=choice_gender) 
	message = forms.CharField(label="Message",initial="Type your message ...",widget=forms.Textarea)

	
