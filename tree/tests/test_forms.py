from django.test import TestCase

# Create your tests here.

from django.utils.translation import gettext_lazy as _

from ..forms import PersonForm
from ..models import Person
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
        
# Тесты формы PersonFormTests
class PersonFormTests(TestCase):
    # Тест лейблов полей        
    def test_field_labels(self):
        form = PersonForm()
        surname_label = form.fields['surname'].label
        self.assertEqual(surname_label, _('surname'))
        name_label = form.fields['name'].label
        self.assertEqual(name_label, _('name'))
        patronymic_label = form.fields['patronymic'].label
        self.assertEqual(patronymic_label, _('patronymic'))
        sex_label = form.fields['sex'].label
        self.assertEqual(sex_label, _('sex'))
        birthday_label = form.fields['birthday'].label
        self.assertEqual(birthday_label, _('birthday'))
        tribe_label = form.fields['tribe'].label
        self.assertEqual(tribe_label, _('tribe'))
        clan_label = form.fields['clan'].label
        self.assertEqual(clan_label, _('clan'))
        phone_label = form.fields['phone'].label
        self.assertEqual(phone_label, _('phone'))
        address_label = form.fields['address'].label
        self.assertEqual(address_label, _('address'))
        email_label = form.fields['email'].label
        self.assertEqual(email_label, _('email'))
        photo_label = form.fields['photo'].label
        self.assertEqual(photo_label, _('photo'))
        details_label = form.fields['details'].label
        self.assertEqual(details_label, _('details'))
        father_label = form.fields['father'].label
        self.assertEqual(father_label, _('father'))
        mother_label = form.fields['mother'].label
        self.assertEqual(mother_label, _('mother'))
        print("PersonFormTests.test_field_labels OK")
    # Тест создания новой записи
    def test_form_save(self):
        data = {"surname": "Иванов", 
                "name": "Иван", 
                "patronymic": "Иванович",
                "sex": "М",
                "birthday": timezone.now(),
                "tribe": "Арғын",
                "clan": "Қанжығалы",
                "phone": "+7-701-111-2222",
                "address": "ул. Ленина, 6-12",
                "email": "email@mail.ru",
                "photo": None,
                "details": "",
                "father": None,
                "mother": None}        
        form = PersonForm(data=data)
        self.assertTrue(form.is_valid())        
        self.assertIsInstance(form.save(), Person)
        print("PersonFormTests.test_form_save OK")
        
              

