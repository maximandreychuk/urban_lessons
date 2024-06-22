from django import forms
from .models import Message


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class ContactMessageFrom(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'name', 'message',)
