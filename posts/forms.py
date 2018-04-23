from django	 import	forms
from .models import	Post
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'what is on your mind?'}), max_length=4000,help_text = 'Maximum length of the text is 4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']"""

class NewPostForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'placeholder':'what is on your mind?'}), max_length=4000,help_text = 'Maximum length of the text is 4000')
	class	Meta:
		model = Post
		fields	=	('subject',	'message')

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
