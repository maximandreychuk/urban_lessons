from django import forms
from .models import Booking, ExtraService, Message, Tour, Tourist
from django.contrib.auth import get_user_model


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

    class Meta:
        model = Booking
        fields = ('tour', 'start_date', 'end_date',
                  'adults', 'children', 'extraservice', 'pay_method')
        help_texts = {
            'extraservice': 'Дополнительные услуги',
        }

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['extraservice'].required = False

    def clean_extraservice(self):
        extraservice = self.cleaned_data['extraservice']
        if not extraservice:
            return None
        else:
            return extraservice

    def clean_adults(self):
        adults = self.cleaned_data['adults']
        if adults < 1:
            raise forms.ValidationError(
                "Должен быть хотя бы один взрослый"
            )
        return adults

    # def clean(self):
    #     cleaned_data = super(BookingForm, self).clean()
    #     book_stdt = cleaned_data.get('start_date')
    #     book_endt = cleaned_data.get('end_date')
        # if tour.objects.filter(start_date__gt=book_stdt):
        #     raise forms.ValidationError(
        #         "Дата начала tура не должна быть позже даты начала бронирования"
        #     )
        # elif tour.objects.filter(end_date__lte=book_endt):
        #     raise forms.ValidationError(
        #         "Дата окончания tура не должна быть раньше даты начала бронирования"
        #     )


class TouristForm(forms.ModelForm):

    class Meta:
        model = Tourist
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'address', 'country', 'city', 'zip_code')

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if '@' not in email:
                raise forms.ValidationError('Неверный формат email')
            elif Tourist.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    'Пользователь с таким email уже существует')

            return email

        def clean_phone_number(self):
            phone_number = self.cleaned_data.get('phone_number')
            if len(phone_number) != 10:
                raise forms.ValidationError(
                    'Номер должен содержать 10 цифр')
            if phone_number[0] != 7 or phone_number[0] != 8:
                raise forms.ValidationError(
                    'Номер должен начинаться на 7 или 8')
