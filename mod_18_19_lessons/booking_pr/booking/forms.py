from django import forms
from .models import Booking, Tourist
from django.contrib.auth import get_user_model


User = get_user_model()


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

    def clean_children(self):
        children = self.cleaned_data['children']
        if children < 0:
            raise forms.ValidationError(
                "Введите 0 если у вас нет детей"
            )
        return children

    def clean_adults(self):
        adults = self.cleaned_data['adults']
        if adults < 1:
            raise forms.ValidationError(
                "Должен быть хотя бы один взрослый"
            )
        return adults

    def clean(self):
        cleaned_data = super(BookingForm, self).clean()
        book_stdt = cleaned_data.get("start_date")
        tour_stdt = cleaned_data.get('tour').start_date
        book_enddt = cleaned_data.get("end_date")
        tour_enddt = cleaned_data.get('tour').end_date

        if book_stdt < tour_stdt:
            raise forms.ValidationError(
                "Дата начала бронирования не может быть раньше даты начала тура"
            )
        elif book_enddt > tour_enddt:
            raise forms.ValidationError(
                "Дата окончания бронирования не может быть позже даты окончания тура"
            )
        elif book_stdt >= book_enddt:
            raise forms.ValidationError(
                "Дата начала бронирования не может быть позже даты окончания бронирования"
            )


class TouristForm(forms.ModelForm):

    class Meta:
        model = Tourist
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'address', 'country', 'city', 'zip_code')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:
            raise forms.ValidationError('Неверный формат email')
        elif Tourist.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Пользователь с таким email уже существует')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if len(phone) != 11:
            raise forms.ValidationError(
                "Номер должен содержать 11 цифр"
            )
        return phone
