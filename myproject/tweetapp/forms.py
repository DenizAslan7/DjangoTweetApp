from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(max_length=50,label="username")
    message_input = forms.CharField(max_length=100,label="message",
                                    widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    

class AddTweetModelForms(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","message"]
        