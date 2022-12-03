from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput
from .models import Person
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.utils import timezone
import re

# При разработке приложения, использующего базу данных, чаще всего необходимо работать с формами, которые аналогичны моделям.
# В этом случае явное определение полей формы будет дублировать код, так как все поля уже описаны в модели.
# По этой причине Django предоставляет вспомогательный класс, который позволит вам создать класс Form по имеющейся модели
# атрибут fields - указание списка используемых полей, при fields = '__all__' - все поля
# атрибут widgets для указания собственный виджет для поля. Его значением должен быть словарь, ключами которого являются имена полей, а значениями — классы или экземпляры виджетов.
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('surname', 'name', 'patronymic', 'sex', 'birthday', 'tribe', 'clan', 'phone', 'address', 'email', 'photo', 'details', 'father', 'mother')
        widgets = {
            'surname': TextInput(attrs={"size":"50"}),
            'name': TextInput(attrs={"size":"50"}),
            'patronymic': TextInput(attrs={"size":"50"}),
            'birthday': DateInput(attrs={"type":"date"}),
            'tribe': TextInput(attrs={"size":"50"}),
            'clan': TextInput(attrs={"size":"50"}),
            'phone': TextInput(attrs={"size":"50", "type":"tel"}),
            'address': TextInput(attrs={"size":"50"}),
            'email': TextInput(attrs={"size":"50", "type":"email"}),
            'details': Textarea(attrs={'cols': 50, 'rows': 5}),
            'father': forms.Select(attrs={'class': 'chosen'}),
            'mother': forms.Select(attrs={'class': 'chosen'}),
        }
        labels = {
            'father': _('father'),
            'mother': _('mother'),
        }
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['father'].queryset = Person.objects.filter(sex='М')
        self.fields['mother'].queryset = Person.objects.filter(sex='Ж')
    # Метод-валидатор для поля surname
    def clean_surname(self):
        data = self.cleaned_data['surname']
        # Ошибка если начинается не с большой буквы
        if data.istitle() == False:
            raise forms.ValidationError(_('Value must start with a capital letter'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля name
    def clean_name(self):
        data = self.cleaned_data['name']
        # Ошибка если начинается не с большой буквы
        if data.istitle() == False:
            raise forms.ValidationError(_('Value must start with a capital letter'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля name
    def clean_patronymic(self):
        data = self.cleaned_data['patronymic']
        # Ошибка если начинается не с большой буквы
        if data is not None:
            if len(data)>0:
                if data.istitle() == False:
                    raise forms.ValidationError(_('Value must start with a capital letter'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля birthday
    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        #print(data)
        #print(timezone.now())
        # Проверка даты (не больше текущей даты-времени)
        if data > timezone.now():
            raise forms.ValidationError(_('Cannot be greater than the current date'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data   
    # Метод-валидатор для поля phone
    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data is not None:
            result = re.match(r'^((\+?7|8)[ \-] ?)?((\(\d{3}\))|(\d{3}))?([ \-])?(\d{3}[\- ]?\d{2}[\- ]?\d{2})$', data)
            #print('result ',bool(result))  
            # Проверка телефонного номера по маске с помощью регулярного выражения
            if bool(result) == False:
                raise forms.ValidationError(_('Enter your phone number in the format +7-ХХХ-ХХХ-ХХХХ or 8-ХХХ-ХХХ-ХХХХ'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data
    # Метод-валидатор для поля email
    def clean_email(self):
        data = self.cleaned_data['email']
        if data is not None:
            # Проверка корректности адреса электронной почты
            if validate_email( data ) == False:
                raise forms.ValidationError(_('Please enter a valid email address'))
        # Метод-валидатор обязательно должен вернуть очищенные данные, даже если не изменил их
        return data

# Форма регистрации
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
