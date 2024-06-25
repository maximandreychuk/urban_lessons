from django import forms
from .models import Booking, Message
from django.contrib.auth import get_user_model
from .validation import validate_data

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Электронная почта')
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)


class ContactMessageFrom(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'name', 'message',)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
        help_texts = {
            'username': None,
            'email': None,
            'password': None,
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError('Неверный формат email')
        elif User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Пользователь с таким email уже существует')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Пароль слишком короткий')

        return password

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )


# далее - Домашнее задание по теме "Джанго формы"
class BookingForm(forms.ModelForm):
    extraservice = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, required=False)

    class Meta:
        model = Booking
        fields = ('adults', 'tour_start_date')

    def clean_adults(self):
        adults = self.cleaned_data['adults']
        if adults < 1:
            raise forms.ValidationError(
                "Должен быть хотя бы один взрослый"
            )
